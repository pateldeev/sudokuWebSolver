from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import random
from time import sleep

browser = webdriver.Firefox()
browser.get('https://google.com')

sleep(10)

browser.close()
