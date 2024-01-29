
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

driver.get('https://www.fifacm.com/players')

tbody = driver.find_element(By.CLASS_NAME,'player-row')

data = []

for tr in tbody.find_elements(By.XPATH,'//tr'):
    row = [item.text for item in tr.find_elements(By.TAG_NAME, 'td')]
    data.append(row)

print(data,'********************************************')

df=pd.DataFrame(data)
df.to_csv('clubs.csv',index=False)
