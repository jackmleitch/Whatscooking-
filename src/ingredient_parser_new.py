import pandas as pd 
import nltk
import string
import ast
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from collections import Counter

# def ingredient_parser(ingreds):
#     '''
    
#     This function takes in a list (but it is a string as it comes from pandas dataframe) of 
#        ingredients and performs some preprocessing. 
#        For example:

#        input = ['1 x 1.6kg whole duck', '2 heaped teaspoons Chinese five-spice powder', '1 clementine',
#                  '6 fresh bay leaves', 'GRAVY', '', '1 bulb of garlic', '2 carrots', '2 red onions', 
#                  '3 tablespoons plain flour', '100 ml Marsala', '1 litre organic chicken stock']
       
#        output = ['duck', 'chinese five spice powder', 'clementine', 'fresh bay leaf', 'gravy', 'garlic',
#                  'carrot', 'red onion', 'plain flour', 'marsala', 'organic chicken stock']

#     '''
#     if isinstance(ingreds, list):
#         ingredients = ingreds
#     else:
#         ingredients = ast.literal_eval(ingreds)
    
input = ['1 x 1.6kg whole duck', '2 heaped teaspoons Chinese five-spice powder', '1 clementine', 
        '6 fresh bay leaves', 'GRAVY', '', '1 bulb of garlic', '2 carrots', '2 red onions', 
        '3 tablespoons plain flour', '100 ml Marsala', '1 litre organic chicken stock']
test = nltk.word_tokenize(input[1])
print(test)

