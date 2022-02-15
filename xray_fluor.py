# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 12:10:32 2021

@author: pc719
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math
import pandas as pd
import glob

#%%

path = r'H:/x-ray/fluor'
    
df = pd.read_csv(path + '/textdata/Cu_90_120s.txt', delimiter = '/t', engine = 'python')

df1 = pd.read_csv(path + '/csvdata/Cu_90_120s.csv')

dft = pd.read_csv(path + '/csvdata/*.csv')

#%%
csvfiles = glob.glob(path + '/csvdata/*.csv')

li = []

for filename in csvfiles:
    dft = pd.read_csv(filename, index_col = None, header = 0)
    li.append(dft)
    

