import scrapy
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from demo.items import PyItem

class MySpider(scrapy.Spider):
    name = "mySpider"
    key = "python"
    source_url = "https://github.com/"


    def start_requests(self):
        url = MySpider.source_url+"search?q="+MySpider.key
        yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        try:
            dammit = UnicodeDammit(response.boby,["utf-8","gbk"])
            data =dammit.unicode_markup
            selector = scrapy.Selector(text=data)
            lis = selector.xpath('//a@[class="v-align-middle"')
            for li in lis:
                title = li.xpath("./a[position()=1]/@herf").extract_first()
                item = PyItem()
                item["title"]=title.strip()if title else ""
                yield item
            link = selector.xpath("//div[@class='paginate-container codesearch-pagination-container']/a/@href").extract_first()
            if link<5:
                url = response.urljoin(link)
                yield scrapy.Request(url=url,callback=self.parse)
        except Exception as err:
            print(err)