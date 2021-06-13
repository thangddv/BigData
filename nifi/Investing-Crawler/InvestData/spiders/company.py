import scrapy
import json
from InvestData.items import CompanyItem
from InvestData.settings import LOG_COUNTRY, ROOT_FOLDER
import urllib.parse


class CompanySpider(scrapy.Spider):
    name = 'company'
    allowed_domains = ['investing.com']
    url = 'https://www.investing.com/equities/StocksFilter?'
    custom_settings = {
        'ITEM_PIPELINES': {
            'InvestData.pipelines.CompanyPipeline': 400
        }
    }

    """
    Note:
    Edit only the feed() method to change the spider's input.
    feed() should yield a list of smlIds
    """

    def feed(self):
        # Open country list and parse one by one
        with open(ROOT_FOLDER + LOG_COUNTRY, 'r') as f:
            lines = f.readlines()

        for line in lines:
            yield json.loads(line)['smlId'],

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        params = {
            'noconstruct': '1',
            'smlID': None,
            'tabletype': 'fundamental',
            'index_id': 'all',
        }

        for smlId in self.feed():
            smlId = list(smlId)
            smlId = ''.join(smlId)
            smlId.replace("'", "")
            smlId.replace(",", "")
            print(smlId)
            params['smlID'] = smlId
            params_str = urllib.parse.urlencode(params)
            yield scrapy.FormRequest(url=self.url + params_str, callback=self.parse, headers=headers, cb_kwargs={'smlId': smlId})

    def parse(self, response, smlId):
        item = CompanyItem()
        for data in response.xpath("//table[@id='fundamental']/tbody/tr"):
            item['name'] = data.xpath('./td[2]/span').attrib['data-name']
            item['currId'] = data.xpath('./td[2]/span').attrib['data-id']
            item['short_name'] = data.xpath('./td[2]/a/text()').get()
            item['avg_volume'] = data.xpath('./td[3]/text()').get()
            item['market_cap'] = data.xpath('./td[4]/text()').get()
            item['revenue'] = data.xpath('./td[5]/text()').get()
            item['p_e_ratio'] = data.xpath('./td[6]/text()').get()
            item['beta'] = data.xpath('./td[7]/text()').get()
            item['smlId'] = smlId

            yield item
