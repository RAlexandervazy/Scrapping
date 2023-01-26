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

#symbols_coins = {"usd-mxn":{"$US","1"},"eur-mxn":"€"} 
scraper = cfscrape.create_scraper()

# for coin in coins_arr:
#   constructed_url = f'{base_url}/{url_coins}/{coin}' #Se arma el link
#   scraperRes = scraper.get(constructed_url) #Se genera la consulta
#   soup = BeautifulSoup(scraperRes.content, "html.parser") #Se convierte html
#   valor = soup.find_all("span", class_="text-2xl")  #Se indica la ubicación del valor deseado
#   for i in valor: 
#     #valor_final.append(i.text)
#     print(f'Valor de {coin}: {i.text}')

# for Vcommo in commodities_arr:
#   commodities_url = f'{base_url}/{url_commodities}/{Vcommo}'
#   scraperCommo = scraper.get(commodities_url)
#   soupCommo = BeautifulSoup(scraperCommo.content, "html.parser")
#   PriceCommo = soupCommo.find('span', class_="text-2xl")
#   for i in PriceCommo:
#     print(f'Valor de {Vcommo}: {i.text}')

def scrapValor(base_url,section_url,specific_item,label,class_):
  URL = f'{base_url}/{section_url}/{specific_item}'
  scraperURL = scraper.get(URL)
  soupURL = BeautifulSoup(scraperURL.content, "html.parser")
  valorURL = soupURL.find_all(label, class_)
  for i in valorURL:
    return f'Valor de {specific_item}: {i.text}'


for coin in coins_arr:
  print(scrapValor(base_url,url_coins,coin,"span","text-2xl"))

for commodi in commodities_arr:
  print(scrapValor(base_url,url_commodities,commodi,"span","text-2xl"))

print("")
#print(scrapValor(base_url,url_commodities,commodities_arr[2],"span","text-2xl"))


# scraperusd= scraper.get('https://mx.investing.com/currencies/usd-mxn')
# scrapereur= scraper.get('https://mx.investing.com/currencies/eur-mxn')
# scraperjpy= scraper.get('https://mx.investing.com/currencies/jpy-mxn')
# scrapercny= scraper.get('https://mx.investing.com/currencies/cny-mxn')
# scraperOro= scraper.get('https://mx.investing.com/commodities/gold')
# scraperPlata= scraper.get('https://mx.investing.com/commodities/silver')
# scraperPetroleo= scraper.get('https://mx.investing.com/commodities/crude-oil')

time.sleep(5)   
   