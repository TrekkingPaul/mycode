#!/usr/bin/python3
# python3 -m pip install selenium
# download gecko webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import getpass

myemail = input("What is the email address associated with your Pizza Profile? ")
mypass = getpass.getpass("What is your Pizza Profile password? ")

# if you downloaded geckodriver to a random place, tweak the path in the following
# line to point the program to your copy of the geckodriver
driver = webdriver.Firefox(executable_path=r"/usr/bin/geckodriver.exe")

# open the dominos website
driver.get("https://dominos.com/en/")

time.sleep(2)
click_sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/nav/ul[2]/li[1]/button")
click_sign_in.click()

time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="Email"]').click()
driver.find_element(By.XPATH, '//*[@id="Email"]').send_keys(myemail)

time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="Password"]').click()
driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys(mypass + Keys.RETURN)
time.sleep(3)

# at this point you should be signed into your
# Domino's Pizza Profile!

