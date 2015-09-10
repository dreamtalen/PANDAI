import requests
if __name__ == '__main__':
	pic = 'http://www.th7.cn/d/file/p/2014/11/23/f66dc70b5cd5004327bc38ce9be76e00.jpg'
	print pic
	r = requests.get(pic, stream=True)
	name = 'hehe'
	with open(name+'.jpg', 'wb') as f:
		for chunk in r.iter_content():
			f.write(chunk)