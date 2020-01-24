# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:43:26 2020

@author: Muskan Lalit
"""

# Thompson Sampling
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

import random
N = 10000
d = 10
ads_selected = []
total_reward = 0
number_of_rewards_1 = [0] * d
number_of_rewards_0 = [0] * d
for n in range (0, N):
    ad = 0
    max_reward = 0
    for i in range(0, d):
        random_beta = random.betavariate(number_of_rewards_1[i] + 1, number_of_rewards_0[i] + 1)
        if random_beta > max_reward :
            max_reward = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    if reward == 0:
        number_of_rewards_0[ad] = number_of_rewards_0[ad] + 1
    else:
        number_of_rewards_1[ad] = number_of_rewards_1[ad] + 1
    total_reward = total_reward + reward


plt.hist(ads_selected)
plt.title('Histogram of ad selections')
plt.xlabel('Ads')
plt.ylabel('Number of times ad was selected')
plt.show()