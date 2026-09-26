import random as rd

#print(rd.seed.__doc__)
x=10
#print(x.__doc__)

import datetime
#print(datetime.timedelta.__doc__)

p=datetime.datetime.now()
q=datetime.timedelta()
print(p,q,sep="\n")
print(p-q)
r=datetime.timedelta(days=10)
print(p-r)