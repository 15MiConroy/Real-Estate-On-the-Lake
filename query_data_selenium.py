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
sortDir = 'asc'
pageSize = soup.find(id="PageSize")['value']
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
    'Cookie': 'ASP.NET_SessionId=gb20am4rotcdlconctlrwv5w',
    'Origin': 'https://auditor.lakecountyohio.gov',
    'Pragma': 'no-cache',
    'Referer': 'https://auditor.lakecountyohio.gov/search/advancedsearch.aspx?mode=advanced',
    'Cache-Control': 'no-cache',
    'Host': 'auditor.lakecountyohio.gov',
    'Content-Length': '8103',
    'Connection': 'keep-alive',
    'User-Agent': 'PostmanRuntime/7.22.0',
    'Postman-Token': '7aacde3e-f799-42ce-9917-fd3aa7e54255'
}

# Define the data for the POST request
# data = {
#     '__VIEWSTATE':'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',
#     '__VIEWSTATEGENERATOR': viewstategenerator,
#     '__EVENTVALIDATION': 'tTgT9/CJGpHEWpBdfDgLnKw9imdqWHWBCs60qi0zyzdsrjCb4eI9UsLmPw5+FzOHzMiBXvU+7inYim8IMfmc0StgffQgLT13koz2PM58x0fnccrWq3MqhVGycTa0HMmNFfhfxdVg/SWrbX7nABP7dB4+qhTufyfLXijOemqn9lV/ItDxYZ1j0/7CasRsfZfk/XswUUZ/b7+rMLykNLYSgsLCT4sLcifIa9+ACAaH4HCJ/LQw1D3xpFa1p+hY/VxLT8SboeTWmUq5nRtU4h74sTqeGQ9/I7pCknBLfQa6zW+0Elv7vEFxps/bqKQ2hXd+nW2XaME5kW9PfOu+x3mlvRwaOe6HdqKk8bS2K57WpHNpD5VUrkLphFMJ8NLEW61TIIb1bYMBIqfUkLGCS7wtFlPJRB9bCnag5EqRdXfPb/elGHx9zcF4aiAZXXkgVeA1Rm0tkGSBxwjMnEUBkhZg73KDzNO+yvxRJyxl7L5vZZvKvp+7xIR+XxVnj/9tobtkJwWdGZYUwq4e15alIutEcONdxCfuYu2iK+E7sKgNSXecUMR1XcakT2aMm9PL0/oaFPPGrPFnQbSwU9Ci2/hGlQ==',
#     'SortBy': sortBy,
#     'SortDir': sortDir,
#     'PageSize': pageSize,
#     'hdCriteria': hdCriteria,
#     'hdSearchType': hdSearchType,
#     'hdCriteriaTypes': hdCriteriaTypes,
#     'hdLastState': hdLastState,
#     'hdSelectedQuery': hdSelectedQuery,
#     'hdCriterias': hdCriterias,
#     'hdSelectAllChecked': hdSelectAllChecked,
#     'ctl01$dlGroups': ctl01dlGroups,
#     'inpDistinct': inpDistinct,
#     'ctl01_cal1_dateInput_ClientState': ctl01_cal1_dateInput_ClientState,
#     'ctl01_cal1_calendar_SD': ctl01_cal1_calendar_SD,
#     'ctl01_cal1_calendar_AD': ctl01_cal1_calendar_AD,
#     'ctl01_cal1_ClientState': ctl01_cal1_ClientState,
#     'ctl01_cal2_dateInput_ClientState': ctl01_cal2_dateInput_ClientState,
#     'ctl01_cal2_calendar_SD': ctl01_cal2_calendar_SD,
#     'ctl01_cal2_calendar_AD': ctl01_cal2_calendar_AD,
#     'ctl01_cal2_ClientState': ctl01_cal2_ClientState,
#     'selSortBy': selSortBy,
#     'selSortDir': selSortDir,
#     'selPageSize': selPageSize,
# }

data = {
    "__VIEWSTATE": "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",
    "__VIEWSTATEGENERATOR":"81E50120",
    "__EVENTVALIDATION": "tTgT9/CJGpHEWpBdfDgLnKw9imdqWHWBCs60qi0zyzdsrjCb4eI9UsLmPw5+FzOHzMiBXvU+7inYim8IMfmc0StgffQgLT13koz2PM58x0fnccrWq3MqhVGycTa0HMmNFfhfxdVg/SWrbX7nABP7dB4+qhTufyfLXijOemqn9lV/ItDxYZ1j0/7CasRsfZfk/XswUUZ/b7+rMLykNLYSgsLCT4sLcifIa9+ACAaH4HCJ/LQw1D3xpFa1p+hY/VxLT8SboeTWmUq5nRtU4h74sTqeGQ9/I7pCknBLfQa6zW+0Elv7vEFxps/bqKQ2hXd+nW2XaME5kW9PfOu+x3mlvRwaOe6HdqKk8bS2K57WpHNpD5VUrkLphFMJ8NLEW61TIIb1bYMBIqfUkLGCS7wtFlPJRB9bCnag5EqRdXfPb/elGHx9zcF4aiAZXXkgVeA1Rm0tkGSBxwjMnEUBkhZg73KDzNO+yvxRJyxl7L5vZZvKvp+7xIR+XxVnj/9tobtkJwWdGZYUwq4e15alIutEcONdxCfuYu2iK+E7sKgNSXecUMR1XcakT2aMm9PL0/oaFPPGrPFnQbSwU9Ci2/hGlQ==",
    "SortBy": "PARID",
    "SortDir": "asc",
    "PageSize": "5002",
    "hdCriteria": "bedrooms|1~99",
    "hdSearchType": "AdvSearch",
    "hdCriteriaTypes": "N|N|N|N|C|N|C|C|C|C|C|C|C|D|N|C|N|N|N|C|N|C|C|C|N|C|N|C",
    "hdLastState":"1",
    "hdSelectedQuery":"0",
    "hdCriterias":"acres|aprval|bathrooms|bedrooms|comm_building|comm_card|class|luc|Legal|nbhd|owner|parid|projno|salesdate|salesprice|val01|sfla|sqfeetcomm|stories|adrstr|adrno|taxdist|val02|transno|comm_units|yrblt|yrblt_comm|zip",
    "hdSelectAllChecked":"false",
    "ctl01$dlGroups":"4",
    "inpDistinct":"on",
    "ctl01_cal1_dateInput_ClientState":'{"enabled":true,"emptyMessage":"","validationText":"","valueAsString":"","minDateStr":"1900-01-01-00-00-00","maxDateStr":"2099-12-31-00-00-00","lastSetTextBoxValue":""}',
    "ctl01_cal1_calendar_SD":"[]",
    "ctl01_cal1_calendar_AD":'[[1900,1,1],[2099,12,30],[2024,2,21]]',
    "ctl01_cal1_ClientState":'{"minDateStr":"1900-01-01-00-00-00","maxDateStr":"2099-12-31-00-00-00"}',
    "ctl01_cal2_dateInput_ClientState":'{"enabled":true,"emptyMessage":"","validationText":"","valueAsString":"","minDateStr":"1900-01-01-00-00-00","maxDateStr":"2099-12-31-00-00-00","lastSetTextBoxValue":""}',
    "ctl01_cal2_calendar_SD":'[]',
    "ctl01_cal2_calendar_AD":'[[1900,1,1],[2099,12,30],[2024,2,21]]',
    "ctl01_cal2_ClientState":'{"minDateStr":"1900-01-01-00-00-00","maxDateStr":"2099-12-31-00-00-00"}',
    "selSortBy":"PARID",
    "selSortDir":"asc",
    "selPageSize":"15"
}

params = {
    'mode': 'advanced'
    }

# Send the POST request
response = requests.post('https://auditor.lakecountyohio.gov/search/advancedsearch.aspx?mode=advanced', headers=headers, params=params)

# Print the response
print(response.status_code)

# #write the response to a file
# with open('response.txt', 'w') as f:
#     f.write(response.text)