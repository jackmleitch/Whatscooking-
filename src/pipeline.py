# /Users/Jack/Documents/ML/Projects/Whatscooking-/src
import pandas as pd 
import nltk
import string
import ast
import re
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from ingredient_parser import ingredient_parser

# import our recipe dataset
recipe_df = pd.read_csv("/Users/Jack/Documents/ML/Projects/Whatscooking-/input/df_parsed.csv")

