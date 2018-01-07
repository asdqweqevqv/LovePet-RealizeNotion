# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field

class CpsecspidersItem(Item):

    article_name = Field()
    article_url = Field()
    article_content = Field()
    article_time = Field()
    article_id = Field()
    crawl_time = Field()
    article_from = Field()
    click_num = Field()
    reply_num = Field()
    article_author =Field()