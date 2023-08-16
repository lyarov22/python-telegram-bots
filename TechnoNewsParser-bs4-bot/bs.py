from bs4 import BeautifulSoup
import requests

rq = requests.get('http://www.ixbt.com/export/articles.rss')
soup = BeautifulSoup(rq.text, 'html.parser')


first_title = (str(soup.find('item')('title')[0])[7::]).replace('</title>', '\n')

last_title = (str(soup.find('item')('description')[0])[125::]).replace(']]></description>', '')

def first_new():
  return first_title

def last_new():
  return last_title
