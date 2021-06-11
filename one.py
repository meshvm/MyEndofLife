
import random
import os
import re
import time
import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# product=input("Enter product name")

# #
option = Options()
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }
d["pageLoadStrategy"] = "none"  #  complete
option = Options()
#option.add_argument("--headless")
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-images")
option.add_argument("--no-sandbox")
option.add_experimental_option("prefs", {
   "profile.default_content_setting_values.notifications": 2,
   "profile.managed_default_content_settings.images":2
})

path = "/home/sudhanshu/Desktop/first_project/ChromeDriver/chromedriver"
driver = webdriver.Chrome(chrome_options=option, executable_path=path)
def getlist():   
   product=str(input("Enter product name"))
   link ="https://endoflife.date/"+product
   a_link = link
   driver.get(a_link)
   try:
      initial_results = driver.find_element_by_class_name('main')
      print("count",initial_results) 
      driver.close() 
      
   except NameError:
      print("NameError")  
      driver.close() 
      
   else:
      print("everything is fine")   
      driver.close() 

getlist()


