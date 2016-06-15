# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:05:54 2015

@author: Christopher M. Tasich
@organization: Vanderbilt University
"""
#%% Import packages

from ftplib import FTP
import os

#%% Import packages

local_dir = r'C:/Projects/Vanderbilt/p32_met/data/raw'
local_files = os.listdir(local_dir)

try:
    ftp = FTP('data-out.unavco.org')
except:
    print "Couldn't connect to server"
ftp.login()
ftp.cwd('/private/mSJzLcSUg.pqklBundG4=r0')
serv_files = ftp.nlst()

down_files = [f for f in serv_files if not f in local_files and f.upper().startswith('PD32')]

for f in down_files:
    with open(os.path.join(local_dir,f),'wb') as file:
        ftp.retrbinary('RETR '+f,file.write)