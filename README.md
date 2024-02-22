# Real-Estate-On-the-Lake
A project to mine Lake County residential property data.

The overall goal of this project is to showcase data science skills:
- Data Mining
- Data Cleansing
- Data Analysis
- Data Visualization
- Data Modeling
- Machine Learning
- etc.

First step: Mine all residential data from https://auditor.lakecountyohio.gov/

Potential Approaches:
1) Do full search on properties that have more than 1 bathroom
2) Use selenium to loop through all results and collect parcel number and link to details page
3) 

.....

Github Copilot came up with a better solultion!!! I can open the search page through selenium, get the necessary headers and body tags!
Then I can query on 5000 records. I tested all of this using postman and it worked! Max amount of records I can get out is currently 5k. So I will need to find a way to query the rest in a systematic way.

I may or may not have gotten the request to work via python. Need to revisit once I have had some sleep :P



EUREEKA! (idk how to spell it). I had 2 eureeka moments.
1) I got the python request to finally work, but then realized each link would be relative to the search.
2) After digging around I found out I CAN use the pacel id to search for the property information!
    - https://auditor.lakecountyohio.gov/Datalets/Datalet.aspx?UseSearch=no&pin=01A0010000090&mode=sales
    Where the 01A001..... is the parcel ID

Potential approach to getting ALL parcel numbers:
- Advanced search allows searching based on year built. Could loop through all years (1800-now)


I also stumbled upon this site that actually has parcel data: https://gis-lakeohgis.opendata.arcgis.com/