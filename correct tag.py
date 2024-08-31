import pandas as pd


tags_df = pd.read_csv('tags.csv')
movies_df = pd.read_csv('movies.csv')


matrix_movie_id = movies_df[movies_df['title'] == 'Matrix, The (1999)']['movieId'].values[0]


matrix_tags = tags_df[tags_df['movieId'] == matrix_movie_id]

unique_tags = matrix_tags['tag'].unique()

print(f"Tags submitted for 'Matrix, The (1999)':")
print(unique_tags)