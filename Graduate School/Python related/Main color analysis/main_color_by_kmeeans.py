#%%
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import os, time
import cv2
os.chdir('D:\\研究所(2019.9.23)\\碩一上\\DIGI\\專案\\pic')
pic = '2.png'

#%%
def get_main_color_by_kmeans(pic,k):    
    #k=5
    image = cv2.imread(pic)
    resize_img = cv2.resize(image,(128,128))
    img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2LAB)
    img_ori_shape = img.shape
    img1 = img.reshape((img_ori_shape[0] * img_ori_shape[1], img_ori_shape[2]))
    img_shape = img1.shape
    
    n_channels = img_shape[1]
    
    estimator = KMeans(n_clusters=k, max_iter=5, init='k-means++', n_init=5)  # 建立分類器
    estimator.fit(img1)  # 分類
    centroids = estimator.cluster_centers_   
    colorLabels = list(estimator.labels_)
       
    colorInfo = {}
    for center_index in range(k):
        colorRatio = colorLabels.count(center_index)/len(colorLabels)
        colorInfo[colorRatio] = centroids[center_index]
    
    colorInfo = [(k,colorInfo[k]) for k in sorted(colorInfo.keys(), reverse=True)] 
    a = ''
    for color in colorInfo:
        #print('比例：', color[0], '颜色：', color[1])
        #print('比例:{:.4f}\t顏色:{}\n'.format(color[0],color[1]))
        aa = '比例:{:.4f}\t顏色:{}\n'.format(color[0],cv2.cvtColor(color[1].reshape((1, 1, n_channels)).astype('uint8'), cv2.COLOR_LAB2RGB).reshape((n_channels)))
        a += aa
    
    result = []
    result_width = 200
    result_height_per_center = 80
    for center_index in range(k):
        result.append(np.full((result_width * result_height_per_center, n_channels), colorInfo[center_index][1], dtype=int))
    result = np.array(result)
    result = result.reshape((result_height_per_center * k, result_width, n_channels))
    result1 = cv2.cvtColor(result.astype('uint8'), cv2.COLOR_LAB2RGB)
    
    plt.imshow(result1)
    print(a)
    
#%%
get_main_color_by_kmeans(pic,5)
    


























 