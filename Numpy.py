import numpy as np
import csv
insta_list=[]
study_time=[]
with open("digital_behaviour.csv","r",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        insta_list.append((int)(row["Instagram_Minutes"]))
        study_time.append((int)(row["Study_Minutes"]))
    insta_list=insta_list[:7]
    study_tim
    e=study_time[:7]
    insta_array=np.array(insta_list)
    study_array=np.array(study_time)
    # total=np.sum(insta_array)
    total=insta_array.sum()
    average=insta_array.mean()
    maximum=np.max(insta_array)
    minimum=np.min(insta_array)
    print(f"sum of the values of seven days :{total},{average},{maximum},{minimum}")
    insta_array[0]
    insta_array[-1]  #vectors
    insta_array[0:3] #slicing
    insta_array[-3::] #Slicing with step
    insta_array[1:4] 
    # insta_array=[val/60 for val in insta_array]      insta_array=numpy array
    hours=insta_array/60
    diff=insta_array-study_array

    # boolean filtering
    # [value>100 for val in insta_array]
greater_than_100=insta_array>100
# [val for val in greater_than_100 if val]
#[val for val in insta_array if val>1
greater=insta_array[insta_array>100]
count=(insta_array>100).sum()
average=insta_array.mean()
greater=insta_array[insta_array>average]
