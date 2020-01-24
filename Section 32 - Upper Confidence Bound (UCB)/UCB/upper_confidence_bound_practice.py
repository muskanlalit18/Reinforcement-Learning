# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 01:46:15 2020

@author: Muskan Lalit
"""

# UCB
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

import math
N = 10000
d = 10
ads_selected = []
total_reward = 0
number_of_selections = [0] * d
sum_of_rewards = [0] * d
for n in range (0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if(number_of_selections[i]>0):
            average_reward = sum_of_rewards[i] / number_of_selections[i]
            delta_i = math.sqrt(1.5 * math.log(n+1)/number_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound :
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    number_of_selections[ad] = number_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sum_of_rewards[ad] = sum_of_rewards[ad] + reward
    total_reward = total_reward + reward


plt.hist(ads_selected)
plt.title('Histogram of ad selections')
plt.xlabel('Ads')
plt.ylabel('Number of times ad was selected')
plt.show()