import urllib.request 
from bs4 import BeautifulSoup

class Scraper: 
    def __init__(self, site):
        self.site = site 
    
    def Scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        with open("article_output.txt", "w") as f: 
            for tag in soup.find_all('a'):
                url = tag.get('href')
                if url and 'html' in url: 
                    print("\n" + url)
                    f.write(url + "\n")

# example 
Scraper('https://news.google.com/').scrape()