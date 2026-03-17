import pandas as pd

df = pd.read_csv("data/GUIDE_Train.csv", nrows=100000)

print(df.head())
print(df.shape)