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
   
    x = 0
    y = len(date)
    candleAr = []
    while x < y:           #Tag 2 this will create the candle stick
      appendLine = date[x], openp[x], closedp[x], highp[x], lowp[x], volume[x]
      candleAr.append(appendLine)
      x+=1

 
    fig = plt.figure(facecolor='grey')
    #ax1 = plt.subplot(2,1,1) # 1 by 1 square so 1 position, (2,3,2) 2 by 3 square at position 2 or 2 vert 3 horizontal position 2
    ax1 = plt.subplot2grid((5,4), (0,0), rowspan=4, colspan=4, axisbg = 'grey') #4 x 4 grid, start at 0,0 size row span is 3, 3 rows down, and over to the right 4
    #ax1.plot(date,openp)  #Tag 3 for the sake of the candle stick we are going to remove these graphs
    #ax1.plot(date,highp)  #Tag 3 for the sake of the candle stick we are going to remove these graphs     
    #ax1.plot(date,lowp)   #Tag 3 for the sake of the candle stick we are going to remove these graphs     
    #ax1.plot(date,closedp)  #Tag 3 for the sake of the candle stick we are going to remove these graphs     
    #candlestick(ax1, candleAr, width=1, colorup='g', colordown='r', shadowColor='w') #Tag 2. So the shadowColor here you would have to make the changes in the finance modules in two places, on in the candlestick function and another in the vline2D and add the shadowColor param here
    candlestick(ax1, candleAr, width=1, colorup='g', colordown='r') #Tag 2
    ax1.grid(True, color ='w')  #Tag 4 making grid lines white 
    ax1.spines['bottom'].set_color('#5998ff')
    ax1.spines['top'].set_color('#5998ff')
    ax1.spines['left'].set_color('#5998ff')
    ax1.spines['right'].set_color('#5998ff')
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(12)) #tim period how many you want to use
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d')) #the date format you want to show on the axis
    ax1.yaxis.label.set_color('w') #Tag 4 Makes the lables white
    ax1.tick_params(axis='y', colors='w') #Price parameter for the stock price
    plt.ylabel('Stock price')
    
    #ax1.axes.xaxis.set_ticklabels([]) #Tag 1 - here you can try to use an empyt arry but both dates will be blank all dates
    plt.setp(ax1.get_xticklabels(), visible=False) #Tag 1 - because you are sharing xaxis, you will have two date, this will hide the one on the top for stock and only show vvolum
    
    volumeMin = volume.min() #Tag 5 to use the fill, minimun value to use the fill, tells the fill how low to fill to 

    #ax2 = plt.subplot(2,1,2, sharex=ax1)
    ax2 = plt.subplot2grid((5,4), (4,0), sharex=ax1, rowspan=1, colspan=4) 
    ax2.plot(date, volume, '#00ffe8', linewidth=.8)
    #ax2.bar(date, volume, '#00ffe8', linewidth=.8) #Tag 5 removed to use the plot and fill method
    ax2.fill_between(date, volumeMin, volume, facecolor='#00ffe8', alpha=.5) #Tag 5
    ax2.axes.yaxis.set_ticklabels([]) #this removes the 'le' above the volume bar chart for the volume
    plt.ylabel('Volume')
    ax2.grid(True)
    ax2.spines['bottom'].set_color('#5998ff')
    ax2.spines['top'].set_color('#5998ff')
    ax2.spines['left'].set_color('#5998ff')
    ax2.spines['right'].set_color('#5998ff')
    ax2.tick_params(axis='x', colors='w') #Price parameter for the stock price
    ax2.tick_params(axis='y', colors='w') #Price parameter for the stock price
    
    for label in ax1.xaxis.get_ticklabels():
      label.set_rotation(45)

    for label in ax2.xaxis.get_ticklabels():
      label.set_rotation(45)

    #plt.subplots_adjust(left=.10, bottom = .20, right=.93, top=.95, wspace=.20, hspace=.45)
    plt.subplots_adjust(left=.09, bottom = .14, right=.94, top=.95, wspace=.20, hspace=0)
    plt.xlabel('Date', color='r')
    plt.ylabel('Volume', color='w')
    plt.suptitle(stock+' Stock Price', color='r')
    plt.show()
    fig.savefig(stock+'.png', facecolor=fig.get_facecolor())

if __name__ =='__main__':

  stock = ['tsla']

  for s in stock:
    graph(s)
