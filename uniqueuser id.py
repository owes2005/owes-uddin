import pandas as pd


ratings_df = pd.read_csv('ratings.csv')


unique_user_ids = ratings_df['userId'].unique()


print(f"Number of unique user IDs: {len(unique_user_ids)}")
print(unique_user_ids)