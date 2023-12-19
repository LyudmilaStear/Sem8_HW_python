import pandas as pd
df = pd.read_csv('california_housing_train.csv')
mask = (df['population'] > 0) & (df['population'] < 500)
filtered_df = df[mask]
avg = filtered_df['median_house_value'].mean()

