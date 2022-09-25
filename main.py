from bs4 import BeautifulSoup
import requests
import pandas as pd

upperframe=[]
req = requests.get("https://www.politifact.com/factchecks/list/")
soup = BeautifulSoup(req.content,'html.parser')
print(soup)
frame = []
links = soup.find_all('li',class_ ='o-listicle__item')
filename = "news.csv"
f=open(filename,"w",encoding = 'utf-8')
headers = "Statement,Link,Date,Source,Label\n"
f.write(headers)

for link in links:
    Statement = link.find("div",class_ = 'm-statement__quote').text.strip()
    Link = "https://www.politifact.com"
    Link += link.find("div",class_ = 'm-statement__quote').find('a')['href'].strip()
    Date = link.find("div",class_ = 'm-statement__body').find('a').text.strip()
    Source = link.find("div",class_ = 'm-statement__meta').find('a').text.strip()
    Label = link.find("div",class_ = 'm-statement__content').find("img",class_ = 'c-image__original').get('alt').strip()
    frame.append((Statement,Link,Date,Source,Label))
    f.write(Statement.replace(",","^")+","+Link+","+Date.replace(",","^")+","+Label.replace(",","^")+"\n")
    upperframe.extend(frame)
f.close()
data=pd.DataFrame(upperframe, columns=['Statement','Link','Date','Source','Label'])
data.head()

