# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:05:54 2015

@author: Christopher M. Tasich
@organization: Vanderbilt University
"""
#%% Import packages

import os,subprocess

#%% Import data

proj_dir = r'C:/Projects/Vanderbilt/p32_met'
in_data = os.path.join(proj_dir,'data/raw')

#%% Initiliaze variables and create directories

# Conversion programs
runpkr00 = os.path.join(proj_dir,r'bin\runpkr00.exe')
teqc = os.path.join(proj_dir,r'bin\teqc.exe')

# Make directories
out_data = os.path.join(proj_dir,'data/processed')
tgd_dir = os.path.join(out_data,'tgd')
obs_dir = os.path.join(out_data,'obs')
met_dir = os.path.join(out_data,'met')

if not os.path.exists(out_data):
    os.makedirs(out_data)
if not os.path.exists(tgd_dir):
    os.makedirs(tgd_dir)
if not os.path.exists(obs_dir):
    os.makedirs(obs_dir)
if not os.path.exists(met_dir):
    os.makedirs(met_dir)

raw_files = [f[:-4] for f in os.listdir(in_data) if os.path.isfile(os.path.join(
    in_data,f)) and f.upper().endswith('T02')]
    
tgd_files = [f[:-4] for f in os.listdir(tgd_dir) if os.path.isfile(os.path.join(
    tgd_dir,f)) and f.upper().endswith('.TGD')]

#%% Process data

# Determine files to be processed
t02_list = [f for f in raw_files if not f in tgd_files] # will be used in runpkr00

count=0
if not t02_list:
    print 'No new t02 files to process.'
else:
    for f in t02_list:
        subprocess.call([runpkr00,'-d','-g', os.path.join(
            in_data,f+'.t02'),os.path.join(tgd_dir,f)])
        count = count + 1
    print 'Processed %i t02 file(s).' % count
    
tgd_files = [f[:-4] for f in os.listdir(tgd_dir) if os.path.isfile(os.path.join(
    tgd_dir,f)) and f.upper().endswith('.TGD')]

obs_files = [f[:-4] for f in os.listdir(obs_dir) if os.path.isfile(os.path.join(
    obs_dir,f)) and f.upper().endswith('.OBS')]

met_files = [f[:-4] for f in os.listdir(met_dir) if os.path.isfile(os.path.join(
    met_dir,f)) and f.upper().endswith('.MET')]

tgd_list = [f for f in tgd_files if f not in obs_files or f not in met_files]

count = 0
if not tgd_list:
    print 'No new tgd files to process.'
else:
    for f in tgd_list:
        subprocess.call([teqc,'+met', os.path.join(met_dir,f+'.met'),os.path.join(
            tgd_dir,f+'.tgd'),'>',os.path.join(obs_dir,f+'.obs')],shell=True)
        count = count + 1
    print 'Processed %i tgd file(s).' % count