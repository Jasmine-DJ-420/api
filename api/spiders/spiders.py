#-*-coding:utf-8-*-
__author__ = 'DJ'

from scrapy.spiders import BaseSpider
from scrapy import Request
from api.items import urlItem
import json

class test(BaseSpider):

    access_token = "access_token=412ac4e93b48227b32c6f36d85276361e8b03f00"
    name = "test"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "https://api.stackexchange.com/2.2/questions?order=desc&sort=votes&site=stackoverflow&run=true"
    ]
    download_warnsize = 0
    download_timeout = 1800

    def parse(self, response):
        json_response = json.loads(response.body_as_unicode())

        header = response.headers
        # link1 = header["Link"]
        # link2 = link1.split("<")
        # link = link2[1].split(">")[0]
        item = urlItem()
        item['url'] = header
        yield item

        print header


        # new_request = Request(link, callback=self.parse)
        # yield new_request

