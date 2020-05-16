#%%
from sklearn import preprocessing
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
import lightgbm as lgb
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, precision_recall_curve, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns 
import os
#%%
os.chdir('D:\\研究所(2019.9.23)\\碩一上\\國泰大數據競賽\\刪變數後資料集')
data = pd.read_csv('train5-3.csv', encoding = 'Big5', float_precision = '10')
data = data.drop(['CUS_ID'], axis=1)
#pd.set_option("display.precision", 10)
data[['INSD_LAST_YEARDIF_CNT','LIFE_INSD_CNT']].describe()
#plt.hist(new_data['INSD_LAST_YEARDIF_CNT'])
#plt.hist(new_data['LIFE_INSD_CNT'])
# MaxAbs標準化
# 建立MinMaxScaler物件
#maxabs = preprocessing.MaxAbsScaler()
# 右偏變數處理
data[['INSD_LAST_YEARDIF_CNT','LIFE_INSD_CNT']] = data[['INSD_LAST_YEARDIF_CNT','LIFE_INSD_CNT']]*10000+10
#a = maxabs.fit_transform(a)
plt.hist(data['INSD_LAST_YEARDIF_CNT'])# 和下面那行框一起跑
plt.hist(data['LIFE_INSD_CNT'])
# 變數取log
data[['INSD_LAST_YEARDIF_CNT','LIFE_INSD_CNT']] = np.log(data[['INSD_LAST_YEARDIF_CNT','LIFE_INSD_CNT']])
plt.hist(data['INSD_LAST_YEARDIF_CNT'])
plt.hist(data['LIFE_INSD_CNT'])
# 新增變數，初步檢查準確率沒有比較高
#data['SUM_OF_INSD_LAST_YEARDIF_CNT_AND_LIFE_INSD_CNT'] = data['INSD_LAST_YEARDIF_CNT'] + data['LIFE_INSD_CNT']

# 將y轉為0,1型態、將資料轉為lgbm可理解的型態
data['Y1'] = data['Y1'].replace(['Y', 'N'], [1, 0])
# one-hot encoding
new_data = get_dummies(['GENDER','AGE','CHARGE_CITY_CD','CONTACT_CITY_CD','EDUCATION_CD','MARRIAGE_CD',
                        'INSD_1ST_AGE','APC_1ST_AGE','RFM_R','REBUY_TIMES_CNT','LIFE_CNT','CUST_9_SEGMENTS_CD'], data)
for i in new_data.columns:
    col_type = new_data[i].dtype
    if col_type == 'object' or col_type.name == 'category':
        new_data[i] = new_data[i].astype('category')
X = new_data.drop(['Y1'], axis = 1)
target = new_data['Y1']
X_train,X_test,y_train,y_test =train_test_split(X,target,test_size=0.2, random_state=0)
params = {
    'boosting_type': 'gbdt', 
    'objective': 'binary', 
    'metric': 'auc',
    'learning_rate': 0.1, 
    'num_leaves': 200, 
    'max_depth': 8,
    'subsample': 0.8, 
    'colsample_bytree': 0.8, 
    }    
data_train = lgb.Dataset(X_train, y_train, silent=True)
cv_results = lgb.cv(
    params, data_train, num_boost_round=1000, nfold=5, stratified=False, shuffle=True, metrics='rmse',
    early_stopping_rounds=50, verbose_eval=50, show_stdv=True, seed=0)

print('best n_estimators:', len(cv_results['rmse-mean']))# best n_estimators: 22
print('best cv score:', cv_results['rmse-mean'][-1])
#%%
# 開始調參
from sklearn.model_selection import GridSearchCV
params_test1={'max_depth': range(3,8,1), 'num_leaves':range(5, 100, 5)}    
params_test1={'max_depth': [5], 'num_leaves':range(18, 23, 1)} 
gsearch1 = GridSearchCV(estimator = lgb.LGBMClassifier(boosting_type='gbdt',objective='binary',metrics='auc',learning_rate=0.1, n_estimators=22), 
                       param_grid = params_test1, scoring='roc_auc',cv=10,n_jobs=-1)
gsearch1.fit(X_train,y_train)
gsearch1.best_params_, gsearch1.best_score_    # 'max_depth': 5, 'num_leaves': 21

params_test2={'max_bin': range(5,256,10), 'min_data_in_leaf':range(1,102,10)}
params_test2={'max_bin': range(53,58,1), 'min_data_in_leaf':range(99,104,1)}
gsearch2 = GridSearchCV(estimator = lgb.LGBMClassifier(boosting_type='gbdt',objective='binary',metrics='auc',learning_rate=0.1, n_estimators=22, max_depth=5, num_leaves=21), 
                       param_grid = params_test2, scoring='roc_auc',cv=10,n_jobs=-1)
gsearch2.fit(X_train,y_train)
gsearch2.best_params_, gsearch1.best_score_    # 'max_bin': 55, 'min_data_in_leaf': 100

params_test3={'feature_fraction': [0.6,0.7,0.8,0.9,1.0],
              'bagging_fraction': [0.6,0.7,0.8,0.9,1.0],
              'bagging_freq': range(0,81,10)
}
gsearch3 = GridSearchCV(estimator = lgb.LGBMClassifier(boosting_type='gbdt',objective='binary',metrics='auc',learning_rate=0.1, n_estimators=22, max_depth=5, num_leaves=21, max_bin=55, min_data_in_leaf=100), 
                       param_grid = params_test3, scoring='roc_auc',cv=10,n_jobs=-1)
gsearch3.fit(X_train,y_train)
gsearch3.best_params_, gsearch3.best_score_    # 'bagging_fraction': 0.9, 'bagging_freq': 10, 'feature_fraction': 1

params_test4={'lambda_l1': [1e-5,1e-3,1e-1,0.0,0.1,0.3,0.5,0.7,0.9,1.0],
              'lambda_l2': [1e-5,1e-3,1e-1,0.0,0.1,0.3,0.5,0.7,0.9,1.0]
}     
gsearch4 = GridSearchCV(estimator = lgb.LGBMClassifier(boosting_type='gbdt',objective='binary',metrics='auc',learning_rate=0.1, n_estimators=22, max_depth=5, num_leaves=21, max_bin=55, min_data_in_leaf=100, 
                                                       bagging_fraction=0.9,bagging_freq= 10, feature_fraction= 1), 
                       param_grid = params_test4, scoring='roc_auc',cv=10,n_jobs=-1)
gsearch4.fit(X_train,y_train)
gsearch4.best_params_, gsearch4.best_score_    # 'lambda_l1': 0.001, 'lambda_l2': 1e-05

params_test5={'min_split_gain':[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]}
gsearch5 = GridSearchCV(estimator = lgb.LGBMClassifier(boosting_type='gbdt',objective='binary',metrics='auc',learning_rate=0.1, n_estimators=22, max_depth=5, num_leaves=21, max_bin=55, min_data_in_leaf=100,
                                                       bagging_fraction=0.9,bagging_freq= 10, feature_fraction= 1,
                        lambda_l1=0.001,lambda_l2=1e-05), param_grid = params_test5, scoring='roc_auc',cv=10,n_jobs=-1)
gsearch5.fit(X_train,y_train)
gsearch5.best_params_, gsearch5.best_score_    # 'min_split_gain': 0.0
#%%
# 再測一次n_eatimator
params = {
          'boosting_type': 'gbdt',
          'objective': 'binary',
          'metric': 'auc',
          'nthread':4,
          'learning_rate':0.005,
          'num_leaves':21, 
          'max_depth': 5,   
          'subsample': 0.8, 
          'colsample_bytree': 0.8, 
          'max_bin':55,
          'min_data_in_leaf':100,
          'min_split_gain': 0.0, 
          'bagging_fraction':0.9,'bagging_freq': 10, 'feature_fraction': 1,
          'lambda_l1':0.001, 'lambda_l2':1e-05
    }    
data_train = lgb.Dataset(X_train, y_train, silent=True)
cv_results = lgb.cv(
    params, data_train, num_boost_round=1000, nfold=5, stratified=False, shuffle=True, metrics='rmse',
    early_stopping_rounds=50, verbose_eval=50, show_stdv=True, seed=0)

print('best n_estimators:', len(cv_results['rmse-mean']))# best n_estimators: 原為22，變969
print('best cv score:', cv_results['rmse-mean'][-1])

#%%
# test
os.chdir('D:\\研究所(2019.9.23)\\碩一上\\國泰大數據競賽\\刪變數後資料集')
test_data = pd.read_csv('test5-3.csv', encoding = 'Big5', float_precision = '10')
test_data = test_data.drop(['CUS_ID'], axis=1)
test_data[['INSD_LAST_YEARDIF_CNT','LIFE_INSD_CNT']] = test_data[['INSD_LAST_YEARDIF_CNT','LIFE_INSD_CNT']]*10000+10
plt.hist(test_data['INSD_LAST_YEARDIF_CNT'])# 和下面那行框一起跑
plt.hist(test_data['LIFE_INSD_CNT'])
# 變數取log
test_data[['INSD_LAST_YEARDIF_CNT','LIFE_INSD_CNT']] = np.log(test_data[['INSD_LAST_YEARDIF_CNT','LIFE_INSD_CNT']])
plt.hist(test_data['INSD_LAST_YEARDIF_CNT'])
plt.hist(test_data['LIFE_INSD_CNT'])
test_data = get_dummies(['GENDER','AGE','CHARGE_CITY_CD','CONTACT_CITY_CD','EDUCATION_CD','MARRIAGE_CD',
                        'INSD_1ST_AGE','APC_1ST_AGE','RFM_R','REBUY_TIMES_CNT','LIFE_CNT','CUST_9_SEGMENTS_CD'], test_data)
for i in test_data.columns:
    col_type = test_data[i].dtype
    if col_type == 'object' or col_type.name == 'category':
        test_data[i] = test_data[i].astype('category')
#%%
model = lgb.LGBMClassifier(boosting_type='gbdt',objective='binary',metrics='auc',learning_rate=0.005, 
                           n_estimators=969, max_depth=5, num_leaves=21,max_bin=55,min_data_in_leaf=100,bagging_fraction=0.9,bagging_freq= 10, feature_fraction= 1,
                           lambda_l1=0.001,lambda_l2=1e-05, min_split_gain=0)
model.fit(X_train, y_train)
probabilities = model.predict_proba(test_data)
buy_prob = probabilities[:,1]
will_buy = buy_prob[buy_prob > 0.4]  
#%%
os.chdir('D:\\研究所(2019.9.23)\\碩一上\\國泰大數據競賽\\預測機率')
type(buy_prob)
dataframe = pd.DataFrame(buy_prob)
dataframe.to_csv("lgbmclassifiertest06.csv",index=False,sep=',')





































