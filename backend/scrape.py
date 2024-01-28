from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import NoSuchElementException


from typing import List
from urllib.parse import urlparse
from main import writecsv, removecommas


# Link to UCI Campus Groups Events Website
URL = 'https://campusgroups.uci.edu/events'

# Preparing Selenium
service = Service(executable_path='backend/chromedriver-mac-x64/chromedriver') # Gets the chromedriver.exe
options = webdriver.ChromeOptions() # Sets up the options for Selenium
options.add_argument("--headless=new") # Makes our options headless (so the browser won't open)
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(5)

driver.get(URL)


def scrape(verbose: bool=False) -> List[List]:
    """
    Scrapes all of the submissions for UCI Campus Group Events and return the data as a list of lists.
    Each i-th inner list represents the data scraped from the i-th project.

    If verbose set to True, will output all scraped data to the console.
    """
    event_list_data: List[List] = []

    # Looping through all events on the webpage
    for event in driver.find_elements(By.XPATH, '//*[contains(@class, "list-group-item") and contains(@id, "event_")]'):
        try:
            # Getting Name, image source, time, and location
            name = (event.find_element(By.XPATH, './/div/div/div[2]/div/div/h3/a')).text.strip()
            img_src_element = event.find_element(By.XPATH, './/div/div/div[1]/a/img')
            img_src = img_src_element.get_attribute('src').strip()
            time = (event.find_element(By.XPATH, './/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div')).text.strip()
            location = (event.find_element(By.XPATH, './/div/div/div[2]/div/div/div[1]/div[2]')).text.strip()

            
            # Clicking on the link of the associated event
            event_link = event.find_element(By.XPATH, './/div/div/div[2]/div/div/h3/a')
            link_href = event_link.get_attribute('href') # Getting the href of the address
            driver.get(link_href)
            
            try:
                # Get the address from the webpage if it exists
                address = driver.find_element(By.XPATH, '//*[@id="event_main_card"]/div[3]/div/div[2]/div[2]/p[2]').text.strip()
            except NoSuchElementException:
                # If not, leave blank
                address = ""

            
            driver.back()
        
            if verbose:
                print("Event Name: ", name)
                print("Event Image Src: ", img_src)
                print("Event Time: ", time)
                print("Event Location: ", location)
                print("Address: ", address) # Needs further testing on websites which have the address, tested on a website without address
                print("-" * 50)
        
        except NoSuchElementException as e:
            print(f"Error: {e}")

    return event_list_data


if __name__ == '__main__':
   event_data = scrape(verbose=True)
   writecsv(event_data, 'eventinfo.csv')


driver.quit()
