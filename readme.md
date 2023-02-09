# Data pipelining
This project was created as an assignment for the Coderush Apprenticeship. Here, we have scraped https://thehimalayantimes.com/ to collect headline, body, category and time_published followed by data manipulation to serve the data to the endpoint.

The Project is a group project and the Members of the group are:<br/>
-Abhinandhan Shrestha
-Anushil Timsina
-Santosh Dangal

1. Run scraper.py as: 
>
> python scraper.py 
>
This creates scrapedData.csv inside category folder. This csv file is preprocessed and visualized using preprocessing.ipynb to create the following categories:<br/>
- Art&Culture
- Business
- Entertainment
- Environment
- Health
- Lifestyle
- Mobile&Apps
- Nepal
- Opinion
- preprocessedData
- ScienceandTech
- TravelAbroad
- World

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
> "https://localhost:8585/" followed by category name as URI. 
>
For example:
> http://localhost:8585/Art&Culture
>
> http://localhost:8585/Business
>
> and so on for every category
>
If we want raw scraped data then it is accessible at:
>
> http://localhost:8585/scrapedData
>
Also, if we want preprocessed entire data then it is accessible at:
>
> http://localhost:8585/preprocessedData
>
