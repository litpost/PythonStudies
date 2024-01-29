
from bs4 import BeautifulSoup
import requests
import pandas as pd




alldata = []

# or i in range(1,7):
# url = f'https://www.fifacm.com/players'
url = 'https://www.futwiz.com/en/fifa22/career-mode/players'
response = requests.get(url)
# print(response.status_code, '-----------------------------------------------------')
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
 
# print(headers)
teams = soup.find_all('table',Class='table results playersearchresults')
# clubs = soup.find_all('',class_='wikitable sortable jquery-tablesorter')

print(teams)

for team in teams:
        rank = team.find('th',Name='Team').text.strip()
        # rank = club.find('th',class_='Rank').text.strip()
        # price = product.find('th',class_='price').text.strip()
        # # vendor = product.find('span',class_='retailrocket-item__vendor').text.strip()
        # category = product.select_one('th.product__info__part.nav').text.strip()
        # lizingas1 = product.find('th',class_='product-tags__s').text.strip()
        # populiari1 = product.find('th',class_='product-tags__ts').text.strip()
        #
        # tags = product.find('ul',class_='product-tags')
        # lizingas_tag='N/A'
        # naujiena_tag='N/A'
        # populiari_tag='N/A'

        # if product.tags:
        #     for tag in product.tags.find_all('li'):
        #         if 'product-tags__s' in tag.get('class',[]):
        #             lizingas_tag=tag.get('data-type-s','N/A')
        #         elif'product-tags__n' in tag.get('class',[]):
        #             naujiena_tag = tag.get('data-type-n', 'N/A')
        #         elif'product-tags__ts' in tag.get('class',[]):
        #             populiari_tag = tag.get('data-type-ts', 'N/A')

        alldata.append([
            'rank'.rank,
            # 'price'.price,
            # 'category'.category,
            # 'lizingas'.lizingas_tag,
            # 'naujiena'.naujiena_tag,
            # 'populiari'.populiari_tagory
        ])

        print(alldata,'********************************************')

df=pd.DataFrame(alldata)
df.to_csv('clubs.csv',index=False)
#         print(alldata,'********************************************')
#

