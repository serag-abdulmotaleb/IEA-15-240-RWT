# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:01:55 2022

@author: seragela
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def gen_step_wind(T_sim,T_trans,dt_dat,U_min,U_step,steps,file_name):

    T_max = (steps + 1)*T_sim + steps*T_trans
    Tdat = np.around(np.linspace(0, T_max, round(T_max/dt_dat)+1),3)
    Vh_ref = np.zeros((len(Tdat)))
    
    for step in range(steps+1):
        sim1 = round(step*(T_sim+T_trans)/dt_dat)
        trans1 = sim1 + round(T_sim/dt_dat)
        trans2 = trans1 + round(T_trans/dt_dat)
        
        for t in Tdat[sim1:trans2]:
            Vh_ref[round(t/dt_dat)] = U_min + U_step*np.floor(t/(T_sim+T_trans))
        for t in Tdat[trans1:trans2]:
            Vh_ref[round(t/dt_dat)] += U_step/T_trans*(t-Tdat[trans1])
    
    Delta = np.zeros((len(Tdat)))
    
    
    Vz = np.zeros((len(Tdat)))
    HLinShr = np.zeros((len(Tdat)))
    VShr = np.zeros((len(Tdat))) + 0.14
    VLinShr = np.zeros((len(Tdat)))
    VGust = np.zeros((len(Tdat)))
    cols = ['#Tdat','Vh_ref','Delta','Vz','HLinShr','VShr','VLinShr','VGust']
    
    data = np.array([Tdat,Vh_ref,Delta,Vz,HLinShr,VShr,VLinShr,VGust]).transpose()
    
    df = pd.DataFrame(data,columns = cols)
    plt.plot(Tdat,Vh_ref)
    
    df.to_csv(file_name,index=False)
    
def main():
    T_sim = 600
    T_trans = 100
    dt_dat = 100
    U_min = 4
    U_step = 1
    steps = 21
    file_name = 'StepWind.wnd'
    
    gen_step_wind(T_sim,T_trans,dt_dat,U_min,U_step,steps,file_name)
    
if __name__ == "__main__":
    main()