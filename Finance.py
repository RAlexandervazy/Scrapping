from clases import Scrapping
import time



coins = Scrapping('currencies')
commodities = Scrapping('commodities')

resultado_coins = coins.makeScrapping()
resultado_comoddities = commodities.makeScrapping()

coins.changeStatic('ars-mxn')
coins.makeScrapping()

#Debuggear porque no devuelve valores
bitcoin = Scrapping('crypto', ['bitcoin'])
print(bitcoin.makeScrapping())

#usar funciones  - retorne arreglos para usar con cualquier moneda
#Aplicar para comodities


#Version 1.2 se genera la funcion con el tipo de variable a consultar


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
   