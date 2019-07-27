# IMDB-org-scraping-with-python

Scraping IMDB Org with Python and Flask using API key. ScrapeD IMDB website for Names, Rating and cast of atleast 1000 movies.

***Api which is used:*** <br><br>
 `GET: /autocomplete
 given a search input prefix, display movie names that start with prefix, sorted by rating.

 Example:
 prefix = avg
 Response ::
 1. avengers`
 `2. avengers endgame`

 `PARAMETERS:
 prefix : input query [MUST]
 limit : leturn limit number of movie names (default : 5)
 offset : return limit number of movie names starting from offset
position (default : 0)

 GET: /movies/<movie_id>
 given a movie_id return details of the movie like, name, cast and rating`


#####Used production read DB
