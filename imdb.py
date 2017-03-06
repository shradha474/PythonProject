
#import urllib.request
import sys
import requests
from bs4 import BeautifulSoup


weburl1 = "http://www.imdb.com/chart/top-indian-movies"
#while len(weburl1) > 1:
#frm = i
#tu = int(sys.argv[2])
url = weburl1 
req =  requests.get(url)
ab = req.text
soup = BeautifulSoup(ab,"html.parser")
for s in soup.findAll('td',{'class': 'titleColumn'}):
                     b = s.find('a').text
             #txturl = q.get('itemprop')
            # urllib.request.urlretrieve(txturl)
                     print b

