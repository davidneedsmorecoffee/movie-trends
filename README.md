# Movie Trend Analysis

* Please see below for the analyses performed and the files used and/or generated
* Please note that there are multiple notebooks for the different analyses
* See file *movie_trends__ar_dl_nm_rh.pptx* for the powerpoint presentation

## **API CALL + CLEAN UP**
### File with list of movies used for the API call
* *movies_1999_2019_singletable_ut8.csv*
* The list of movies in the above file was scraped from https://en.wikipedia.org/wiki/List_of_American_films_of_####, where the #### represents the year of the movie. Movies from listed from 1999-2019 were obtained.

### API call and export CSV
* Code used: api_to_CSV.ipynb
* the file generated is *All_Movies_1999_2019.csv*

### CSV clean up
* Code used: *CSV_Cleanup.ipynb*
* filter to focus on movies released on or after 2000
* also filter to obtain movies that had more complete dataset
* the file generated is *All_Movies_Working.csv*


## **ANALYSIS**

### Run-time related analyses
* Code used: *Runtime_Review.ipynb*

### Season-related analyses
* Code used: *Season_Review.ipynb*

### Genre and census-related analysis
* Code used: *genre_and_census.ipynb* and *Economy_Indicators.csv*
* Images folder: *content_rating_images*
* PoE=Percent of Earning; CR=Content Rating; POM=Percent of Movies 

### Score-related analyses
* Code used: *movie_score_analysis.ipynb*
* Images folder: *movie_score_images* 
* BO=Box Office; IMDB=Internet Movie Database; RT=Rotten Tomatoes; MC=Metacritic

### Rating-related analyses
* Code used: *Content Rating Analysis.ipynb*
* Images folder: *content_rating_images*
