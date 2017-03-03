# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

# Scrapy 的每个Item（条目）对象表示网站上的一个页面

class Article(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
