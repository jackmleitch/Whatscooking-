import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np
import re

headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

class JamieOliver():
    """ This class will output the recipe details. Recipes have the
    following properties:

    Attributes:
        url: The url of the recipe on Jamie Oliver site.

    Methods:
        Ingredients: Recipe ingredients.
        Cooking time: What it says on the tin.
        Difficulty: Recipe difficulty.
        Serves: How many people the recipe serves.
    """
    def __init__(self, url):
        self.url = url 
        self.soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
    
    def recipe_name(self):
        """ Locates the recipe title """
        # Some of the urls are not recipe urls so to avoid errors we use try/except 
        try:
            return self.soup.find('h1').text.strip()
          # return self.soup.select('ht.hidden-xs')[0].text.strip()
        except: 
            return np.nan
        
    def serves(self):
        """ Locates the number of people the meal serves """
        try:
            return self.soup.find('div', {'class': 'recipe-detail serves'}).text.split(' ',1)[1]
        except:
            return np.nan 

    def cooking_time(self):
        """ Locates the cooking time (in mins or hours and mins) """
        try:
            return self.soup.find('div', {'class': 'recipe-detail time'}).text.split('In')[1]
        except:
            return np.nan


    def difficulty(self):
        """ Locates the cooking difficulty """
        try:
            return self.soup.find('div', {'class': 'col-md-12 recipe-details-col remove-left-col-padding-md'}).text.split('Difficulty')[1]
        except:
            return np.nan

    def ingredients(self):
        """ Creating a vector containing the ingredients of the recipe """
        try:
            ingredients = [] 
            for li in self.soup.select('.ingred-list li'):
                ingred = ' '.join(li.text.split())
                ingredients.append(ingred)
            return ingredients
        except:
            return np.nan


