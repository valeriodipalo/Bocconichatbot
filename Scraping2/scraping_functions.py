import scraping_functions as sf
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

### 1. LOOPER FUNCTIONS: These funcitons are used to get all the links in the page

def looper_test1(link):
    """By putting in the list of higher level links [LEVEL 1] will return all the subsections [LEVEL 2] """
    link2 = []
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
    soup = BeautifulSoup(res.text, "html.parser")
    inner2links = soup.find_all('section')
    for i in inner2links:
        link2.append('https://bit.unibocconi.it' + (i.find('a').get('href')))
    return link2

def looper_test2(link):
    """By putting in the list of subsections links [LEVEL 1] will return all the end links [LEVEL 2] """
    link3 = []
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
        print('a bad link has been found')
        badlink3.append(link)
    soup = BeautifulSoup(res.text,"html.parser")
    inner2links = soup.find_all(class_='article-list-item')
    for i in inner2links:
        # print(link3)
        link3.append('https://bit.unibocconi.it'+(i.find('a').get('href')))
    return link3

