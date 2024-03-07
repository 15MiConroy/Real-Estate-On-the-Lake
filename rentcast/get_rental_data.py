import requests
import os
import datetime
import json

# Send get request tot rentcast API
headers = {
    'accept': 'application/json',
    'X-Api-Key': os.environ.get('rentcast_api_key'),
}

# params = {
#     'limit': '500',
#     'status': 'active',
#     'state': 'OH',
#     'city': 'Willoughby',
#     'city': 'Mentor',
#     'city': 'Willoughby Hills',
#     'city': 'Eastlake',
#     }
response = requests.get('https://api.rentcast.io/v1/listings/sale?limit=500&status=active&state=OH&city=Willoughby&city=Mentor', headers=headers)

if response.status_code == 200:
    #export the response to a json file
    #set the filename to include the current date and time
    filename = 'rental_data' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.json'
    with open(filename, 'w') as f:
        f.write(response.text)

    print('Data successfully retrieved and saved to rental_data.json')