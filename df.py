import omdb
import os
import pandas as pd
import numpy as np
import requests

omdb.set_default('apikey', "your api key")

L99_03 = ['1999','2000','2001','2002','2003']
L04_08 = ['2004','2005','2006','2007','2008']
L09_13 = ['2009','2010','2011','2012','2013']
L14_18 = ['2014','2015','2016','2017','2018']
df = pd.read_excel('project1/movies_1999_2019.xlsx',sheet_name = SUB_IN_LIST_HERE,encoding='latin-1',header = None)
# df[0] will be the first year in the list, [1] the second, etc.

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

notfound = 0
found = 0
total = len(df)
j = 0

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

notfound = 0
found = 0
total = len(df)
j = 0

for film in films:
    try:
        response = omdb.get(title={film})
        box_office.append(response["box_office"])
        titles.append(response["title"])
        rated.append(response["rated"])
        genre.append(response["genre"])
        
        metascore.append(response["metascore"])
        imdb_rating.append(response["imdb_rating"])
        imdb_votes.append(response["imdb_votes"])
        
        runtime.append(response["runtime"])
        released.append(response["released"])
        year.append(response["year"])

        j += 1
        found += 1
        print(f"Processing Record {j} of {total} | {film}")
    except Exception:
        print(f"Processing Record {j} of {total} | {film} not found - skipping.")
        notfound += 1
        
pct_movie_found = round(found/(notfound+found)*100,1)       
print(f"{pct_movie_found}% of movies found")

# Coverting to a dataframe 

df = pd.DataFrame({'Title': titles, 'Metascore': metascore, 'Rated': rated,'Runtime': runtime,'Released': released, 'Year': year, 'Genre': genre,'Box Office': box_office,
                  'imdb_rating': imdb_rating, 'imdb_votes': imdb_votes})
df.to_csv("films.csv", encoding="utf-8", index=False)
