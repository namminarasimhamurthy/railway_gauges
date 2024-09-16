import pandas as pd
df=pd.read_csv('railway_gauges.csv')
df.head()
df.iloc[[df['Total'].idxmax()]]
import matplotlib.pyplot as plt
df=df.drop('Total',axis=1)
ax=df.plot(x="Year",kind="bar")
plt.xticks(rotation=70)
plt.xlabel('year')
plt.ylabel('Total')
plt.title('Gauges:Number of railway tracks installed per year')
plt.savefig('railway_gauges.png')
plt.show()
