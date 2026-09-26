import pandas as pd
import csv
df=pd.read_csv('digital_behaviour.csv')
print(df.head(5))
print(df.tail(5))
print(df.shape)
print(df.describe())
print(df['Instagram_Minutes'])
print(df[['Instagram_Minutes','Study_Minutes']].describe())
print(df[['Date','Instagram_Minutes']])
print(df.columns)
print(df['Instagram_Minutes'].sum())
print(df['Study_Minutes'].mean())
print(df['YouTube_Minutes'].max())
print(df[df['Instagram_Minutes']>100])
print(df[df['Study_Minutes']>180])
print(df[(df['Instagram_Minutes']>100) & (df['Study_Minutes']<180)])
len(df[df['Instagram_Minutes']>100])
sorted_df=df.sort_values('Instagram_Minutes',ascending=False)
print(sorted_df)
print(sorted_df.head(5))
print(df.sort_values('Study_Minutes',ascending=False).head(5))
df['Total_Screen_Time']=df['Instagram_Minutes']+df['YouTube_Minutes']+df['WhatsApp_Minutes']+df['LinkedIn_Minutes']
df['Screen_Hours']=df['Total_Screen_Time']/60
df['Digital_Balance']=df['Study_Minutes']/df['Total_Screen_Time']
df['Day_Type']=df['Total_Screen_Time'].apply(lambda x: 'Heavy' if x>300 else 'Normal')

print("Instagram total:",df['Instagram_Minutes'].sum())
print("Youtube total:",df['YouTube_Minutes'].sum())
print("Whatsapp total:",df['WhatsApp_Minutes'].sum())
print("Linkedin total:",df['LinkedIn_Minutes'].sum())

app_totals = {'Instagram': df['Instagram_Minutes'].sum(),
              'YouTube': df['YouTube_Minutes'].sum(),
              'WhatsApp': df['WhatsApp_Minutes'].sum(),
              'LinkedIn': df['LinkedIn_Minutes'].sum()
             }
print(max(app_totals, key=app_totals.get))

print((df['Day_Type'] == 'Heavy').sum())

best_study = df.loc[df['Study_Minutes'].idxmax()]
print("Best study day:", best_study['Date'])
print("Study minutes:", best_study['Study_Minutes'])

heaviest_screen = df.loc[df['Total_Screen_Time'].idxmax()]
print("Heaviest screen day:", heaviest_screen['Date'])
print("Study on that day:", heaviest_screen['Study_Minutes'])

print(df['Digital_Balance'].mean())

df.to_csv('my_analysis.csv', index=False)








