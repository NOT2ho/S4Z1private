from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd

driver = webdriver.Chrome() 
driver.get('https://x.com/Aspirin_4140')
time.sleep(3)
for c in range(0,10000):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)

    time.sleep(2)
    css17 = driver.find_elements(By.CLASS_NAME, "css-175oi2r")
    df = pd.DataFrame({'text' : ['start']})
   
    for i in css17:
        context = i.text
        new_row = {'text' : [context]}
        print(context)
        df = df._append(new_row, ignore_index=True)  
        df.to_excel('df.xlsx')