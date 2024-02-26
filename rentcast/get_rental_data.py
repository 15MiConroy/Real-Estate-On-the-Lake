import requests
import os

# Send get request tot rentcast API
headers = {
    'accept': 'application/json',
    'X-Api-Key': os.environ.get('rentcast_api_key'),
}

params = {
    'limit': '500',
    'status': 'active',
    'state': 'OH',
    }
response = requests.get('https://api.rentcast.io/v1/listings/sale', headers=headers, params=params)

if response.status_code == 200:
    #export the response to a json file
    with open('rental_data.json', 'w') as f:
        f.write(response.text)

    print('Data successfully retrieved and saved to rental_data.json')