import scrapy
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from demo.items import PyItem
import requests
from requests.exceptions import RequestException


def get_one_page(url):
    # headers, 伪装成浏览器
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/68.0.3440.106 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

name = "mySpider"
key = "python"
source_url = "https://github.com/"


url = source_url+"search?utf8=%E2%9C%93&q="+key

def get_one_page(url):
    # headers, 伪装成浏览器
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/68.0.3440.106 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
html = get_one_page(url)
selector = scrapy.Selector(text=html)
lis = selector.xpath("//h3")
for li in lis:
    title =li.xpath("./a[position()=1]/@href").extract_first()
    item = PyItem()
    item["title"] = title.strip() if title else ""


link = selector.xpath("//div[@data-pjax='true']/a/@href").extract_first()
print(link)