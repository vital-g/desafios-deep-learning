# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['https://www.reddit.com/r/Python/']
    start_urls = ['https://www.reddit.com/r/Python/']

    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css('._eYtD2XCVieq6emjKBH3m::text').extract()
        votes = response.css('._1rZYMD_4xY3gRcSS3p8ODO::text').extract()
        comments = response.css('.FHCV02u6Cp2zYL0fhQPsO::text').extract()
       
        #Give the extracted content row wise
        for item in zip(titles,votes,comments):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'vote' : item[1],
                'comments' : item[2],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
