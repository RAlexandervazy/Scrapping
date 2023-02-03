from bs4 import BeautifulSoup
import cfscrape
import time


base_url = 'https://mx.investing.com'
url_coins = 'currencies'
url_commodities = 'commodities'


#usar funciones  - retorne arreglos para usar con cualquier moneda
#Aplicar para comodities
coins_arr = ['usd-mxn', 'eur-mxn', 'jpy-mxn', 'cny-mxn']
commodities_arr = ["gold","silver","crude-oil"]

scraper = cfscrape.create_scraper()

#Version 1.2 se genera la funcion con el tipo de variable a consultar
def Nueva_Version(tipo,specific_item):
  label="span"
  class_="text-2xl"
  if tipo=='commodities':
    URL=f'{base_url}/{url_commodities}/{specific_item}'
  else:
    URL=f'{base_url}/{url_coins}/{specific_item}'
  scraperURL = scraper.get(URL)
  soupURL = BeautifulSoup(scraperURL.content, "html.parser")
  valorURL = soupURL.find_all(label, class_)
  for i in valorURL:
    return f'Valor de {specific_item}: {i.text}'

for comoddities in commodities_arr:
  print(Nueva_Version("commodities",comoddities))

# def scrapValor(base_url,section_url,specific_item,label,class_):
#   URL = f'{base_url}/{section_url}/{specific_item}'
#   scraperURL = scraper.get(URL)
#   soupURL = BeautifulSoup(scraperURL.content, "html.parser")
#   valorURL = soupURL.find_all(label, class_)
#   for i in valorURL:
#     return f'Valor de {specific_item}: {i.text}'

# print('Sepracion***********************')

# for coin in coins_arr:
#   print(scrapValor(base_url,url_coins,coin,"span","text-2xl"))

# for commodi in commodities_arr:
#   print(scrapValor(base_url,url_commodities,commodi,"span","text-2xl"))

time.sleep(5)   
   