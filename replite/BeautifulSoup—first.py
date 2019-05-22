import urllib.request#Python 提供了一个支持处理网络链接的内置模块urllib
from bs4 import BeautifulSoup

class Scraper(object):
	"""docstring for Scraper"""
	def __init__(self, site):#接受要爬取的网站作为参数
		self.site = site

	def srape(self):#需要从传入的网站中爬取数据时则调用该方法
		r = urllib.request.urlopen(self.site)#向网站发起请求，并返回包含HTML和其他数据的response对象
		html = r.read()#返回response对象中的HTML代码
		parser = "html.parser"
		sp = BeautifulSoup(html, parser)#解析html
		for tag in sp.find_all("a"):#找出里面的超链接
			url = tag.get("href")
			if url is None:
				continue
			if "html" in url:
				print("\n" + url)

news = "https://baike.baidu.com/item/%E7%99%BE%E5%BA%A6/6699?fr=aladdin"
Scraper(news).srape()

