# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 23:40:24 2021

@author: yaobv
"""
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from scipy.stats.mstats import winsorize
st.set_option('deprecation.showPyplotGlobalUse', False)

players = pd.read_csv(r'https://github.com/yaobviously/playerplotterB/blob/main/playboxscore2021.csv?raw=true')
todaysp = pd.read_csv(r'https://raw.githubusercontent.com/yaobviously/playerplotterB/main/slatetoday.csv')
todaysp = todaysp.sort_values(by='Salary', ascending=False)

playerlist = todaysp['Player'].to_list()
option = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

st.sidebar.header("Select Player")

player = st.sidebar.selectbox('Player', playerlist)
rollinginc = st.sidebar.selectbox('Rolling Average', option)

st.write("Player Usage and Production This Season")
         

def rollingplayer(player, option=8):
    _df = players21[players21['Player'] == x].reset_index()
    _df['RollingFP/36'] = _df['GameFP/36'].rolling(option, min_periods =2).mean()
    _df['rollingusage'] = _df['Usage'].rolling(option, min_periods = 2).mean()
    
    return sb.lineplot(data= _df[['MIN', 'Usage', 'PlayerFP', 'rollingfp']])



def playerdistribution(player, quantile=0.75):
    
    jc = players21.loc[players21['Player'] == name][['GameFP/36', 'MIN']]
    fp = winsorize(jc['GameFP/36'], [0.05, 0.05]).mean()    
    minutes = winsorize(jc['MIN'], [0.05, 0.05]).mean()
    cj = jc.T
    covariance = np.cov(cj)
    distribution = pd.DataFrame(multivariate_normal.rvs(mean = [fp, minutes], cov= covariance, size=1000))
    distribution['total'] = distribution[0]/36 * distribution[1]
    graph = sb.kdeplot(data=distribution['total'], fill=True)
    
    return graph, distribution['total'].quantile(quantile), covariance


st.pyplot()
