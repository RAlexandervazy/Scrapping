from bs4 import BeautifulSoup
import cfscrape


class Scrappering:
    coins_arr = ['usd-mxn', 'eur-mxn', 'jpy-mxn', 'cny-mxn']
    commodities_arr = ["gold","silver","crude-oil"]
    def __init__(self):
        None
    def Nueva_Version(tipo,specific_item):
        base_url = 'https://mx.investing.com'
        url_coins = 'currencies'
        url_commodities = 'commodities'
        
        scraper = cfscrape.create_scraper()
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
            costo=f'Valor de {specific_item}: {i.text}'
        return costo