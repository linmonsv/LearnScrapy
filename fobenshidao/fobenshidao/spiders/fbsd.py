# -*- coding: utf-8 -*-
import scrapy
import re

class FbsdSpider(scrapy.Spider):
    name = "fbsd"
    #allowed_domains = ["http://www.xxbiquge.com/2_2640/"]
    start_urls = (
        'http://www.xxbiquge.com/2_2640//',
    )

    def parse(self, response):
        #print(response.body)
        selector = scrapy.Selector(response)
        books = selector.xpath('//*[@id="wrapper"]/div[7]')
        for each in books:
            for i in range(1, 466 + 1):
                one_xpath = ('//*[@id="list"]/dl/dd[%d]' % i)
                one_data = each.xpath(one_xpath).extract()[0]
                #print('标题:' + one_data)
                one_group = re.search('.*href="(.*?.html)">(.*)</a></dd>', one_data)
                one_title = one_group.group(2)
                one_url = one_group.group(1)
                print('标题:' + one_title)
                print('地址:' + 'http://www.xxbiquge.com/2_2640//' + one_url)
