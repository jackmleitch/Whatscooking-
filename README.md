## Cooking data science project. 
## Given a list of ingredients, what are different recipes we can make?

Given a list of ingredients, what are different recipes I can make? That is, what recipes can I make with the food I have in my apartment?
 

You can run this model yourself using my API, in your terminal put:
```
docker pull jackmleitch/whatscooking:API

docker run -p 5000:5000 -d whatscooking:api

```

I have two blogs on this project also and they can be found here:

https://medium.com/r?url=https%3A%2F%2Fjackmleitch.medium.com%2Fusing-beautifulsoup-to-help-make-beautiful-soups-d2670a1d1d52

https://towardsdatascience.com/building-a-recipe-recommendation-api-using-scikit-learn-nltk-docker-flask-and-heroku-bfc6c4bdd2d4



In the input folder you will find to csv files:
* df_recipes.csv: A csv file containing 4600 cooking recipes, their ingredients and the corresponding urls. 
* df_parsed.csv: A csv file containing parsed ingredients.

The src folder contains:
* ingredient_parser.py: An ingredient parser to parse recipe ingredients so that they can be encoded. 
* app.py: Flask API 
* rec_sys.py : The recommendation system to recommend recipes based on the users input ingredients. 
* JO_url_scrape.py: Python script to scrape recipe urls from Jamie Oliver website - then saves to recipe_urls.csv
* JO_scrape_class.py: Contains a class built to obtain recipe attributes from JO recipe urls
* JO_full_scrape.py: Here we use JO_scrape_class.py to scrape recipe details from each url in recipe_urls.csv
