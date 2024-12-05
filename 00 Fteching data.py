'''from bs4 import BeautifulSoup
import requests

try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')
    movies = soup.find("")

except Exception as e:
    print(e)'''











'''
def FetchAndSavetoFile(url ,path ):
    r = requests.get(url)
    with open (path,"w", encoding='utf-8') as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/city/delhi"

FetchAndSavetoFile(url,"data/times.html")
'''
