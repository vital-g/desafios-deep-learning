# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class DatabloggerSpider(scrapy.Spider):
    name = 'airliners'
#    allowed_domains = ['https://www.airliners.net/']
    start_urls = ['https://www.airliners.net/search?keywords=klm&page=1/']
    base_url = 'https://www.airliners.net/search?keywords=klm&page='
    n = 1

    #location of csv file
    custom_settings = {
       'FEED_URI' : 'tmp/airliners.csv',
       'IMAGES_STORE' : 'tmp/images/klm'
   }

    def parse(self, response):
        #Extract product information

        for item in self.scrape(response):
            scraped_info = {
                'name' : item[0],
                'image_urls' : [item[1]]
            }
            
            yield scraped_info
#        next_page = response.xpath('//*[@id="layout-page"]/div[2]/section/section/section/div/div[1]/ul/li[13]/a'
#                                   ).extract_first()
        
        for a in response.css('li.next a'):
                yield response.follow(a, callback=self.parse)
            
    def scrape(self, response):
        name = response.css('.ua-name-content::text').extract()
        images = response.css('.lazy-load::attr(src)').extract()
        
        return zip(name,images)