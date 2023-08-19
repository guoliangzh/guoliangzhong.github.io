# -*- coding: utf-8 -*-
# Hang Xiao 2023.04
# xiaohang007@gmail.com
import os,sys,glob,json


with open('./results.csv','w')as f:
    f.write('name,structureMatcher_bool,structureGraph_distance\n')
result_csv=''

for root,dirs,files in os.walk('./'):
    for f in files:
        if f.endswith('result.csv') :
            with open(os.path.join(root, f),'r') as result:
                result_csv += result.read()
with open("results.csv",'a') as result:
    result.write(result_csv)
result_sci=""
for root,dirs,files in os.walk('./'):
    for f in files:
        if f.endswith('result.sci') :
            with open(os.path.join(root, f),'r') as result:
                result_sci += result.read()
with open("./prior_aug.sli",'w') as result:
    result.write(result_sci)

for i in glob.glob("job_*"):
    os.system("rm -r "+i)
                           
                
                
