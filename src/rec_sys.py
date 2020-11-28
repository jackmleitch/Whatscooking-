import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  
from ingredient_parser import ingredient_parser
import pickle

# Top-N recomendations order by score
def get_recommendations(N, scores):
    # load in recipe dataset 
    df_recipes = pd.read_csv("../input/df_recipes.csv")
    # order the scores with and filter to get the highest N scores
    top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:N]
    # create dataframe to load in recommendations 
    recommendation = pd.DataFrame(columns = ['recipe', 'ingredients', 'score', 'url'])
    count = 0
    for i in top:
        recommendation.at[count, 'recipe'] = df_recipes['recipe_name'][i]
        recommendation.at[count, 'ingredients'] = df_recipes['ingredients'][i]
        recommendation.at[count, 'url'] = df_recipes['recipe_urls'][i]
        recommendation.at[count, 'score'] = scores[i]
        count += 1
    return recommendation

def RecSys(ingredients, N=5):
    """
    The reccomendation system takes in a list of ingredients and returns a list of top 5 
    recipes based of of cosine similarity. 
    :param ingredients: a list of ingredients
    :param N: the number of reccomendations returned 
    :return: top 5 reccomendations for cooking recipes
    """

    # load in tdidf model and encodings 
    with open("../input/tfidf_encodings.pkl", 'rb') as f:
        tfidf_encodings = pickle.load(f)

    with open("../models/tfidf.pkl", "rb") as f:
        tfidf = pickle.load(f)

    # parse the ingredients using my ingredient_parser 
    try: 
        ingredients_parsed = ingredient_parser(ingredients)
    except:
        ingredients_parsed = ingredient_parser([ingredients])
    
    # use our pretrained tfidf model to encode our input ingredients
    ingredients_tfidf = tfidf.transform([ingredients_parsed])

    # calculate cosine similarity between actual recipe ingreds and test ingreds
    cos_sim = map(lambda x: cosine_similarity(ingredients_tfidf, x), tfidf_encodings)
    scores = list(cos_sim)

    # Filter top N recommendations 
    recommendations = get_recommendations(N, scores)

    return recommendations

if __name__ == "__main__":
    # test ingredients
    test_ingredients = "tomato hummus lettuce turkey tortilla bagel"
    recs = RecSys(test_ingredients)
    print(recs)