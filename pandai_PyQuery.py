import sys
import urllib
reload(sys)
sys.setdefaultencoding( "utf-8" )
from pyquery import PyQuery as pq
import HTMLParser
print 'begin'

doc = pq (url='http://www.amazon.co.jp/dp/B00TRURY0I/', headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'})
productName = doc('#productTitle').text()
print '[PANDAI]'+ productName

picUrl = doc('#landingImage').attr('src')
data = urllib.urlopen(picUrl).read()  
f = file("1.jpg","wb") 
f.write(data)
f.close()
print "Picture saved"

priceStr = doc('#priceblock_ourprice').text()[2:]
price = int(priceStr.replace(',',''))

if price<5000:	price = price*0.064
elif price<15000:	price = price*0.062
elif price<30000:	price = price*0.06
else:	price = price*0.58

print price
