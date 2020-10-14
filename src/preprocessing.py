import pandas as pd 
import nltk
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# import our recipe dataset
recipe_df = pd.read_csv("/Users/Jack/Documents/ML/Projects/Whatscooking-/input/JamieOliver_full.csv")

# columns in our recipe dataset 
columns = list(recipe_df.columns)

ingred = recipe_df['ingredients'][0]

# Weigths and measures are the type of words that will not add value to the model
#https://en.wikipedia.org/wiki/Cooking_weights_and_measures
#https://thebakingpan.com/ingredient-weights-and-measures/

measures=['litrbes','liter','millilitres','mL','grams','g', 'kg','teaspoon','tsp',
 'tablespoon','tbsp','fluid', 'ounce','oz','fl.oz', 'cup','pint','pt','quart','qt',
 'gallon','gal','smidgen','drop','pinch','dash','scruple','dessertspoon','teacup',
 'cup','c','pottle','gill','dram','wineglass','coffeespoon','pound','lb','tbsp',
 'plus','firmly', 'packed','lightly','level','even','rounded','heaping','heaped',
 'sifted','bushel','peck','stick','chopped','sliced','halves', 'shredded','slivered',
 'sliced','whole','paste','whole',' fresh', 'peeled', 'diced','mashed','dried','frozen',
 'fresh','peeled','candied','no', 'pulp','crystallized','canned','crushed','minced',
 'julienned','clove','head', 'small','large','medium']

lemmatizer = WordNetLemmatizer()
measures = [lemmatizer.lemmatize(m) for m in measures]
