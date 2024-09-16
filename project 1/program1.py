import pandas as pd
import numpy as n
d = pd.read_csv('railway_gauges.csv')
print(d.head())
print("second output:")
print(d.iloc[d['Total'].idxmax()])
from  matplotlib import pyplot as m
d = d.drop('Total',axis=1)
ax = d.plot(x='Year',kind='bar')
m.xticks(rotation=70)
m.xlabel('year')
m.ylabel('Total')
m.title('gauges:number of railway tracks installed per year')
m.savefig('rail_gauges.png')
m.show()
