## Cooking data science project. 
## Given a list of ingredients, what are different recipes we can make?

In the input folder you will find to csv files:
* recipe_urls.csv: This contains all of the urls for the recipes on the Jamie Oliver website (https://www.jamieoliver.com/)
* JamieOliver_full.csv: For each url in the previous csv, this csv contains recipe ingedients, title, serving size etc etc.

The src folder contains:
* JO_url_scrape.py: Python script to scrape recipe urls from Jamie Oliver website - then saves to recipe_urls.csv
* JO_scrape_class.py: Contains a class built to obtain recipe attributes from JO recipe urls
* JO_full_scrape.py: Here we use JO_scrape_class.py to scrape recipe details from each url in recipe_urls.csv
