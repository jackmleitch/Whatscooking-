# /Users/Jack/Documents/ML/Projects/Whatscooking-/src

import pandas as pd 
import nltk
import string
import ast
import re
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# import our recipe dataset
recipe_df = pd.read_csv("/Users/Jack/Documents/ML/Projects/Whatscooking-/input/JamieOliver_full.csv")

# columns in our recipe dataset 
columns = list(recipe_df.columns)

# Weigths and measures are words that will not add value to the model. I got these standard words from 
# https://en.wikibooks.org/wiki/Cookbook:Units_of_measurement

volume = ['teaspoon', 't', 'tsp.', 'tablespoon', 'T', 'tbl.', 'tbs', 'tbsp.', 'fluid ounce', 
          'fl oz', 'gill', 'cup', 'c', 'pint', 'p', 'pt', 'fl pt', 'quart', 'q', 'qt', 'fl qt',
          'gallon', 'g', 'gal', 'ml', 'milliliter', 'millilitre', 'cc', 'mL', 'l', 'liter', 'litre',
          'L', 'dl', 'deciliter', 'decilitre', 'dL', 'bulb', 'level', 'heaped', 'rounded', 'whole']

mass = ['pound', 'lb', '#', 'ounce', 'oz', 'mg', 'milligram', 'milligramme', 'g', 'gram', 'gramme',
        'kg', 'kilogram', 'kilogramme', 'x', 'of']

length = ['mm', 'millimetre', 'millimeter', 'cm', 'centimeter', 'centimetre', 'm', 'meter', 'metre',
          'inch', 'in']

prefix = ['milli', 'centi', 'deci', 'hecto', 'kilo']

measures = volume + mass + length + prefix

# We lemmatize the words to reduce them to their smallest form (lemmas). 
lemmatizer = WordNetLemmatizer()
measures = [lemmatizer.lemmatize(m) for m in measures]

# The ingredient list is now a string so we need to turn it back into a list. We use ast.literal_eval
ingreds = recipe_df['ingredients'][0]
# ingreds = ast.literal_eval(ingreds)
print(ingreds)



def ingredient_parser(ingreds):
    '''
    
    This function takes in a list (but it is a string as it comes from pandas dataframe) of 
       ingredients and performs some preprocessing. 
       For example:

       input = '['1 x 1.6kg whole duck', '2 heaped teaspoons Chinese five-spice powder', '1 clementine',
                 '6 fresh bay leaves', 'GRAVY', '', '1 bulb of garlic', '2 carrots', '2 red onions', 
                 '3 tablespoons plain flour', '100 ml Marsala', '1 litre organic chicken stock']'
       
       output = ['duck', 'chinese five spice powder', 'clementine', 'fresh bay leaf', 'gravy', 'garlic',
                 'carrot', 'red onion', 'plain flour', 'marsala', 'organic chicken stock']

    '''

    # The ingredient list is now a string so we need to turn it back into a list. We use ast.literal_eval
    ingredients = ast.literal_eval(ingreds)
    # We first get rid of all the punctuation. We make use of str.maketrans. It takes three input 
    # arguments 'x', 'y', 'z'. 'x' and 'y' must be equal-length strings and characters in 'x'
    # are replaced by characters in 'y'. 'z' is a string (string.punctuation here) where each character
    #  in the string is mapped to None. 
    translator = str.maketrans('', '', string.punctuation)

    ingred_list = []
    for i in ingredients:
        i.translate(translator)
        # We split up with hyphens as well as spaces
        items = re.split(' |-', i)
        # Get rid of words containing non alphabet letters
        items = [word for word in items if word.isalpha()]
        # Turn everything to lowercase
        items = [word.lower() for word in items]
        # Lemmatize words so we can compare words to measuring words
        items = [lemmatizer.lemmatize(word) for word in items]
        # Gets rid of measuring words/phrases, e.g. heaped teaspoon
        items = [word for word in items if word not in measures]
        if items:
            ingred_list.append(' '.join(items)) 
    return ingred_list

new = ingredient_parser(ingreds)

# bigram = list(nltk.bigrams(new))
# print(bigram)