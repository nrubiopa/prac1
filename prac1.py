import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
link = "https://www.casadellibro.com/libro-fortunata-y-jacinta---estuche/9788491819165/11405930"
page = requests.get(link)
soup = BeautifulSoup(page.content)
titulo = soup.find('title')
titulo = re.findall('[a-zA-Z0-9_][^|]*', titulo.string)[0][:-1]
autor = soup.find('title')
autor = re.findall('[a-zA-Z0-9_].*[a-zA-Z0-9_]',re.findall('\|.*\|', autor.string)[0])[0]
precio = soup.find_all('script', type="application/ld+json")
precio = re.findall('"Price":"\d*.\d*"', str(precio))
precio = float(re.findall('\d\d\.\d\d', str(precio))[0])
resumen = str(soup.find_all('div', class_="resume-body")[0].string)
d = {}
info = soup.find_all('div', class_="row text-body-2 no-gutters")
for i in info:
  if len(i.find_all('span')) == 2:
    d[i.find_all('span')[0].string] = i.find_all('span')[1].string
info = d
df = pd.DataFrame({'Titulo':[titulo], 'Autor': [autor], 'Precio': [precio], 'Resumen': resumen,'Info': [info]})