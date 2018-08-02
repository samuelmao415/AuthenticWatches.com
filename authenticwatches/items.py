# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class AuthenticwatchesItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product=Field()
    item_number=Field()
    retail_price=Field()
    price=Field()
    availability=Field()
    condition=Field()
    warranty=Field()
    image=Field()
