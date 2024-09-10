import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svetiljniki = response.css('div._Ud0k')
        for svet1 in svetiljniki:
            yield {
                'name': svet1.css('div.lsooF  div.wYUX2  a.ui-GPFV8  span::text').get(),
                'price': svet1.css('div.lsooF  div.wYUX2  div.q5Uds span.ui-LD-ZU::text').get(),
                'url': svet1.css('div._Ud0k div.Gb9dg a.ui-GPFV8 div.Pk6w8 img').css('img').xpath('@src').extract()[0]
            }
