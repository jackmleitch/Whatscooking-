import pandas as pd 
import requests
import time
from bs4 import BeautifulSoup
import numpy as np
from JO_scrape_class import JamieOliver

# Reads in the csv containing each recipes url
recipe_df = pd.read_csv("/Users/Jack/Documents/ML/Projects/Whatscooking/input/recipe_urls.csv")
# The list of recipe attributes we want to scrape
attribs = ['recipe_name', 'serves', 'cooking_time', 'difficulty', 'ingredients']

# For each url (i) we add the attribute data to the i-th row
temp = pd.DataFrame(columns=attribs)
for i in range(0,len(recipe_df['recipe_urls'])):
    url = recipe_df['recipe_urls'][i]
    recipe_scraper = JamieOliver(url)
    temp.loc[i] = [getattr(recipe_scraper, attrib)() for attrib in attribs]
    if i % 25 == 0:
        print(f'Step {i} completed')
    time.sleep(np.random.randint(1,5,1))

# Put all the data into the same dataframe
temp['recipe_urls'] = recipe_df['recipe_urls']
columns = ['recipe_urls'] + attribs
temp = temp[columns]

JamieOliver_df = temp

JamieOliver_df.to_csv(r"/Users/Jack/Documents/ML/Projects/Whatscooking-/input/JamieOliver_full.csv", index=False)

