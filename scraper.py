from bs4 import BeautifulSoup
import requests
import re
import csv

#Configure beautiful soup
url="https://news.sky.com/"
htmldocs=requests.get(url).content
soup = BeautifulSoup(htmldocs,'html.parser')

#Create csv ready data
data=[]
container = soup.find_all('div',class_='sdc-site-tile__body-main')
for item in container:
    title = item.find('a',class_='sdc-site-tile__tag-link')
    if title!=None:
        headline = item.find('span',class_='sdc-site-tile__headline-text')
        category=re.sub(r'\s+', '',title.text)
        headline = headline.text
        # print(category,headline)
        a={'category':category,'headline':headline}
        data.append(a)
# print(data)

# Save file to csv for further analysis
with open('scraptedData.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = ['category','headline'])
    writer.writeheader()
    writer.writerows(data)