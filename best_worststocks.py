#===Assignment 2:best & worst performing stocks===#

import urllib
import csv

performance = []
stocklist = ['AXP','AAPL','BA','CAT','CVX','CSCO','KO','DIS','DWDP','XOM',\
             'GE','GS','HD','IBM','INTC','JNJ','JPM','MCD','MMM','MRK',\
             'MSFT','NKE','PFE','PG','TRV','UNH','UTX','VZ','V','WMT']
for stock in stocklist:
    url = "https://marketdata.websol.barchart.com/getHistory.csv?"

    key = "6737d798d17f68384ec9b40e569e04a2"

    url = url + "apikey=" + key

    url = url + "&symbol=" + stock

    url = url + "&type=daily&startDate=20160104"

    url = url + "&splits=true&dividends=false&volume=sum"

    filename = "DJIA2017/" + stock + ".csv"
    urllib.urlretrieve(url,filename)

    stockfile = open(filename, "r")
    data = csv.reader(stockfile)
    for line in data:
        if "2016-12-30" in line:
            close1 = line[6]
            close1 = float(close1)
        if "2017-12-29" in line:
            close2 = line[6]
            close2 = float(close2)
    final_change = close2 - close1
    final_change = ((final_change/close1)*100.0)
    final_change_rounded = round(final_change, 2)
    newlist = []
    newlist.append(final_change_rounded)
    newlist.append(stock)
    performance.append(newlist)

performance.sort(reverse=True)
for i in range(0,30):
    print performance[i][0], performance[i][1]
