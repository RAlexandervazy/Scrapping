from bs4 import BeautifulSoup
import cfscrape
import time


base_url = 'https://mx.investing.com'
url_coins = 'currencies'
url_commodities = 'commodities'


#usar funciones  - retorne arreglos para usar con cualquier moneda
#Aplicar para comodities
coins_arr = ['usd-mxn', 'eur-mxn', 'jpy-mxn', 'cny-mxn']
#symbols_coins = {"usd-mxn":{"$US","1"},"eur-mxn":"€"} 
scraper = cfscrape.create_scraper()

for coin in coins_arr:
  constructed_url = f'{base_url}/{url_coins}/{coin}'
  scraperRes = scraper.get(constructed_url)
  soup = BeautifulSoup(scraperRes.content, "html.parser")
  valor = soup.find_all("span", class_="text-2xl")
  for i in valor:
    #valor_final.append(i.text)
    print(f'Valor de {coin}: {i.text}')



# scraperusd= scraper.get('https://mx.investing.com/currencies/usd-mxn')
# scrapereur= scraper.get('https://mx.investing.com/currencies/eur-mxn')
# scraperjpy= scraper.get('https://mx.investing.com/currencies/jpy-mxn')
# scrapercny= scraper.get('https://mx.investing.com/currencies/cny-mxn')
# scraperOro= scraper.get('https://mx.investing.com/commodities/gold')
# scraperPlata= scraper.get('https://mx.investing.com/commodities/silver')
# scraperPetroleo= scraper.get('https://mx.investing.com/commodities/crude-oil')

time.sleep(10)   
   