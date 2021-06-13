import scrapy
import json
from InvestData.items import DailyStockItem
from InvestData.settings import LOG_COMPANY, ROOT_FOLDER


class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['investing.com']
    start_url = 'https://www.investing.com/instruments/HistoricalDataAjax'

    # custom_settings = {
    #     'ITEM_PIPELINES': {
    #         'InvestData.pipelines.StockPipeline': 400
    #     }
    # }

    """
    Note:
    Edit only the feed() method to change the spider's input.
    feed() should yield a list of currIds
    """

    def feed(self):
        # Open country list and parse one by one
        with open(ROOT_FOLDER + LOG_COMPANY, 'r') as f:
            lines = f.readlines()

        for line in lines:
            yield json.loads(line)['currId']

    """
    The following methods should not be changed in anyway, unless you know exactly what you are doing.
    """

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        body = {
            'curr_id': '',
            'st_date': '01/01/2017',
            'end_date': '12/31/2020',
            'interval_sec': 'Daily',
            'sort_col': 'date',
            'sort_ord': 'DESC',
            'action': 'historical_data',
        }

        for currId in self.feed():
            body['curr_id'] = currId
            body_str = '&'.join('{}={}'.format(key, value)
                                for key, value in body.items())
            yield scrapy.FormRequest(url=self.start_url, callback=self.parse, headers=headers, formdata=body, cb_kwargs={'currId': currId})

    def parse(self, response, currId):
        item = DailyStockItem()
        for data in response.xpath("//table[@id='curr_table']/tbody/tr"):
            item['date'] = data.xpath('./td[1]').attrib['data-real-value']
            item['price'] = data.xpath('./td[2]').attrib['data-real-value']
            item['open_price'] = data.xpath(
                './td[3]').attrib['data-real-value']
            item['high'] = data.xpath('./td[4]').attrib['data-real-value']
            item['low'] = data.xpath('./td[5]').attrib['data-real-value']
            item['vol'] = data.xpath('./td[6]').attrib['data-real-value']
            item['change'] = data.xpath('./td[7]/text()').get()
            item['currId'] = currId
            yield item
