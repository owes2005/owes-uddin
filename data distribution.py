import pandas as pd
import matplotlib.pyplot as plt


ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

fight_club_movie_id = movies_df[movies_df['title'] == 'Fight Club (1999)']['movieId'].values[0]


fight_club_ratings = ratings_df[ratings_df['movieId'] == fight_club_movie_id]

plt.figure(figsize=(8, 6))
plt.hist(fight_club_ratings['rating'], bins=10, edgecolor='black')
plt.title('Distribution of User Ratings for "Fight Club (1999)"')
plt.xlabel('Rating')
plt.ylabel('Number of Ratings')
plt.xticks(range(1, 6)) 
plt.grid(True)
plt.show()