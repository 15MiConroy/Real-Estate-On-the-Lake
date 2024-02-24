from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
from bs4 import BeautifulSoup
import time
import json

service = Service(executable_path='C:/Users/Micha/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service) 

# Go to the website
driver.get('https://auditor.lakecountyohio.gov/search/advancedsearch.aspx?mode=advanced')

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

#Sleep to avoid being blocked
time.sleep(0.5)

# Find the VIEWSTATE and EVENTVALIDATION values
viewstate = soup.find(id="__VIEWSTATE")['value']
eventvalidation = soup.find(id="__EVENTVALIDATION")['value']
viewstategenerator = soup.find(id="__VIEWSTATEGENERATOR")['value']
sortBy = soup.find(id="SortBy")['value']
sortDir = 'asc'
pageSize = "5000"
hdCriteria = "bedrooms|1~99"
hdSearchType = "AdvSearch"
hdCriteriaTypes = "N|N|N|N|C|N|C|C|C|C|C|C|C|D|N|C|N|N|N|C|N|C|C|C|N|C|N|C"
hdLastState = soup.find(id="hdLastState")['value']
hdSelectedQuery = soup.find(id="hdSelectedQuery")['value']
hdCriterias = soup.find(id="hdCriterias")['value']
hdSelectAllChecked = "false"
ctl01dlGroups = "4"
inpDistinct = "on"
ctl01_cal1_dateInput_ClientState = soup.find(id="ctl01_cal1_dateInput_ClientState")['value']
ctl01_cal1_calendar_SD  = soup.find(id="ctl01_cal1_calendar_SD")['value']
ctl01_cal1_calendar_AD = soup.find(id="ctl01_cal1_calendar_AD")['value']
ctl01_cal1_ClientState = soup.find(id="ctl01_cal1_ClientState")['value']
ctl01_cal2_dateInput_ClientState = soup.find(id="ctl01_cal2_dateInput_ClientState")['value']
ctl01_cal2_calendar_SD = soup.find(id="ctl01_cal2_calendar_SD")['value']
ctl01_cal2_calendar_AD = soup.find(id="ctl01_cal2_calendar_AD")['value']
ctl01_cal2_ClientState = soup.find(id="ctl01_cal2_ClientState")['value']
selSortBy = sortBy
selSortDir = 'asc'
selPageSize = pageSize


# Close the browser
driver.quit()

# Define the headers for the POST request
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Origin': 'https://auditor.lakecountyohio.gov',
    'Referer': 'https://auditor.lakecountyohio.gov/search/advancedsearch.aspx?mode=advanced',
    'Host': 'auditor.lakecountyohio.gov',
}

# Define the data for the POST request
data = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    '__EVENTVALIDATION': eventvalidation,
    'SortBy': sortBy,
    'SortDir': sortDir,
    'PageSize': pageSize,
    'hdCriteria': hdCriteria,
    'hdSearchType': hdSearchType,
    'hdCriteriaTypes': hdCriteriaTypes,
    'hdLastState': hdLastState,
    'hdSelectedQuery': hdSelectedQuery,
    'hdCriterias': hdCriterias,
    'hdSelectAllChecked': hdSelectAllChecked,
    'ctl01$dlGroups': ctl01dlGroups,
    'inpDistinct': inpDistinct,
    'ctl01_cal1_dateInput_ClientState': ctl01_cal1_dateInput_ClientState,
    'ctl01_cal1_calendar_SD': ctl01_cal1_calendar_SD,
    'ctl01_cal1_calendar_AD': ctl01_cal1_calendar_AD,
    'ctl01_cal1_ClientState': ctl01_cal1_ClientState,
    'ctl01_cal2_dateInput_ClientState': ctl01_cal2_dateInput_ClientState,
    'ctl01_cal2_calendar_SD': ctl01_cal2_calendar_SD,
    'ctl01_cal2_calendar_AD': ctl01_cal2_calendar_AD,
    'ctl01_cal2_ClientState': ctl01_cal2_ClientState,
    'selSortBy': selSortBy,
    'selSortDir': selSortDir,
    'selPageSize': selPageSize,
}

params = {
    'mode': 'advanced'
    }

# Send the POST request
response = requests.post('https://auditor.lakecountyohio.gov/search/advancedsearch.aspx', headers=headers, params=params, data=data)

# Print the response status code
print(response.status_code)

# Parse the response with BeautifulSoup
response_soup = BeautifulSoup(response.text, 'html.parser')

parcel_dict = {}
# Get the parcel numbers
for parcel in response_soup.findAll('input', {'id':'chkPin'}):
    parcel_number = parcel.get('value').split(':')[1]
    parcel_dict[parcel_number] = 'https://auditor.lakecountyohio.gov/Datalets/Datalet.aspx?UseSearch=no&pin=' + parcel_number

# Write the parcel numbers to a file
with open('parcels.json', 'w') as f:
    #dump the dictionary to a json file'
    json.dump(parcel_dict, f)