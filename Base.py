import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick #Tag 2 Candlestick
import matplotlib
matplotlib.rcParams.update({'font.size':9}) #Change the font on the graph to 9

def graph(stock):
    stockFile = stock+'.txt'
    date, closedp, highp, lowp, openp, volume, adjClose = np.loadtxt(stockFile, delimiter=',', unpack=True, converters={0:mdates.strpdate2num('%Y-%m-%d')})

    fig = plt.figure()     #assigns fig to plt.figure() greats the graph
    ax1 = plt.subplot2grid((4,4), (0,0), rowspan=4, colspan=4)  #Creates a subplot grid using subplot2grid, 4x4, starting at (0,0), to span for 4 rows, and 4 col 
    ax1.plot(date,openp) #on ax1 use the plot function to plot the date and open price on ax1
    ax1.grid(True)       #on ax1 use the grid function to turn on the gird 
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(8)) 
    
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y')) 

    ax1.tick_params(axis='y', color='red') #on ax1 use the tick_params  
    plt.ylabel('Stock Price')   #plot the y label axis as Stock Prices
    plt.show()    #show the graph


if __name__=='__main__':
  stock = ['tsla']

  for s in stock:
    graph(s)




