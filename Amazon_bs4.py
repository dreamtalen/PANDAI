# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import HTMLParser
import json
import re

if __name__ == '__main__':
	for i in range(10):
		try:
			url = 'http://www.amazon.co.jp/dp/B010MR4T5M'
			resp = requests.get(url)
			# with open('amazon_result.txt', 'w') as f:
				# f.write(resp.text.encode('utf-8'))
			# print resp.text.encode('utf-8')
			soup = BeautifulSoup(resp.text)
			soup.prettify()
			# print soup.find_all(attrs={'class':'content'})
			title = soup.find('span', id='productTitle').string.encode('utf-8')
			print title

			price = soup.find('span', id='priceblock_ourprice').string
			price = int(price[2:].encode('utf-8').replace(',',''))

			if price<5000:	price = price*0.066
			elif price<15000:	price = price*0.065
			elif price<30000:	price = price*0.064
			else:	price = price*0.062
			print price

			picUrl = soup.find('img', id='landingImage')['data-a-dynamic-image']
			BigPic = json.loads(picUrl).keys()[-1]
			pic = re.sub(r'_SX.*_.','', BigPic)
			print pic
			r = requests.get(pic, stream=True)
			with open('233.jpg', 'wb') as f:
				for chunk in r.iter_content():
					f.write(chunk)
		except:
			pass