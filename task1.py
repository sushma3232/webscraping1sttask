
import requests

from bs4 import BeautifulSoup
sample=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup = BeautifulSoup(sample.content,"html.parser")
Title = soup.title


scraped_movies = soup.find_all('td', class_='titleColumn')

movies=[]
for i in scraped_movies:
    i=i.get_text().replace('\n',"")
    i=i.strip(" ")
    movies.append(i)
a=len(movies)
j=0
while j<a:
    print(movies[j])
    j=j+1