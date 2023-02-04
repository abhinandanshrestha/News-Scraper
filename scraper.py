from bs4 import BeautifulSoup
import requests
import re
import csv
import time

def scrape(soup):
    """
    Scrapes a page from the given url

    Parameters:
    soup (html): The url to be scraped.

    Returns:
    A dictionary with headlines, body, location and time_published.
    """

    container = soup.find_all('article',class_='row animate-box fadeInUp animated-fast')
    for item in container:
        headline = item.find('h3',class_='alith_post_title HideMobile').text
        body =  item.find('div',class_='alith_post_except HideMobile fontsize14height40').text
        body=re.sub(r"^\s+|\s+$", "", body)
        location = item.find('span',class_="section").text
        time_published =  item.find('span', class_="meta_date").text
        a={'headline':headline,'body':body,'location':location,'time_published':time_published}
        return a
        # data.append(a)  
    
    # print("Scraped page"+str(j)+" from url "+str(i))
    time.sleep(1)

# Save file to csv for further analysis
def csvExport(data):
    """
    Exports list of dictionary into csv

    Parameters:
    data (list of dictionary): data that has to be exported into a csv.

    Returns:
    Nothing.
    """

    with open('category/scrapedData.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = ['headline','body','location','time_published'])
        writer.writeheader()
        writer.writerows(data)


def driver(category):
    """
    A driver for scraping all the pages from the url of a category also after scraping is done,
        this function calls csvExport(data: list of dictionary)

    Parameters:
    category (list): categories to scrape from the url.

    Returns:
    Nothing.
    """
    data=[]
    
    #Configure beautiful soup
    for i in range(len(category)):
        for j in range(1,31):
            
            url="https://thehimalayantimes.com/morearticles/"+category[i]+"?pgno="+str(j)
            htmldocs=requests.get(url).content
            soup = BeautifulSoup(htmldocs,'html.parser')

            #Create csv ready data by scraping and converting into dictionary
            a=scrape(soup)
            data.append(a)
            print("Scraped page"+str(j)+" from url "+str(i))

    csvExport(data)

if __name__=='__main__':
    category=['Nepal','World','Opinion','Business','Entertainment','Lifestyle','Science%20and%20Tech','Health']
    driver(category)