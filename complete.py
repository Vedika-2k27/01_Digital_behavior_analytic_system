#app name
import csv
APP = "Instagram"
minutes=[]
with open("digital_behaviour.csv","r",encoding="utf-8") as f:
    reader=csv.DictReader(f)  
    for row in reader:
        minutes.append(int(row["Instagram_Minutes"]))
        # minutes[start:stop:step]
        minutes[:7]
        total=sum(minutes)
        average=total/len(minutes)
        highest=max(minutes)
        lowest=min(minutes)
        counter=0
        for i in minutes:
            if i>average:
                counter+=1
        print(f"{APP}: Highest={highest}, Lowest={lowest}, Average={average:.2f}, Total={total}, Above Average={counter}")
        