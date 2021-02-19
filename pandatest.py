import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('titanic_data.csv')
print(df.describe())

print(df.info())

sns.scatterplot(data=df, x='Age', y='Pclass', hue='Sex')
plt.xlabel('Age of person')
plt.show()

