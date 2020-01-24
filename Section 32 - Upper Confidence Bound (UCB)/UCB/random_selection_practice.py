# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 01:44:59 2020

@author: Muskan Lalit
"""
#%reset -f
# Random Selection
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Ads_CTR_Optimisation.csv')

import random
N = 10000
d = 10
ads_selected = []
total_reward = 0
for n in range (0,N):
    
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    total_reward = total_reward + reward

plt.hist(ads_selected)
plt.title('Histogram of random selection')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
    
