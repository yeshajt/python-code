#===Assignment 1: create csv and excel files===#

import urllib

stocklist = ['AXP','AAPL','BA','CAT','CVX','CSCO','KO','DIS','DWDP','XOM',\
             'GE','GS','HD','IBM','INTC','JNJ','JPM','MCD','MMM','MRK',\
             'MSFT','NKE','PFE','PG','TRV','UNH','UTX','VZ','V','WMT']
for stock in stocklist:
    url = "https://marketdata.websol.barchart.com/getHistory.csv?"

    key = "6737d798d17f68384ec9b40e569e04a2"

    url = url + "apikey=" + key

    url = url + "&symbol=" + stock

    url = url + "&type=daily&startDate=20161230"

    url = url + "&splits=true&dividends=false&volume=sum"

    filename = "DJIA2017/" + stock + ".csv"
    urllib.urlretrieve(url,filename)
    print "Created" + stock + ".csv file"

