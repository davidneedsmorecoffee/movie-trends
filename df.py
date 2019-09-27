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
ratings = []
runtime = []
released = []
genre = []
box_office = []

record = 1
notfound = 0
found = 0
total = len(df)
j = 0

for film in films:
    try:
        response = omdb.get(title={film})
        titles.append(response["title"])
        metascore.append(response["metascore"])
        ratings.append(response["rated"])
        runtime.append(response["runtime"])
        released.append(response["released"])
        genre.append(response["genre"])
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

df = pd.DataFrame({'Title': titles, 'Metascore': metascore, 'Ratings': ratings,'Runtime': runtime,'Released': released, 'Genre': genre})
df.to_csv("films.csv", encoding="utf-8", index=False)
