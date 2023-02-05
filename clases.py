from bs4 import BeautifulSoup
import cfscrape


class Scrapping:
    coins_arr = ['usd-mxn', 'eur-mxn', 'jpy-mxn', 'cny-mxn']
    commodities_arr = ["gold","silver","crude-oil"]
    scraper = cfscrape.create_scraper()

    def __init__(self, endpoint, endpoint_arr = [], base_url= 'https://mx.investing.com', label="span", html_class="text-2xl"):
        self.base_url = base_url
        self.endpoint = endpoint
        self.label = label
        self.html_class = html_class
        self.resultado = []
        if endpoint == 'commodities': 
          self.specific_item_arr = self.commodities_arr
        elif endpoint == 'coins':
          self.specific_item_arr = self.coins_arr
        else:
          self.specific_item_arr = endpoint_arr
          
    def makeScrapping(self):
        for item in self.specific_item_arr:
          URL=f'{self.base_url}/{self.endpoint}/{item}'
          scraperURL = self.scraper.get(URL)
          soupURL = BeautifulSoup(scraperURL.content, "html.parser")
          valorURL = soupURL.find_all(self.label, self.html_class)
          for i in valorURL:
            self.resultado.append(i.text)
        return self.resultado
    
    def changeStatic(self, new_value):
        self.coins_arr = self.coins_arr.append(new_value)