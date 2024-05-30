from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd

driver = webdriver.Chrome() 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r'user-data-dir=C:/remote-profile')
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://x.com/Aspirin_4140')
time.sleep(3)

for c in range(0,10000):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)

    time.sleep(0.5)
    #body = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div')
    #className = driver.find_elements(By.CLASS_NAME,"css-175oi2r")
    fe = driver.find_elements(By.CSS_SELECTOR, "#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div:nth-child(3) > div > div > section > div > div > div:nth-child(6) > div > div > article > div > div > div.css-175oi2r.r-18u37iz > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu > div:nth-child(2)")
    #css17 = driver.find_elements(By.CSS_SELECTOR, "#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div:nth-child(3) > div > div > section > div > div > div:nth-child(6)")
    df = pd.DataFrame({'text' : ['start']})
   
    for i in fe:
        context = i.text
        new_row = {'text' : [context]}
        print(context)
        df = df._append(new_row, ignore_index=True) 
    df.to_excel('df.xlsx') 