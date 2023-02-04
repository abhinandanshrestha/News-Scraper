from bs4 import BeautifulSoup
import requests
import re
import csv
import time

data=[]
category=['Nepal','World','Opinion','Business','Entertainment','Lifestyle','Science%20and%20Tech','Health']
# base_url=["https://thehimalayantimes.com/morearticles/"+category+"?pgno=" for category in categories]

#Configure beautiful soup
for i in range(len(category)):
    for j in range(1,31):
        url="https://thehimalayantimes.com/morearticles/"+category[i]+"?pgno="+str(j)
        htmldocs=requests.get(url).content
        soup = BeautifulSoup(htmldocs,'html.parser')

        #Create csv ready data
        container = soup.find_all('article',class_='row animate-box fadeInUp animated-fast')
        for item in container:
            headline = item.find('h3',class_='alith_post_title HideMobile').text
            body =  item.find('div',class_='alith_post_except HideMobile fontsize14height40').text
            body=re.sub(r"^\s+|\s+$", "", body)
            location = item.find('span',class_="section").text
            time_published =  item.find('span', class_="meta_date").text
            a={'headline':headline,'body':body,'location':location,'time_published':time_published}
            data.append(a)  
        
        print("Scraped page"+str(j)+" from url "+str(i))
        time.sleep(1)

# Save file to csv for further analysis
with open('category/scrapedData.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = ['headline','body','location','time_published'])
    writer.writeheader()
    writer.writerows(data)