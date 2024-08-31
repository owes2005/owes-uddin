import pandas as pd


ratings_df = pd.read_csv('ratings.csv')


ratings_count = ratings_df.groupby('movieId')['rating'].count()


max_rated_movie_id = ratings_count.idxmax()
max_ratings = ratings_count.max()


print(f"Movie ID with maximum ratings: {max_rated_movie_id}")
print(f"Number of ratings received: {max_ratings}")


movies_df = pd.read_csv('movies.csv')


max_rated_movie_title = movies_df[movies_df['movieId'] == max_rated_movie_id]['title'].values[0]

print(f"Movie with maximum ratings: {max_rated_movie_title}")