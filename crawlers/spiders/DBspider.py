from crawlers.items import CrawlersItem
import scrapy
from scrapy.loader import ItemLoader
import json

class DBSpider(scrapy.Spider):
    name = "DBSpider"
    # allowed_domains = ["huxiu.com"]
    start_urls = [
        "https://research.cs.wisc.edu/dbworld/browse.html"
    ]
    file= open('items.json', 'w')


    def process_item(self, item):
        item_json = json.dumps(dict(item)) + '\n'
        self.file.writelines(item_json)
        print('------------------------')
        return item

    def parse(self, response):
        table = response.xpath('//table')
        projects = table.xpath('//tbody/tr')
        # print(projects)
        for project in projects:
            # print(project.xpath('td'))
            # pass
            Item = CrawlersItem()
            Item['sent'] = project.xpath('td[1]/text()').extract()
            Item['type'] = project.xpath('td[2]/text()').extract()
            Item['author'] = project.xpath('td[3]/text()').extract()
            Item['subject'] = project.xpath('td[4]//text()').extract()
            Item['deadline'] = project.xpath('td[5]/text()').extract()
            Item['webpage'] = project.xpath('td[6]/text()').extract()
            yield self.process_item(Item)
        self.file.close()




        # filename = "DB.txt"
        # with open(filename, "w") as f:
        #     f.writelines(table)
        # for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
        #     item = CrawlersItem()
        #     item['title'] = sel.xpath('h3/a/text()')[0].extract()
        #     item['link'] = sel.xpath('h3/a/@href')[0].extract()
        #     url = response.urljoin(item['link'])
        #     item['desc'] = sel.xpath('div[@class="mob-sub"]/text()')[0].extract()
        #     print(item['title'],item['link'],item['desc'])