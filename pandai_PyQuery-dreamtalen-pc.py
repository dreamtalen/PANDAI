import sys
import urllib
reload(sys)
sys.setdefaultencoding( "utf-8" )
from pyquery import PyQuery as pq
import HTMLParser
print 'begin'

amazon_url = """
http://www.amazon.co.jp/dp/B00WDDE7DS/
"""

doc = pq (url=amazon_url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'})
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

if price<5000:	price = price*0.06
elif price<15000:	price = price*0.059
elif price<30000:	price = price*0.058
else:	price = price*0.056

print price
