from bs4 import BeautifulSoup
import requests
import re
import csv
import time

data=[]
base_url=['https://thehimalayantimes.com/morearticles/Nepal?pgno=','https://thehimalayantimes.com/morearticles/World?pgno=','https://thehimalayantimes.com/morearticles/Opinion?pgno=','https://thehimalayantimes.com/morearticles/Business?pgno=','https://thehimalayantimes.com/morearticles/Entertainment?pgno=','https://thehimalayantimes.com/morearticles/Lifestyle?pgno=','https://thehimalayantimes.com/morearticles/Science%20and%20Tech?pgno=','https://thehimalayantimes.com/morearticles/Health?pgno=']

#Configure beautiful soup
for i in range(len(base_url)):
    for j in range(1,31):
        url=base_url[i]+str(j)
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
        time.sleep(5)

# Save file to csv for further analysis
with open('category/scrapedData.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = ['headline','body','location','time_published'])
    writer.writeheader()
    writer.writerows(data)