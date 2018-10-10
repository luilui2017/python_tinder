import os
import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

I=1
chro = webdriver.Chrome('/Users/username/Desktop/chromedriver_win32/chromedriver')

#Go to Tinder.com
chro.get("https://tinder.com/app/login")
#You need to login Tinder.com manually and wait until the top page of your account appears, then press y in the window.
#The program put "yes"(right crick) /second
key = input('Press y when the top page of tinder appears')

if key == "y":
    while I < 10000:
        I=I+1
        chro.find_element_by_tag_name("body").send_keys(Keys.RIGHT)
        time.sleep(1)
        print(I)
    else:
        print("swipe 10000 people")
        chro.close()
        
