from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions


from typing import List
from main import writercsv


# Link to UCI Campus Groups Events Website
URL = 'https://campusgroups.uci.edu/events'

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


   name = (driver.find_element(By.XPATH, '//*[contains(@id, "event")]/div/div/div[2]/div/div/h3/a')).text.strip()
   img_src_element = driver.find_element(By.XPATH, '//*[contains(@id, "event")]/div/div/div[1]/a/img')
   img_src = img_src_element.get_attribute('src').strip()
   time = (driver.find_element(By.XPATH, '//*[contains(@id, "event")]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div')).text.strip()
   location = (driver.find_element(By.XPATH, '//*[contains(@id, "event")]/div/div/div[2]/div/div/div[1]/div[2]')).text.strip().replace(',', '')

   # event_link = driver.find_element(By.XPATH, '//*[contains(@id, "event")]/div/div/div[2]/div/div/h3/a')

   


   if verbose:
       print("Event Name: ", name)
       print("Event Image Src: ", img_src)
       print("Event Time: ", time)
       print("Event Location: ", location)


   return event_list_data


if __name__ == '__main__':
   event_data = scrape(verbose=True)
   writecsv(event_data, 'eventinfo.csv')


driver.quit()
