from clases import Scrapping
import time



coins = Scrapping('currencies')
commodities = Scrapping('commodities')

resultado_coins = coins.makeScrapping()
resultado_comoddities = commodities.makeScrapping()
print(resultado_coins)
print(resultado_comoddities)

cwd = coins.NewDoc()
coins.InsertData(cwd,resultado_comoddities)


#coins.changeStatic('ars-mxn')
#coins.makeScrapping()
#bitcoin = Scrapping('indices', ['investing.com-btc-mxn'])
#print(bitcoin.makeScrapping())

time.sleep(5)   
   