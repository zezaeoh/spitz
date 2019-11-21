import scrapy


class SnapFitSpider(scrapy.Spider):
    name = 'snap_fit'
    allowed_domains = ['66girls.co.kr']
    start_urls = ['http://66girls.co.kr/']

    def parse(self, response):
        pass
