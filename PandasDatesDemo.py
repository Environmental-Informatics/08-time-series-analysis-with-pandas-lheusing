#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:18:12 2020

@author: lheusing

Work through the tutorial found at  http://earthpy.org/pandas-basics.html 
Time series analysis with pands written by nikolay koldunov
majority of commands done via shell line. 
Essential commands saved to script

"""

import pandas as pd 
import numpy as np
from pandas import Series, DataFrame, Panel 
pd.set_option('display.max_rows',15)

ao = np.loadtxt('monthly.ao.index.b50.current.ascii') #import data into time array
dates = pd.date_range('1950-01', periods=ao.shape[0], freq='M') #take dates off
AO = Series(ao[:,2], index = dates) #pair the date and value

nao = np.loadtxt('norm.nao.monthly.b5001.current.ascii')
dates_nao = pd.date_range('1950-01', periods =nao.shape[0], freq ='M')
NAO = Series(nao[:,2], index = dates_nao)

aonao = DataFrame({'AO' : AO, 'NAO':NAO}) #if the size is different then fill to longer one and fill shorter with NA

AO_mm = AO.resample("A").mean()  #resample to mean value

AO_md = AO.resample("A").mean()  #resample for median plot via command line

aonao.rolling(window=12, center = False).mean().plot(style='-g') #plot rolling mean for ao and nao