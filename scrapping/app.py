import requests
from bs4 import BeautifulSoup

count = 1
per_page = 250
base_url = "https://www.imdb.com/search/title/?genres=sci-fi&count=250&start="
server_url = "http://127.0.0.1:5000/add"
number_of_movies = 1000

status = True

for page in range(5):
    if status:
        response = requests.get(f"{base_url}{count}")
        soup = BeautifulSoup(response.text, "html.parser")
        movies = soup.select(".lister-item.mode-advanced")
        for movie in movies:
            try:
                name = movie.select(".lister-item-header>a")[0].get_text()
                rating = movie.select(".inline-block.ratings-imdb-rating>strong")[0].get_text()
                data = {'name':name, 'rating': rating }
                r = requests.post(url = server_url, data = data )
                number_of_movies -= 1
            except:
                print(number_of_movies)
                
            if number_of_movies < 1:
                status = False
                break
                print("Download Completed")
        count = count + per_page


