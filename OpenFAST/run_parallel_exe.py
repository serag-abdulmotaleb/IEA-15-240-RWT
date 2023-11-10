# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:17:27 2022

@author: seragela
"""

import os,glob,subprocess
import multiprocessing as mp

def run_cmd(cmds):
    subprocess.run(["start","/wait","cmd","/c",cmds[0],cmds[1]],shell=True)

def run_parallel_exe(exe_file,input_files,sessions):

    cmds = [[exe_file,inp] for inp in input_files]
    worker = mp.Pool(sessions)
    worker.map(run_cmd,cmds)

if __name__ == '__main__':
    exe_file = r'..\..\openfastv3.5.1_x64.exe'
    
    input_files = glob.glob('*.fst')
    
    sessions = 36
    run_parallel_exe(exe_file,input_files,sessions)