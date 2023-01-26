# Data pipelining
This project is created as an assignment for the Coderush Apprenticeship. Here, we have scraped https://news.sky.com/ to collect categories and headlines, followed by data manipulation to serve the data to the endpoint.
1. Run scraper.py as: 
>
> python scraper.py 
>
This creates scrapedData.csv<br/>

2. To install node packages run:
>
> npm install
>
This will install all required packages.
>
> node server.js
>
This will start server at port 8585 and the end point to access the data will be
>
>https://localhost:8585/scrapedData
>