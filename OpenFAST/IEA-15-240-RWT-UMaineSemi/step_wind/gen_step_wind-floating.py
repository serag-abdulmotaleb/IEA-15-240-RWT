# -*- coding: utf-8 -*-
"""
Created on Sat May 13 12:41:48 2023

@author: seragela
"""
import os,glob
import numpy as np
import pandas as pd
from pyFAST.input_output.modify_input_files import modify_fst_deck,read_wind_files

# Common keys
dt = 0.025

fst_dir = r'..'
fst_file = r'IEA-15-240-RWT-UMaineSemi.fst'
out_dir = '.'

fst_dict = {'DT':dt,
            # module switches
            'CompElast': 1,
            'CompInflow':1,
            'CompAero':2,
            'CompServo':1,
            'CompHydro':1,
            'CompSub':0,
            'CompMooring':3,
            # output format
            'DT_Out':dt,
            'OutFileFmt':2}


elasto_dict = {
               # dofs switches
               'FlapDOF1':'True',
               'FlapDOF2':'True',
               'EdgeDOF':'True',
               'TeetDOF':'False',
               'DrTrDOF':'False',
               'GenDOF':'True',
               'YawDOF':'False',
               'TwFADOF1':'True',
               'TwFADOF2':'True',
               'TwSSDOF1':'True',
               'TwSSDOF2':'True',
               'PtfmSgDOF':'True',
               'PtfmSwDOF':'True',
               'PtfmHvDOF':'True',
               'PtfmRDOF':'True',
               'PtfmPDOF':'True',
               'PtfmYDOF':'True',
               # dof initial values
               'OoPDefl':0.,
               'IPDefl':0.,
               'BlPitch(1)':0.,
               'BlPitch(2)':0.,
               'BlPitch(3)':0.,
               'TeetDefl':0.,
               'Azimuth':0.,
               'RotSpeed':0.,
               'NacYaw':0.,
               'TTDspFA':0.,
               'TTDspSS':0.,
               'PtfmSurge':0.,
               'PtfmSway':0.,
               'PtfmHeave':0.,
               'PtfmRoll':0.,
               'PtfmPitch':0.,
               'PtfmYaw':0.,}

inflow_dict = {'WindType':2}

# Varying keys
wnd_file = r'StepWind.wnd'
wnd_data = np.loadtxt(wnd_file,delimiter=',')
fst_dict['TMax'] = wnd_data[-1,0]
## DLC1

inflow_dict['Filename_Uni'] = '"{}"'.format(os.path.relpath(wnd_file,out_dir))

suffix = '_step-wind_floating'
dof_suffix = ''
wind_suffix = ''

modify_fst_deck(fst_dir,fst_file,suffix=suffix,dof_suffix=dof_suffix,wind_suffix=wind_suffix,out_dir=out_dir,
                fst_dict=fst_dict,elasto_dict=elasto_dict,inflow_dict=inflow_dict)
    


