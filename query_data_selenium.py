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

# Close the browser
driver.quit()

# Define the headers for the POST request
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Define the data for the POST request
data = {
    '__VIEWSTATE': viewstate,
    '__EVENTVALIDATION': eventvalidation,
    # Add other necessary fields here
}

# Send the POST request
response = requests.post('https://auditor.lakecountyohio.gov/search/advancedsearch.aspx?mode=advanced', headers=headers, data=data)

# Print the response
print(response.text)