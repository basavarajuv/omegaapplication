from django.shortcuts import render
import requests
import xmltodict
from collections import OrderedDict
from newspaper import Article
import json

# Create your views here.

def global_news():
	'''function for getting the global news'''
	url = "https://news.google.com/news/rss"
	request = requests.get(url)
	order_dict = xmltodict.parse(request.content)
	dict_data = dict(order_dict)
	res_list = []
	for key in dict_data.keys():
		for i in dict_data[key]['channel']['item']:
			d = {}
			article = Article(i['link'], language="en")
			article.download()
			article.parse()
			article.nlp()
			d['title'] = i['title']
			d['link'] = i['link']
			d['pub_date'] = i['pubDate']
			d['source'] = i['source']
			d['image'] = article.top_image
			d['description'] = article.text
			payload = {'document': d['description']}
			summary_url = "https://summarization.dev.iamplus.services/summarize"
			request = requests.post(summary_url, data = json.dumps(payload))
			d.update(request.json())
			res_list.append(d)

	print("global news :",res_list)

global_news()

def india_news():
	'''function for getting the india news'''
	res_data = {}
	url = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
	article = Article(url, language="en")
	article.download()
	article.parse()
	article.nlp()
	res_data["title"] = article.title
	res_data["description"] = article.text
	res_data["image"] = article.top_image
	payload = {'document': res_data['description']}
	summary_url = "https://summarization.dev.iamplus.services/summarize"
	request = requests.post(summary_url, data = json.dumps(payload))
	res_data.update(request.json())

	print("india news :",res_data)

india_news()

def usa_news():
	'''function for getting the usa news'''
	res_data = {}
	url = "https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en"
	article = Article(url, language="en")
	article.download()
	article.parse()
	article.nlp()
	res_data["title"] = article.title
	res_data["description"] = article.text
	res_data["image"] = article.top_image
	payload = {'document': res_data['description']}
	summary_url = "https://summarization.dev.iamplus.services/summarize"
	request = requests.post(summary_url, data = json.dumps(payload))
	res_data.update(request.json())

	print("usa news :",res_data)

usa_news()

def singapore_news():
	'''function for getting the singapore news'''
	res_data = {}
	url = "https://news.google.com/topstories?hl=en-SG&gl=SG&ceid=SG:en"
	article = Article(url, language="en")
	article.download()
	article.parse()
	article.nlp()
	res_data["title"] = article.title
	res_data["description"] = article.text
	res_data["image"] = article.top_image
	payload = {'document': res_data['description']}
	summary_url = "https://summarization.dev.iamplus.services/summarize"
	request = requests.post(summary_url, data = json.dumps(payload))
	res_data.update(request.json())

	print("singapore news :",res_data)

singapore_news()

def uk_news():
	'''function for getting the uk news'''
	res_data = {}
	url = "https://news.google.com/topstories?hl=en-GB&gl=GB&ceid=GB:en"
	article = Article(url, language="en")
	article.download()
	article.parse()
	article.nlp()
	res_data["title"] = article.title
	res_data["description"] = article.text
	res_data["image"] = article.top_image
	payload = {'document': res_data['description']}
	summary_url = "https://summarization.dev.iamplus.services/summarize"
	request = requests.post(summary_url, data = json.dumps(payload))
	res_data.update(request.json())

	print("uk news :",res_data)

uk_news()

def uae_news():
	'''function for getting the uae news'''
	res_data = {}
	url = "https://news.google.com/topstories?hl=ar&gl=AE&ceid=AE:ar"
	article = Article(url, language="en")
	article.download()
	article.parse()
	article.nlp()
	res_data["title"] = article.title
	res_data["description"] = article.text
	res_data["image"] = article.top_image
	payload = {'document': res_data['description']}
	summary_url = "https://summarization.dev.iamplus.services/summarize"
	request = requests.post(summary_url, data = json.dumps(payload))
	res_data.update(request.json())

	print("uae news :",res_data)

uae_news()

