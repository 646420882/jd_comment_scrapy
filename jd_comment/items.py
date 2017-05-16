# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdCommentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    username = scrapy.Field()
    user_ID = scrapy.Field()
    user_level = scrapy.Field()
    time = scrapy.Field()
    good_ID = scrapy.Field()
    good_name = scrapy.Field()
    content = scrapy.Field()
    score = scrapy.Field()
    source = scrapy.Field()
    vote_count = scrapy.Field()
    reply_count = scrapy.Field()
