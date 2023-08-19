# -*- coding: utf-8 -*-
# Hang Xiao 2023.04
# xiaohang007@gmail.com
import os,sys,glob
import re
import numpy as np
import math,json


def split_list(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

os.system('rm -rf job_* structures_ori_opt ./result.csv temp.csv')
#os.mkdir("structures_ori_opt")
threads=100


with open('../5_eform_m3gnet/results_5_eform_m3gnet.csv', 'r') as f:
    cifs=f.readlines()
cifs_split=list(split_list(cifs[1:],threads))

for i in range(len(cifs_split)):
    os.mkdir('job_'+str(i))
    os.system('cp -r ./workflow/. job_'+str(i))
    with open('temp.csv', 'w') as f:
        f.writelines(cifs_split[i])
    os.system('cp temp.csv job_'+str(i))

    os.chdir('job_'+str(i))
    if len(sys.argv)==2:
        if sys.argv[1]=="test":
            os.system('yhbatch 0_test.pbs')
    else:
        os.system('yhbatch 0_run.sh')
    os.chdir('..')
os.system('rm temp.csv')

