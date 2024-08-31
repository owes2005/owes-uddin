import pandas as pd


ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

grouped_ratings = ratings_df.groupby('movieId').agg(
    count_ratings=('rating', 'count')
).reset_index()


merged_df = pd.merge(movies_df, grouped_ratings, on='movieId', how='inner')

sorted_df = merged_df.sort_values(by='count_ratings', ascending=False)


top_5_movies = sorted_df.head(5)


print(top_5_movies[['title', 'count_ratings']])