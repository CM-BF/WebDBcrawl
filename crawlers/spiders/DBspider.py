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
    count = 0
    urls = []

    # def start_requests(self):
    #     urls = [
    #         "https://research.cs.wisc.edu/dbworld/browse.html",
    #     ]
    #     yield scrapy.Request(url=urls[0], callback=self.parse)
    #     self.file.close()
    #     self.file = open('items.json', 'r')
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parsetext)


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
            url = project.xpath('td[4]/a/@href').extract()[0]
            request = scrapy.Request(url=url, callback=self.parsetext)
            request.meta['item'] = Item
            Item['url'] = url
            Item['deadline'] = project.xpath('td[5]/text()').extract()
            Item['webpage'] = project.xpath('td[6]/text()').extract()
            yield request

    def parsetext(self, response):
        Item = response.meta['item']
        text = ''.join(response.xpath('//text()').extract()).replace('\t', '').replace('\xa0', '').splitlines()
        for i in range(len(text)):
            if text[i] != '':
                text[i] = text[i] + '\n'
        text = ''.join(text)
        Item['content'] = text
        item_json = json.dumps(dict(Item))
        file = open('doc/Mail' + str(self.count) + '.txt', 'w')
        self.count += 1
        file.writelines(item_json)
        file.close()
        print('------------------------')



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