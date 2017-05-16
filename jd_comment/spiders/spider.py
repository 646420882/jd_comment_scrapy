#!/usr/bin/env python
# encoding: utf-8

import scrapy
from scrapy import Request
from scrapy.selector import Selector
from jd_comment.items import JdCommentItem
import json

class JdSpider(scrapy.Spider):
    name = 'comment'

    def start_requests(self):
        for k in range(0,1000):
            url = 'http://club.jd.com/comment/productPageComments.action?callback=&productId=3014239&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0'%(k)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        json_data = json.dumps(jsonresponse, ensure_ascii=False, encoding='gbk', indent=4)
#        # json format to dict format
#        str_data = str(json_data).decode("gbk").encode("utf8")
#        data = json.loads(unicode(str_data, "utf8"))
#        comments = data['comments']
        comments = jsonresponse['comments']
        for comment in comments:
            item = JdCommentItem()
            item['username'] = comment['nickname']
            item['user_ID'] = comment['id']
            item['user_level'] = comment['userLevelName']
            item['time'] = comment['referenceTime']
            item['good_ID'] = comment['referenceId']
            item['good_name'] = comment['referenceName']
            item['content'] = comment['content']
            item['score'] = comment['score']
            item['source'] = comment['userClientShow']
            item['vote_count'] = comment['usefulVoteCount']
            item['reply_count'] = comment['replyCount']
            yield item
