import pandas as pd

data=pd.read_csv("data/books.csv")
df=pd.DataFrame(data)

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df[['Title','Author']])
print(
    df[
      (
          (df['Genre']=='AI')
          |
          (df['Genre']=='programming')
          
      )
      &
      (df['Year']>2015)
    ]
)