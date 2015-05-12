from scrapy import Spider
from dota2Blog.items import Dota2BlogItem  #import items store
from scrapy.http import Request
from scrapy.selector import Selector

class dota2Spider(Spider):
    name = 'dota2Spider'   #define our Spider name
    allowed_domains = ['dota2.com']   #rule the allowed domain name
    start_urls = ['http://blog.dota2.com/2015/05/compendium-rewards-incoming/',]   #scrapy starting url
    def parse(self, response):#parse data
        
        #xpath Selector
        sel = Selector(response)
        item = Dota2BlogItem()
        item['title'] = sel.xpath('//title').extract()[0]
        item['url'] = response.url
     
        yield item

        # get next article's url

        nextUrl = sel.xpath('//a[@rel = "prev"]/@href').extract()[0]
        print 'nextUrl is : '
        print nextUrl
        yield Request(nextUrl, callback=self.parse)