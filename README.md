# Real-Estate-On-the-Lake
A project to mine Lake County residential property data.

First step: Mine all residential data from https://auditor.lakecountyohio.gov/

Potential Approaches:
1) Do full search on properties that have more than 1 bathroom
2) Use selenium to loop through all results and collect parcel number and link to details page
3) 

.....

Github Copilot came up with a better solultion!!! I can open the search page through selenium, get the necessary headers and body tags!
Then I can query on 5000 records. I tested all of this using postman and it worked! Max amount of records I can get out is currently 5k. So I will need to find a way to query the rest in a systematic way.

I may or may not have gotten the request to work via python. Need to revisit once I have had some sleep :P