import pandas as pd
import requests
from bs4 import BeautifulSoup


webpage=requests.get('https://www.premierleague.com/stats/top/players/goals?se=578').content
soup=BeautifulSoup(webpage,'html')
print(soup.prettify())

tableclass=soup.find('div',class_='table statsTable stats-table')
table_data = tableclass.find('table')
header = table_data.find('thead')
header = [head.text for head in header.find_all('th')]
header= header[:-1]
data = table_data.find('tbody')
datas = []
for i in data.find_all('tr'):
    row = [j.text for j in i.find_all('td')]
    datas.append(row)

cleaned_data = [[x.strip() for x in sublist] for sublist in datas]
cleaned_data = [sublist[:-1] for sublist in cleaned_data]

import csv
with open('datas.csv','w') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)
    csv_writer.writerows(cleaned_data)


# In[ ]:




