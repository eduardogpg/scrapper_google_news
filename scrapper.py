# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import threading

GOOGLE_NEWS_URL = 'https://news.google.com.mx/'
CUSTOME_TARGET = 'www.eluniversal.com/'


class Article(object):
	def __init__(self, title, url):
		self.title = title
		self.url = url
		self.release_date = datetime.now()


def get_container(url, tag, **kwgars):
	request = request.get(url)
	if request.status_code == 200:
		html = BeautifulSoup(request.text, "html.parser")
		containers = html.find_all('h2', **kwgars)
		return container
	return None

def spider(pos, container):
	title = container.find('span', {'class': 'titletext'}).getText()
	url = container.find('a').get('href')
	new_article = Article(title, url)
	
def scrap_site():
	request = requests.get(GOOGLE_NEWS_URL)
	status = request.status_code
	
	if status == 200:
		html = BeautifulSoup(request.text, "html.parser")
		containers_ = html.find_all('h2',{'class': 'esc-lead-article-title'})
		
		for pos, container in enumerate(containers_):
			sender = threading.Thread(name='spider', target=spider, args=(pos,container,))
			sender.start()


if __name__ == '__main__':
	scrap_site()
	


