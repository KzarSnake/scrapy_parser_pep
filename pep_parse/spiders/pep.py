import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = (
            response.css('table.pep-zero-table')
            .css('tbody')
            .css('a[href^="pep-"]')
        )
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_detail = response.css('h1.page-title::text').get()
        data = {
            'number': int(pep_detail.split()[1].strip()),
            'name': pep_detail.strip(),
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
