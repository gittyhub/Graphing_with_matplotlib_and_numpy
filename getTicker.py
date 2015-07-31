import urllib2
import time
import datetime

def pullData(p=['aapl']):
  listCounter = 0 
  for stocks in p:
    urlToCsv = urlToCsv = 'http://real-chart.finance.yahoo.com/table.csv?s='+stocks+'&a=11&b=12&c=2012&d=06&e=23&f=2015&g=d&ignore=.csv'
    openCsvLink = urllib2.urlopen(urlToCsv)
    listCounter += 1
    fileName = stocks+'-'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M '+ 'EST')
    fileWrite = open(fileName,'a')
    for lines in openCsvLink:
      fileWrite.write(lines)


if __name__=='__main__':
  
  #stocks_to_lookup = raw_input('hello: ')
  pullData(['tsla','lnkd'])
