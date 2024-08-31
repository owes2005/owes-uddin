import pandas as pd


ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

sci_fi_movies = movies_df[movies_df['genres'].str.contains('Sci-Fi')]


grouped_ratings = ratings_df.groupby('movieId').agg(
    count_ratings=('rating', 'count')
).reset_index()


sci_fi_ratings = pd.merge(sci_fi_movies, grouped_ratings, on='movieId', how='inner')

sorted_sci_fi = sci_fi_ratings.sort_values(by='count_ratings', ascending=False)

third_most_popular_sci_fi = sorted_sci_fi.iloc[2] 

print(f"Third most popular Sci-Fi movie based on the number of user ratings:")
print(f"Title: {third_most_popular_sci_fi['title']}")
print(f"Number of Ratings: {third_most_popular_sci_fi['count_ratings']}")