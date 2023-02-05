import clases
import time



valores = clases.Scrappering
#usar funciones  - retorne arreglos para usar con cualquier moneda
#Aplicar para comodities


#Version 1.2 se genera la funcion con el tipo de variable a consultar


for comoddities in valores.commodities_arr:
  print(valores.Nueva_Version("commodities",comoddities))
for coin in valores.coins_arr:
  print(valores.Nueva_Version("coin",coin))
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
   