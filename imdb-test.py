from bs4 import BeautifulSoup
import requests
import sys
import re
from StringIO import StringIO

try:
    import cPickle as pickle
except:
    import pickle

def download_subtitle(url):
    page = requests.get(url).text
    regex = '/en/subtitleserve/sub/[0-9]+"'
    pattern = re.compile(regex)
    matches = pattern.findall(page)
    download_link = 'www.opensubtitles.org'+matches[0].replace('"','')
    print download_link
    return download_link
   
url = 'http://www.imdb.com/chart/top'

response = requests.get(url)
soup = BeautifulSoup(response.text)

movies = soup.select('td.titleColumn')

links = [each.attrs.get('href') for each in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.titleColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []

print(len(movies))
pattern = re.compile('tt.*/')
for index in range(0, len(movies)):

    matches = pattern.findall(links[index])
    movie_id = matches[0].replace("/","").replace("tt","")
    #print movie_id
    movie_name = movies[index].get_text()
    pattern1 = re.compile('.\n.*\n')
    matches1 = pattern1.findall(movie_name)
    movie_name = matches1[0].replace(".\n","").replace("\n","")
    data = {"movie_name": movie_name,
            "movie_id": movie_id}
            #"starCast": crew[index],
            #"rating": ratings[index],
            #"vote": votes[index]}
    imdb.append(data)

for each in imdb:
    movie_name = each['movie_name'].replace(" ","+")
    movie_id = each['movie_id']
    url = "http://www.opensubtitles.org/en/search/imdbid-"+movie_id+"/sublanguageid-eng/moviename-"+movie_name
    subtitle_url = download_subtitle(url)
    each['subtitle_url']=subtitle_url


print(imdb)
