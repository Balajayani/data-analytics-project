from sqlalchemy import create_engine
import pandas as pd

# Credentials
username = 'Bala'
password = 'Bala19'
database = 'netflix_data'

# Read cleaned dataset
df = pd.read_csv('netflix_cleaned.csv')

# Connect to MySQL
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost/{database}', echo=False)

# Load dataframe to SQL
df.to_sql(name='netflix_shows', con=engine, if_exists='replace', index=False)
