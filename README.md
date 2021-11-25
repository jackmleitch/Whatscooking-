# Recipe Recommendation System 
* Created a tool that recommends recipes based on ingredients inputted to help students eat better food.
* Scraped over 4000 recipes from [All Recipes](allrecipes.com) and [Jamie Oliver](jamieoliver.com) using python and beautiful soup.
* Parsed recipe ingredients and created word embeddings using Word2Vec and TF-IDF.
* Created a recipe recommendation system using cosine similarity to measure Euclidean distance between the word embeddings of recipe ingredients.
* Built a client-facing API using flask, and a user-friendly app with Streamlit.

## Motivation
Cooking is a hobby for some and a major problem for others. However, you can always use a helping hand for cooking. Being a student, it is always a difficult decision to decide what to eat for lunch or dinner. Sometimes faced with limited items in the kitchen, it is always a challenge to decide what to cook for a meal. This inspired me to create a system that can recommend recipes based on ingredient suggestions.

## Code 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, gensim, matplotlib, seaborn, beautifulsoup, flask, streamlit, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**You can run this model yourself using my API:**
```
docker pull jackmleitch/whatscooking:API
docker run -p 5000:5000 -d whatscooking:api
```
## Project write-up
I have three blogs on this project and they can be found here:
* [Data gatherting](https://medium.com/r?url=https%3A%2F%2Fjackmleitch.medium.com%2Fusing-beautifulsoup-to-help-make-beautiful-soups-d2670a1d1d52)
* [Initital Model](https://towardsdatascience.com/building-a-recipe-recommendation-api-using-scikit-learn-nltk-docker-flask-and-heroku-bfc6c4bdd2d4)
* [Updated Model](https://towardsdatascience.com/building-a-recipe-recommendation-system-297c229dda7b)

<p align="center">
<img src="./input/flowchart.png" width="700" height="477">
</p>

## Web Scraping
Built a web scraper using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to scrape over 4000 food recipes from [All Recipes](allrecipes.com) and [Jamie Oliver](jamieoliver.com). With each recipe, I got the following:

* Recipe name 
* Ingredients
* URL
* Rating

## Data Cleaning

After scraping the data, we needed to parse the ingredients to remove redundant information that would not help distinguish recipes. The ingredient parser does the following:
* Lemmatize words to ensure we remove all versions of words, e.g. both pounds and pound
* Removed stopwords 
* Removed cooking measures, e.g. pounds and lbs
* Removed common household items such as oil and butter 
 
## Model Building

## Productionization
