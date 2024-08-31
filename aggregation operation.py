import pandas as pd


ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')


grouped_ratings = ratings_df.groupby('movieId').agg(
    count_ratings=('rating', 'count'),
    mean_rating=('rating', 'mean')
).reset_index()

print(grouped_ratings.head()) 

print("\n")


#inner join

merged_df = pd.merge(movies_df, grouped_ratings, on='movieId', how='inner')

print(merged_df.head())

print("\n")

#filter


filtered_df = merged_df[merged_df['count_ratings'] > 50]

print(filtered_df.head()) 

print("\n")