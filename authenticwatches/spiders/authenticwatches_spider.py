from scrapy import Spider,Request
from authenticwatches.items import AuthenticwatchesItem

class AuthenticWatchesSpider(Spider):
    name="authenticwatches_spider"
    allowed_urls=["https://www.authenticwatches.com/"]
    start_urls=["https://www.authenticwatches.com/rolex.html"]
    def parse(self,response):
        #rolex main urls (brwose more)
        rolex_urls = response.xpath('//div[@class="name"]/a/@href').extract()
        for url in rolex_urls:
            yield Request(url=url,callback=self.parse_category_page)

    def parse_category_page(self,response):
        #watches info
        half_watches_urls = response.xpath('//div[@class="moreinf"]/a/@href').extract()
        watchurl="https://www.authenticwatches.com/"
        #list comprehension to concat domain with sublinks in half_watches_urls
        res=[watchurl+s for s in half_watches_urls]
        for url in res:
            yield Request(url=url, callback=self.parse_watch_page)

    def parse_watch_page(self,response):
        product = response.xpath('//h1[@class="pagebanner productheader"]/text()').extract()
        if len(product)!=0:
            item_number=response.xpath('//span[@itemprop="sku"]/text()').extract()
            retail_price=response.xpath('//span[@id="pitPriceBx"]/text()').extract()
            price=response.xpath('//span[@id="pitSalePriceBx"]/text()').extract()
            availability=response.xpath('//span[@class="availability"]/text()').extract()
            condition=response.xpath('//select[@name="Condition"]/option/@value').extract()
            warranty=response.xpath('//select[@name="Warranty"]/option/@value').extract()
            image=response.xpath('//div[@class="itemimg"]/div/a/@href').extract_first()

            item=AuthenticwatchesItem()
            item["product"]=product
            item["item_number"]=item_number
            item["retail_price"]=retail_price
            item["price"]=price
            item["availability"]=availability
            item["condition"]=condition
            item["warranty"]=warranty
            item["image"]=image

            yield item
        else:
            print("*"*50)
            half_watches_urls = response.xpath('//div[@class="moreinf"]/a/@href').extract()
            watchurl="https://www.authenticwatches.com/"
            #list comprehension to concat domain with sublinks in half_watches_urls
            res=[watchurl+s for s in half_watches_urls]
            for url in res:
                yield Request(url=url, callback=self.parse_watches_page)

    def parse_watches_page(self,response):
        product = response.xpath('//h1[@class="pagebanner productheader"]/text()').extract()
        item_number=response.xpath('//span[@itemprop="sku"]/text()').extract()
        retail_price=response.xpath('//span[@id="pitPriceBx"]/text()').extract()
        price=response.xpath('//span[@id="pitSalePriceBx"]/text()').extract()
        availability=response.xpath('//span[@class="availability"]/text()').extract()
        condition=response.xpath('//select[@name="Condition"]/option/@value').extract()
        warranty=response.xpath('//select[@name="Warranty"]/option/@value').extract()
        image=response.xpath('//div[@class="itemimg"]/div/a/@href').extract_first()

        item=AuthenticwatchesItem()
        item["product"]=product
        item["item_number"]=item_number
        item["retail_price"]=retail_price
        item["price"]=price
        item["availability"]=availability
        item["condition"]=condition
        item["warranty"]=warranty
        item["image"]=image

        yield item



######################################################################

# class AuthenticWatchesSpider(Spider):
#     name="authenticwatches_spider"
#     allowed_urls=["https://www.authenticwatches.com/"]
#     start_urls=["https://www.authenticwatches.com/rolex.html"]
#     def parse(self,response):
# #rolex main urls (brwose collection  from (https://www.authenticwatches.com/rolex.html))
# #collect links to individual watch information
#         rolex1_urls = response.xpath('//div[@class="name"]/a/@href').extract()
#         for url in rolex1_urls:
#             yield Request(url=url,callback=self.parse_category1_page)
#
#     def parse_category1_page(self,response):
#     #watches info
#         category_watches_urls = response.xpath('//div[@class="moreinf"]/a/@href').extract()
#         watchurl="https://www.authenticwatches.com/"
#         #list comprehension to concat domain with sublinks in half_watches_urls
#         res1=[watchurl+s for s in category_watches_urls]
#         for url in res1:
#             yield Request(url=url, callback=self.parse_subcategory_page)
#
#     def parse_subcategory_page(self,response):
#     #watches info
#         sub_category_urls = response.xpath('///div[@class="moreinf"]/a/@href').extract()
#         watchurl="https://www.authenticwatches.com/"
#         #list comprehension to concat domain with sublinks in half_watches_urls
#         res2=[watchurl+s for s in sub_category_urls]
#         for url in res2:
#             yield Request(url=url, callback=self.parse_watch1_page)
#
#     def parse_watch1_page(self,response):
#         product = response.xpath('//h1[@class="pagebanner productheader"]/text()').extract()
#         item_number=response.xpath('//span[@itemprop="sku"]/text()').extract()
#         retail_price=response.xpath('//span[@id="pitPriceBx"]/text()').extract()
#         price=response.xpath('//span[@id="pitSalePriceBx"]/text()').extract()
#         availability=response.xpath('//span[@class="availability"]/text()').extract()
#         condition=response.xpath('//select[@name="Condition"]/option/@value').extract()
#         warranty=response.xpath('//select[@name="Warranty"]/option/@value').extract()
#         image=response.xpath('//div[@class="itemimg"]/div/a/@href').extract_first()
#
#         item=AuthenticwatchesItem()
#         item["product"]=product
#         item["item_number"]=item_number
#         item["retail_price"]=retail_price
#         item["price"]=price
#         item["availability"]=availability
#         item["condition"]=condition
#         item["warranty"]=warranty
#         item["image"]=image
#
#         yield item
#
#
#
