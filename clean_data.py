import pandas as pd

# Load dataset
df = pd.read_csv('netflix_titles.csv')

# Basic cleaning
df.dropna(subset=['title'], inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Fill missing values
df['country'].fillna('Unknown', inplace=True)

# Save cleaned version
df.to_csv('netflix_cleaned.csv', index=False)
