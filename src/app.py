from flask import Flask, jsonify, request, render_template
from flask_jsonpify import jsonpify
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  
from ingredient_parser import ingredient_parser
import pickle
import config 
import rec_sys

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    return HELLO_HTML

HELLO_HTML = """
     <html><body>
         <h1>Welcome to my api: Whatscooking!</h1>
         <p>Please add some ingredients to the url to receive recipe recommendations.
            You can do this by appending "/recipe?ingredients= Pasta Tomato ..." to the current url.
         <br>Click <a href="/recipe?ingredients= pasta tomato onion">here</a> for an example.
     </body></html>
     """

@app.route('/recipe', methods=["GET"])
def recommend_recipe():
    ingredients = request.args.get('ingredients')   
    recipe = rec_sys.RecSys(ingredients)
    
    response = {}
    count = 0
    for index, row in recipe.iterrows():
        response[count] = {
            'recipe': str(row['recipe']),
            'score': str(row['score']),
            'ingredients': str(row['ingredients']),
            'url': str(row['url'])
        }
        count += 1
    return jsonify(response)
   

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

# http://127.0.0.1:5000/recipe?ingredients=pasta