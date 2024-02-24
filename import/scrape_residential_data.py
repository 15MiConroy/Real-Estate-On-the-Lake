import requests

parcelNum = "01A0010000090"

params = {
    "UseSearch": "no",
    "pin": parcelNum,
    "mode": "residential"
}

# Send the POST request
response = requests.post('https://auditor.lakecountyohio.gov/Datalets/Datalet.aspx', params=params)

print(response.status_code)