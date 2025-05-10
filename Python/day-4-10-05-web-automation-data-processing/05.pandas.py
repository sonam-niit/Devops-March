import pandas as pd

data = [
    {"Title":"Python 101","Price":29.99,"Rating":5},
    {"Title":"Learn pandas","Price":23.99,"Rating":4},
    {"Title":"Web Scraping guide","Price":19.99,"Rating":4},
    {"Title":"Machine Learning Basics","Price":34.99,"Rating":3},
    {"Title":"Data Science Handbook","Price":39.99,"Rating":5}
]

df = pd.DataFrame(data)
print(df)

high_rated = df[df["Rating"]>4]
print(high_rated)

# Sorting
sorted_df = df.sort_values(by="Price") #ascending
print(sorted_df)
sorted_df = df.sort_values(by="Price",ascending=False)
print(sorted_df)

# Adding new Column
df["Price_USD"]= df["Price"] * 1.25
print(df)

## Average price, rating
print("Average Price: ",df["Price"].mean())
print("Average Rating: ",df["Rating"].mean())
## Filter book which price is less than 30
## Store it into one csv file (to_csv)
under_thirty = df[df["Price"] < 30]
# print("bookes Under 30 rupees: \n ", under_thirty)
under_thirty.to_csv('underthirty.csv', index = False)


