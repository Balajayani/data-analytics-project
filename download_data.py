import os
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

# Set your Kaggle API credentials
os.environ['KAGGLE_CONFIG_DIR'] = os.getcwd()

# Initialize API
api = KaggleApi()
api.authenticate()

# Download Netflix dataset
api.dataset_download_file('shivamb/netflix-shows', file_name='netflix_titles.csv', path='.')

# Unzip if needed
with zipfile.ZipFile("netflix_titles.csv.zip", 'r') as zip_ref:
    zip_ref.extractall()
