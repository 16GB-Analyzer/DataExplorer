
import pandas as pd

data=pd.read_csv("data/books.csv")
df=pd.DataFrame(data)

"""print(df.head())
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
)"""

def menu():
    print("====== Data Explorer ======")
    print("1. View Dataset")
    print("2. Dataset Info")
    print("3. Statistics")
    print("4. Filter Books")
    print("5. Choose Book by Title")
    print("6. Exit")

    while True:
        choice = int(input("Enter your choice: "))
        if choice ==1:
            print(df.head())
        if choice ==2:
            print(df.info())
        if choice ==3:
            print(df.describe())
        if choice == 4:
            print("Avalable Genres: ", df['Genre'].unique())
            genre = input("Genre (Leave blank to skip): ")
            print("Avalable Authors: ", df['Author'].unique())
            author = input("Author (Leave blank to skip): ")
            print("Avalable Years: ", df['Year'].unique())
            year = input("Year (Leave blank to skip): ")
            rating = input("Minimum Rating (Leave blank to skip): ")
            Filtered_df=df
            if genre:
                Filtered_df=Filtered_df[Filtered_df['Genre']==genre]
            if author:
                Filtered_df=Filtered_df[Filtered_df['Author']==author]
            if year:
                Filtered_df=Filtered_df[Filtered_df['Year']==int(year)]
            if rating:
                Filtered_df=Filtered_df[Filtered_df['Rating']>=float(rating)]
            print("found",len(Filtered_df),"match/matches")
            storing = input("Do you want to store the filtered data? (y/n): ")
            if storing.lower()=='y':
                Filtered_df.to_csv("data/filtered_books.csv", index=False)
                print("Filtered data stored in 'data/filtered_books.csv'.")

            Filtered_df.sort_values(by='Rating',ascending=False)
            print(Filtered_df[['Title','Author','Rating']])
        if choice == 5:
            print("Enter the title")
            title = input("Title: ")
            results = df[df['Title'].str.contains(title, case=False)]
            if not results.empty:
                print(results)
            else:
                print("No results found.")
        elif choice == 6:
            print("Exiting the program.")
            break

menu()