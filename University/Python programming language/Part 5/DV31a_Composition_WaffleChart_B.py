# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:30:25 2019

@author: user
"""

#! pip install pywaffle
from pywaffle import Waffle
# 從模組pywaffle中匯入Waffle

# Import
df_raw = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
# 將括號中的資料讀近來，並命名為df(已於DV_00中定義pd為pandas)

# Prepare Data
# By Class Data
df_class = df_raw.groupby('class').size().reset_index(name='counts_class')
# 將資料依據class變數分組，並計算每一組中的資料個數，接著將資料重新還原為默認的索引，命名為df_class
n_categories = df_class.shape[0]
# 讀取矩陣第一維度的長度，並命名為n_categories
colors_class = [plt.cm.Set3(i/float(n_categories)) for i in range(n_categories)]
# 建立色彩表，並依據n_categories中的個數決定顏色的種類數

# By Cylinders Data
df_cyl = df_raw.groupby('cyl').size().reset_index(name='counts_cyl')
# 將資料依據cyl變數分組，並計算每一組中的資料個數，接著將資料重新還原為默認的索引，命名為df_cyl
n_categories = df_cyl.shape[0]
# 讀取矩陣第一維度的長度，並命名為n_categories
colors_cyl = [plt.cm.Spectral(i/float(n_categories)) for i in range(n_categories)]
# 建立色彩表，並依據n_categories中的個數決定顏色的種類數

# By Make Data
df_make = df_raw.groupby('manufacturer').size().reset_index(name='counts_make')
# 將資料依據manufacturer變數分組，並計算每一組中的資料個數，接著將資料重新還原為默認的索引，命名為df_make
n_categories = df_make.shape[0]
# 讀取矩陣第一維度的長度，並命名為n_categories
colors_make = [plt.cm.tab20b(i/float(n_categories)) for i in range(n_categories)]
# 建立色彩表，並依據n_categories中的個數決定顏色的種類數

# Draw Plot and Decorate
fig = plt.figure(
    FigureClass=Waffle,
    plots={
        '311': {
            'values': df_class['counts_class'],
            'labels': ["{1}".format(n[0], n[1]) for n in df_class[['class', 'counts_class']].itertuples()],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.05, 1), 'fontsize': 12, 'title':'Class'},
            'title': {'label': '# Vehicles by Class', 'loc': 'center', 'fontsize':18},
            'colors': colors_class
        },
# 繪製waffle chart，並設定資料來自於df_class；圖例為Class、字型大小為12、位於右上角(位置為1.05,1)；標題為# Vehicles by Class、字型大小為12、位置為圖的中間；顏色為colors_class
        '312': {
            'values': df_cyl['counts_cyl'],
            'labels': ["{1}".format(n[0], n[1]) for n in df_cyl[['cyl', 'counts_cyl']].itertuples()],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.05, 1), 'fontsize': 12, 'title':'Cyl'},
            'title': {'label': '# Vehicles by Cyl', 'loc': 'center', 'fontsize':18},
            'colors': colors_cyl
        },
# 繪製waffle chart，並設定資料來自於df_cyl；圖例為Cyl、字型大小為12、位於右上角(位置為1.05,1)；標題為# Vehicles by Cyl、字型大小為12、位置為圖的中間；顏色為colors_cyl
        '313': {
            'values': df_make['counts_make'],
            'labels': ["{1}".format(n[0], n[1]) for n in df_make[['manufacturer', 'counts_make']].itertuples()],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.05, 1), 'fontsize': 12, 'title':'Manufacturer'},
            'title': {'label': '# Vehicles by Make', 'loc': 'center', 'fontsize':18},
            'colors': colors_make
        }
    },
# 繪製waffle chart，並設定資料來自於df_make；圖例為Manufacturer、字型大小為12、位於右上角(位置為1.05,1)；標題為# Vehicles by Make、字型大小為12、位置為圖的中間；顏色為colors_make
    rows=9,
    figsize=(16, 14)
)
# 設定圖的大小及圖形的列數