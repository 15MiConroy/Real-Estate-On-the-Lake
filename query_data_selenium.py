from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
from bs4 import BeautifulSoup

service = Service(executable_path='C:/Users/Micha/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service) 

# Go to the website
driver.get('https://auditor.lakecountyohio.gov/search/advancedsearch.aspx?mode=advanced')

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the VIEWSTATE and EVENTVALIDATION values
viewstate = soup.find(id="__VIEWSTATE")['value']
eventvalidation = soup.find(id="__EVENTVALIDATION")['value']
viewstategenerator = soup.find(id="__VIEWSTATEGENERATOR")['value']
sortBy = soup.find(id="SortBy")['value']
sortDir = soup.find(id="SortDir")['value']
pageSize = soup.find(id="PageSize")['value']
hdCriteria = "bedrooms|1~99"
hdSearchType = soup.find(id="hdSearchType")['value']
hdCriteriaType = "AdvSearch"
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
selSortDir = sortDir
selPageSize = pageSize


# Close the browser
driver.quit()

# Define the headers for the POST request
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
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
    'hdCriteriaType': hdCriteriaType,
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

# Send the POST request
response = requests.post('https://auditor.lakecountyohio.gov/search/advancedsearch.aspx?mode=advanced', headers=headers, data=data)

# Print the response
print(response.text)

#write the response to a file
with open('response.txt', 'w') as f:
    f.write(response.text)