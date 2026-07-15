import pandas as pd

data=pd.read_csv("data/books.csv")
df=pd.DataFrame(data)

print(df.head())