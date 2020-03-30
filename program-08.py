#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:20:37 2020

@author: lheusing 

using "WabashRiver_DailyDischarge_20150317-20160324.txt" create 3 pdf figures of daily mean
monthly mean and the top 10 values for daily flow on the same x axis for the plots. 
use pandas read_table to import the data into DataFrames and go from there.
Reference PandasDatesDemo.py for useful tips /examples of how to do this
"""
import matplotlib.pyplot as plt
import numpy as np
import datetime
import pandas as pd
from pandas import Series, DataFrame, Panel 

data = pd.read_table('WabashRiver_DailyDischarge_20150317-20160324.txt', skiprows=25,sep='\t') #import data
times = pd.date_range('2015-03-17 00:00', periods=data.shape[0], freq='15T') #collect and create time stamps

flow = data.iloc[:,4].values #rip flow data
flowtime = Series(flow, index = times) 

flowtime_mean = flowtime.resample("D").mean() #resamples mean for daily
fig = flowtime_mean.plot() 
fig.set_ylabel('daily mean discharge (cf)')
plt.savefig('daily mean flow.pdf')
plt.close()


top = flowtime_mean.nlargest(10,keep='first') #take top 10 values and plot them
fig = top.plot(style='^r') 
fig.set_xlim(times[0],times[-1]) #use same x axis as before
fig.set_ylabel('discharge (cf)')
plt.savefig('10 max flow days.pdf')
plt.close()


flowtime_mean_month = flowtime.resample("M").mean()
fig = flowtime_mean_month.plot()
fig.set_ylabel('monthly mean flow (cf)')
plt.savefig('monthly mean flow.pdf')