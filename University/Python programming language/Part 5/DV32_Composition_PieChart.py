# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:32:00 2019

@author: user
"""

# Import
df_raw = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

# Prepare Data
df = df_raw.groupby('class').size()

# Make the plot with pandas
#df.plot(kind='pie', subplots=True, figsize=(8, 8)), dpi= 80)
df.plot(kind='pie', subplots=True, figsize=(8, 8)))
plt.title("Pie Chart of Vehicle Class - Bad")
plt.ylabel("")
plt.show()