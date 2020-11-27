import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  
from ingredient_parser import ingredient_parser
import pickle

# load in recipe dataset 
df_recipes = pd.read_csv("../input/df_recipes.csv")

# load in tdidf model and encodings 
with open("../input/tfidf_encodings.pkl", 'rb') as f:
    tfidf_encodings = pickle.load(f)

with open("../models/tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)

# test ingredients 
test_ingredients = ['tomato', 'hummus', 'lettuce', 'turkey', 'tortilla', 'bagel']
# parse the test ingredients 
test_ingredients_parsed = ingredient_parser(test_ingredients)
# transform the ingredients 
test_ingredients_tfidf = tfidf.transform([test_ingredients_parsed])
# calculate cosine similarity between actual recipe ingreds and test ingreds
cos_sim = map(lambda x: cosine_similarity(test_ingredients_tfidf, x), tfidf_encodings)
scores = list(cos_sim)

# Top-N recomendations order by score
def get_recommendation(N, df_recipes, scores):
    # order the scores with and filter to get the highest N scores
    top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:N]
    print(top)
    # create dataframe to load in recommendations 
    recommendation = pd.DataFrame(columns = ['recipes', 'ingredients', 'score'])
    count = 0
    for i in top:
        recommendation.at[count, 'recipes'] = df_recipes['recipe_name'][i]
        recommendation.at[count, 'ingredients'] = df_recipes['ingredients'][i]
        recommendation.at[count, 'score'] =  scores[i]
        count += 1
    return recommendation

test = get_recommendation(10, df_recipes, scores)
print(test)
