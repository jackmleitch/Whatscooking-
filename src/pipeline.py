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

if __name__=='__main__':
    # import our recipe dataset
    recipe_df = pd.read_csv("/Users/Jack/Documents/ML/Projects/Whatscooking-/input/df_parsed.csv")
    # TF-IDF feature extractor 
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf = TfidfVectorizer()
    tfidf_recipe = tfidf.fit_transform(recipe_df['ingredients'])

    # Count vectorizer feature extractor 
    from sklearn.feature_extraction.text import CountVectorizer
    count_vec = CountVectorizer()
    count_recipe = count_vec.fit_transform(recipe_df['ingredients'])

    # Recommender system 
    from sklearn.metrics.pairwise import cosine_similarity
    test_ingredients = ['cheese', 'milk', 'butter', 'pasta', 'bacon', 'tomato']
    test_ingredients_parsed = ingredient_parser(test_ingredients)

    test_ingredients_tfidf = tfidf.transform([test_ingredients_parsed])
    test_ingredients_count = count_vec.transform([test_ingredients_parsed])

    cos_sim_tfidf = map(lambda x: cosine_similarity(test_ingredients_tfidf, x), tfidf_recipe)
    scores_tfidf= list(cos_sim_tfidf)

    cos_sim_count = map(lambda x: cosine_similarity(test_ingredients_count, x), tfidf_recipe)
    scores_count = list(cos_sim_count)
    
    #  Top-N recomendations order by score
    def get_recommendation(top, recipe_df, scores):
        recommendation = pd.DataFrame(columns = ['recipes', 'ingredients', 'score'])
        count = 0
        for i in top:
            recommendation.at[count, 'recipes'] = recipe_df['recipe_name'][i]
            recommendation.at[count, 'ingredients'] = recipe_df['ingredients'][i]
            recommendation.at[count, 'score'] =  scores[count]
            count += 1
        return recommendation

    top = sorted(range(len(scores_tfidf)), key=lambda i: scores_tfidf[i], reverse=True)[:10]
    print(top)
    # list_scores_tfidf = [scores_tfidf[i][0][0] for i in top]
    # test = get_recommendation(top, recipe_df, list_scores_tfidf)
    # print(test)

    # top = sorted(range(len(scores_count)), key=lambda i: scores_count[i], reverse=True)[:10]
    # list_scores_count = [scores_count[i][0][0] for i in top]
    # test = get_recommendation(top, recipe_df, list_scores_count)
    # print(test)
    