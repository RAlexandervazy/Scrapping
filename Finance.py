from bs4 import BeautifulSoup
import requests
import pandas as pd
import cfscrape
import time


valorfinalUSD= []
valorfinalEur= []
valorfinaljpy=[]   #Yen Japo
valorfinalcny=[]   #Yuan chino
valorfinalOro=[]
valorfinalPlata=[]
valorfinalPetroleo=[]


scraper = cfscrape.create_scraper()
#headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61'}
#The url's are declared
#urlusd = "https://mx.investing.com/currencies/usd-mxn"
#pageusd = requests.get(urlusd, headers=headers)
#soupusd = BeautifulSoup(pageusd.content,"html.parser")


scraperusd= scraper.get('https://mx.investing.com/currencies/usd-mxn')
scrapereur= scraper.get('https://mx.investing.com/currencies/eur-mxn')
scraperjpy= scraper.get('https://mx.investing.com/currencies/jpy-mxn')
scrapercny= scraper.get('https://mx.investing.com/currencies/cny-mxn')
scraperOro= scraper.get('https://mx.investing.com/commodities/gold')
scraperPlata= scraper.get('https://mx.investing.com/commodities/silver')
scraperPetroleo= scraper.get('https://mx.investing.com/commodities/crude-oil')

soupusd = BeautifulSoup(scraperusd.content, "html.parser")
soupeur = BeautifulSoup(scrapereur.content, "html.parser")
soupjpy = BeautifulSoup(scraperjpy.content, 'html.parser')
soupcny = BeautifulSoup(scrapercny.content, 'html.parser')
soupOro = BeautifulSoup(scraperOro.content, 'html.parser')
soupPlata = BeautifulSoup(scraperPlata.content, 'html.parser')
soupPetroleo = BeautifulSoup(scraperPetroleo.content, 'html.parser')

    #Costo

Valorusd = soupusd.find_all("span", class_="text-2xl")
ValorEur = soupeur.find_all('span', class_="text-2xl")
Valorjpy = soupjpy.find_all('span', class_="text-2xl")
Valorcny = soupcny.find_all('span', class_="text-2xl")
ValorOro = soupOro.find_all('span', class_="text-2xl")
ValorPlata = soupPlata.find_all('span', class_="text-2xl")
ValorPetroleo = soupPetroleo.find_all('span', class_="text-2xl")

for i in Valorusd:
    valorfinalUSD.append(i.text)
for i in ValorEur:
    valorfinalEur.append(i.text)   
for i in Valorjpy:
    valorfinaljpy.append(i.text)
for i in Valorcny:
    valorfinalcny.append(i.text)
for i in ValorOro:
    valorfinalOro.append(i.text)
for i in ValorPlata:
    valorfinalPlata.append(i.text)
for i in ValorPetroleo:
    valorfinalPetroleo.append(i.text)


print(("Dolar {}, Euro {}, Yen japones {}, Yuan Chino {}, Oro {}, Plata {}, Petroleo {}").format(valorfinalUSD,valorfinalEur,valorfinaljpy,valorfinalcny, valorfinalOro, valorfinalPlata, valorfinalPetroleo))

time.sleep(10)   
   