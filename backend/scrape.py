from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import NoSuchElementException


from typing import List
from urllib.parse import urlparse

import os
import platform
from main import writecsv, removecommas


# Link to UCI Campus Groups Events Website
URL = 'https://campusgroups.uci.edu/events'

def scrape(start_position: int, end_position: int, verbose: bool = False) -> List[List]:
    """
    Scrapes all of the submissions for UCI Campus Group Events and return the data as a list of lists.
    Each i-th inner list represents the data scraped from the i-th project.

    If verbose set to True, will output all scraped data to the console.

    Will get events given a certain range based on start_position and end_position
        Ex: scrape(1, 3) will get the first, second, and third events)
    """

    event_list_data: List[List] = []

    # Preparing Selenium

    #Getting the chromedriver
    if (platform.system() == 'Windows'):
        service = Service(executable_path='backend/chromedriver/chromedriver-win64/chromedriver.exe')
    elif (platform.system() == 'Darwin'):
        service = Service(executable_path='backend/chromedriver/chromedriver-mac-x64/chromedriver')
    else:
        exit("Not compatible operating system")

    options = webdriver.ChromeOptions() # Sets up the options for Selenium
    options.add_argument("--headless=new") # Makes our options headless (so the browser won't open)
    options.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 2,
        }
    )

    driver = webdriver.Chrome(service=service, options=options)

    driver.get(URL)

    events = driver.find_elements(By.XPATH, '//*[contains(@class, "list-group-item") and contains(@id, "event_")]')

    # Looping through events on the webpage with the given range
    for event_index in range(start_position - 1, end_position + 1):  # Adjust the index to match array indexing
        curdata = []
        while event_index >= len(events):
            # Scrolling down to load more events
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait for the page to load the new events
            # time.sleep(2)
            events = driver.find_elements(By.XPATH, '//*[contains(@class, "list-group-item") and contains(@id, "event_")]')

        event = events[event_index]

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

            # Goes back to the original URL
            driver.back()

            # Removing Commas
            time = removecommas(time).replace('\n', ' ')
            address = removecommas(address).replace('\n', ' ')
            location = removecommas(location).replace('\n', ' ')

            # Appending all the data to the event_list_data
            curdata.append(name)
            curdata.append(img_src)
            curdata.append(time)
            curdata.append(location)
            curdata.append(address)

            event_list_data.append(curdata)

            if verbose:
                print("Event Name: ", name)
                print("Event Image Src: ", img_src)
                print("Event Time: ", time)
                print("Event Location: ", location)
                print("Address: ", address)
                print("-" * 50)

        except NoSuchElementException as e:
            print(f"Error: {e}")

    driver.quit()

    return event_list_data

def specifypath():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(curdir, 'eventinfo.csv')

    return filename


if __name__ == '__main__':
   event_data = scrape(1, 10, verbose=True)
   filename = specifypath()
   writecsv(event_data, filename)
