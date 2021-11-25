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

![alt text](./input/flowchart.png)
<img src="./input/flowchart.png" width="100" height="100">

## Web Scraping
Built a web scraper using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to scrape over 4000 food recipes from [All Recipes](allrecipes.com) and [Jamie Oliver](jamieoliver.com). With each recipe, I got the following:

* Recipe name 
* Ingredients
* URL
* Rating

## Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for my model. I made the following changes before creating word embeddings:

Parsed numeric data out of salary
Made columns for employer provided salary and hourly wages
Removed rows without salary
Parsed rating out of company text
Made a new column for company state
Added a column for if the job was at the company’s headquarters
Transformed founded date into age of company
Made columns for if different skills were listed in the job description:
Python
R
Excel
AWS
Spark
Column for simplified job title and Seniority
Column for description length

## EDA

## Model Building

## Productionization
