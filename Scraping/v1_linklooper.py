from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.common.alert import Alert
from datetime import date, timedelta
from bs4 import BeautifulSoup
import cloudscraper
import time
import random
import requests
import pandas as pd
import re
import json
import pickle


link1 = ['https://bit.unibocconi.it/hc/it/categories/4407572405138-Alloggi-on-campus','https://bit.unibocconi.it/hc/it/categories/4407572389778-Agevolazioni','https://bit.unibocconi.it/hc/it/categories/4405709230354-Biblioteca','https://bit.unibocconi.it/hc/it/categories/4407349830674-Double-Degree','https://bit.unibocconi.it/hc/it/categories/4407569547154-Free-Mover','https://bit.unibocconi.it/hc/it/categories/4406571640978-ITEC-IT-Education-Center-','https://bit.unibocconi.it/hc/it/categories/4406571634962-Lingue','https://bit.unibocconi.it/hc/it/categories/4407579238034-Tasse-e-contributi']

# SET UP THE DRIVER
chrome_driver_path = '/Users/valedipalo/drivers/chromedriver' #
driver = webdriver.Chrome(chrome_driver_path)

link2 = []
link3 = []
bad_links = []


def looper_test1(link):
        delay = random.randint(2, 5)
        print("Sleep " + str(delay) + "s")
        time.sleep(delay)

        scraper = cloudscraper.create_scraper(delay=10)
        res = requests.get(
            url='https://proxy.scrapeops.io/v1/',
            params={
                'api_key': 'ba94a35d-f809-4077-9a4c-c23c77d5c8f5',
                'url': link,
            },
        )
        print(res.status_code)
        soup = BeautifulSoup(res.text,"html.parser")
        inner2links = soup.find_all('section')
        for i in inner2links:
            link2.append('https://bit.unibocconi.it'+(i.find('a').get('href')))

def looper_test2(link):
    delay = random.randint(2, 5)
    print("Sleep " + str(delay) + "s")
    time.sleep(delay)
    res = requests.get(
        url='https://proxy.scrapeops.io/v1/',
        params={
            'api_key': 'ba94a35d-f809-4077-9a4c-c23c77d5c8f5',
            'url': link,
        },
    )
    if res.status_code == 403:
        badlink3.append(link)
    soup = BeautifulSoup(res.text,"html.parser")
    inner2links = soup.find_all('section')
    for i in inner2links:
        # print(link3)
        link3.append('https://bit.unibocconi.it'+(i.find('a').get('href')))


for link in link1:
    looper_test1(link)

for link in link2:
    looper_test2(link)

with open('finallinks.pkl', 'wb') as f:
   pickle.dump(link3, f)






## error exceeded:



