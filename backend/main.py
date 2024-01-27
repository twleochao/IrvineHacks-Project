from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions


from typing import List


# Link to UCI Campus Groups Events Website
URL = 'https://campusgroups.uci.edu/events'


# The name of each column in the CSV file export
HEADERS = ['Event Image Src', 'Event Name', 'Event Location', 'Event Time']


# Preparing Selenium
service = Service(executable_path='backend/chromedriver-mac-x64/chromedriver') # Gets the chromedriver.exe
options = webdriver.ChromeOptions() # Sets up the options for Selenium
options.add_argument("--headless=new") # Makes our options headless (so the browser won't open)
driver = webdriver.Chrome(service=service, options=options)


driver.get(URL)


def scrape(verbose: bool=False) -> List[List]:
   """
   Scrapes all of the submissions for UCI Campus Group Events and return the data as a list of lists.
   Each i-th inner list represents the data scraped from the i-th project.
  
   If verbose set to True, will output all scraped data to the console.
   """
   event_list_data: List[List] = []


   '''
   for event in driver.find_elements(By.XPATH, '//*[contains(@id, "event")]'):
       img_src = event.find_element(By.XPATH, '//*[contains(@id, "event")]/div/div/div[1]/a/img')
       name = (event.find_element(By.XPATH, '//*[contains(@id, "event")]/div/div/div[2]/div/div/h3/a')).text


       if verbose:
           print("Event Image Src:", img_src)
           print("Event Name: ", name)
   '''


   img_src = driver.find_element(By.XPATH, '//*[contains(@id, "event")]/div/div/div[1]/a/img')
   name = (driver.find_element(By.XPATH, '//*[contains(@id, "event")]/div/div/div[2]/div/div/h3/a')).text


   if verbose:
       print("Event Image Src:", img_src)
       print("Event Name: ", name)


   return event_list_data


if __name__ == '__main__':
   event_data = scrape(verbose=True)


driver.quit()
