# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 11:26:20 2021

@author: WG6165
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math


df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)),columns=('apples', 'bicycles', 'fanatics', 'lizards'))

fig, ax = plt.subplots(nrows = 4)
plt.subplots_adjust(wspace = 0, hspace = 0.05)

ax[0].plot(df.index, df['apples'],'.',color = 'red', Markersize = 5)
ax[1].plot(df.index, df['bicycles'],'.',color = 'purple', Markersize = 5)
ax[2].plot(df.index, df['fanatics'],'.',color = 'blue', Markersize = 5)
ax[3].plot(df.index, df['lizards'],'.',color = 'green', Markersize = 5)

