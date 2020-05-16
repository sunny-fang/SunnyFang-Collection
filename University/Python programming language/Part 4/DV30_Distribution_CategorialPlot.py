# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:06:00 2019

@author: user
"""

# conda install -c conda-forge seaborn 
# python -mpip install seaborn==0.9.0
#


# Load Dataset
titanic = sns.load_dataset("titanic")

# Plot
g = sns.catplot("alive", col="deck", col_wrap=4,
                data=titanic[titanic.deck.notnull()],
                kind="count", height=3.5, aspect=.8, 
                palette='tab20')

fig.suptitle('sf')
plt.show()