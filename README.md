# IMDB-org-scraping-with-python

Scraping IMDB Org with Python and Django using API key. ScrapeD IMDB website for Names, Rating and cast of atleast 1000 movies.

***Api which is used:*** <br><br>
 GET: /autocomplete<br>
 given a search input prefix, display movie names that start with prefix, sorted by rating.<br><br>

 Example:<br>
 prefix = avg<br>
 Response ::<br>
 1. avengers<br>
 2. avengers endgame<br>
 ...<br>

 PARAMETERS:<br>
 prefix : input query [MUST]<br>
 limit : leturn limit number of movie names (default : 5)<br>
 offset : return limit number of movie names starting from offset<br>
position (default : 0)<br>
<br>

 GET: /movies/<movie_id><br>
 given a movie_id return details of the movie like, name, cast and rating<br>


***Used production read DB***
