# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:05:54 2015

@author: Christopher M. Tasich
@organization: Vanderbilt University
"""
#%% Import packages

import os
import pandas as pd

#%% Import data

proj_dir = r'D:\Windows\Users\tasichcm\Dropbox (ISEE Bangladesh)\Programming\Python\Projects\P32 Met'
met_dir = os.path.join(proj_dir,'Data\Processed\met')
csv_dir = os.path.join(proj_dir,'Data\Processed\csv')

#%% Initiliaze variables and create directories

met_files = [f for f in os.listdir(met_dir) if os.path.isfile(os.path.join(
    met_dir,f)) and f.upper().endswith('.MET')]

#%% Process data

fn = ['Yr','Mon','Day','Hr','Min','Sec','Press (mBar)','Temp (C)'
    ,'Rel Hum (%)','Wind Spd (m/s)','Wind Dir (az)','Rain Int (mm/h)','Hail Int (hit/h)']
cols = [(0,3),(4,6),(7,9),(10,12),(13,15),(16,18),(18,25),(25,32),(32,39),(
    39,46),(46,53),(53,60),(60,67)]
data = pd.DataFrame()

for f in met_files:
    file = os.path.join(met_dir,f)
    if os.stat(file).st_size > 0:
        df = pd.read_fwf(file, skipinitialspace=True,skiprows=15,
                           colspecs=cols,header=None,names=fn)
        data = data.append(df)

data['Yr']=data['Yr']+2000
out = os.path.join(csv_dir,'data.csv')
data.to_csv(out,index=False)