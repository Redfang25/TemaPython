import pandas as pd
import matplotlib.pyplot as mat

df = pd.read_csv("data.csv")

df['Durata'] = pd.to_numeric(df['Durata'])
df['Puls'] = pd.to_numeric(df['Puls'])
df['MaxPuls'] = pd.to_numeric(df['MaxPuls'])
df['Calorii'] = pd.to_numeric(df['Calorii'])

mat.plot(df)
mat.show()

df_head = df.iloc[:7]
mat.plot(df_head)
mat.show()

df_end = df[['Puls', 'Durata']].tail(13)
#df_end2 = df['Durata'].tail(13)
#df_plot = pd.concat([df_end, df_end2])
mat.plot(df_end)
mat.show()
