# %%

# Analysing Hacker News Posts - A Guided Project by Data Quest*

# We will be analyzing a csv export from Hacker News posts to determine which type of posts receive more attention and comments.

import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

FOLDER_PATH = os.getenv('FOLDER_PATH')


# Reading / importing the csv
hn = pd.read_csv(f'{FOLDER_PATH}hacker_news.csv')

# Displaying the first 5 rows to verify headers, type of data, etc.
hn.head(5)

# %%
