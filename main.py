import pandas as pd
import csv
df=pd.read_csv('digital_behaviour.csv')
print(df.head(5))
print(df.tail(5))
print(df.shape)
print(df[['Instagram_Minutes','Study_Minutes']].describe())
print(df[['Date','Instagram_Minutes']])
print(df.columns)
print(df.info())
print(df['Instagram_Minutes'])
print(df['Instagram_Minutes'].sum())
print(df['Instagram_Minutes'].mean())
print(df['YouTube_Minutes'].max())
val=df[df['Instagram_Minutes']>100]
print(val)
val=df[df['Study_Minutes']>180]
print(val)
val=df[df['Instagram_Minutes']]
print(val)




