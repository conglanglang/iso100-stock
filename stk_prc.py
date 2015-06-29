#Created on 2015/06/15
#By Tea Shaw
#This script is aim to download the current price of a specific stock from SINA Stock 
#The info of each column is: stock number, stock name, opening price today, closing price today, current price, highest price today,lowest price today,don't know, don't know,stock dealed, price dealed today, date, time
#Sample 1#: http://hq.sinajs.cn/list=sh601003
#Sample 2#: http://hq.sinajs.cn/list=sz000002

import urllib

stock_num = raw_input('Please enter the stock number(6 digits): ')
#stock_num = '000002'

if stock_num.startswith('6'):
    url = 'http://hq.sinajs.cn/list=sh' + stock_num
elif stock_num.startswith('0'):
    url = 'http://hq.sinajs.cn/list=sz' + stock_num
else:
    print 'Invalid stock number!'
    quit()
    
try:    
    html = urllib.urlopen(url).read()
except:
    print 'Invalid stock number!'
    
l = html.split(',')
start = l[0]
print 'Stock number:\t\t',start[13:19]
print 'Strock Name:\t\t',start[-8:]
print 'Opening price today:\t',l[1]
print 'Closing price today:\t',l[2]
print 'Current Price:\t\t',l[3]
print 'Highest price today:\t',l[4]
print 'Lowest price today:\t',l[5]
print 'don\'t know:\t\t',l[6]
print 'don\'t know:\t\t',l[7]
print 'Stock dealed:\t\t',l[8]
print 'Price dealed:\t\t',l[9]
print 'Date:\t\t\t',l[10]
print 'Time:\t\t\t',l[11]