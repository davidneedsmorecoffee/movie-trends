import omdb
import os
import pandas as pd
import numpy as np
import requests

omdb.set_default('apikey', "your api key")

df = pd.read_csv('movies_2018.csv',encoding='latin-1')
df.columns={"Title"}

# Module for reading CSV files

films = df["Title"]
titles = []
metascore = []
imdb_rating = []
imdb_votes = []
rated = []
runtime = []
released = []
genre = []
box_office = []
year = []

record = 1
notfound = 0
found = 0
total = len(df)
j = 0

for film in films:
    try:
        response = omdb.get(title={film})
        titles.append(response["title"])
        rated.append(response["rated"])
        genre.append(response["genre"])
        
        metascore.append(response["metascore"])
        imdb_rating.append(response["imdb_rating"])
        imdb_votes.append(response["imdb_votes"])
        
        runtime.append(response["runtime"])
        released.append(response["released"])
        year.append(response["year"])

        box_office.append(response["box_office"])
        j += 1
        record += 1
        found += 1
        print(f"Processing Record {j} of {total} | {film}")
    except Exception:
        print(f"Processing Record {j} of {total} | {film} not found - skipping.")
        record += 1
        notfound += 1
        
pct_movie_found = round(found/(notfound+found)*100,1)       
print(f"{pct_movie_found}% of movies found")

# Coverting to a dataframe 

df = pd.DataFrame({'Title': titles, 'Metascore': metascore, 'Rated': rated,'Runtime': runtime,'Released': released, 'Year': year, 'Genre': genre,
                  'imdb_rating': imdb_rating, 'imdb_votes': imdb_votes})
df.to_csv("films.csv", encoding="utf-8", index=False)
