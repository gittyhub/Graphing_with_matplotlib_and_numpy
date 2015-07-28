import urllib2
import time

def pullData(p=['aapl']):
  #fileLine = p
  #urlToCsv = urlToCsv = 'http://real-chart.finance.yahoo.com/table.csv?s='+p+'&a=11&b=12&c=2012&d=06&e=23&f=2015&g=d&ignore=.csv'
  #openCsvLink = urllib2.urlopen(urlToCsv)
  #saveFile = open(fileLine,'a')
  r = 0
  for i in p:
    urlToCsv = urlToCsv = 'http://real-chart.finance.yahoo.com/table.csv?s='+i+'&a=11&b=12&c=2012&d=06&e=23&f=2015&g=d&ignore=.csv'
    openCsvLink = urllib2.urlopen(urlToCsv)
    saveFile = open(p[r],'a')
    r += 1
    for g in openCsvLink[1:]:
      saveFile.write(g)


if __name__=='__main__':
  '''iPut = raw_input('Stocks: ')'''
  pullData()
