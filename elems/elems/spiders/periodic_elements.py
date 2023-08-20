from scrapy_playwright.page import PageMethod
from elems.items import PeriodicTableItem
from scrapy.loader import ItemLoader
import scrapy

class PeriodicElementsSpider(scrapy.Spider):
    name = "periodic_elements"
    allowed_domains = ["nih.gov"]
    start_urls = ["https://pubchem.ncbi.nlm.nih.gov/ptable/"]

    def start_requests(self):
        yield scrapy.Request(
            self.start_urls[0],
            meta = {
                'playwright': True,
                'playwright_page_methods': [
                    PageMethod("wait_for_selector", 'div.ptable')
                ]
            }
        )

    async def parse(self, response):

        for element in response.css('div.ptable div.element'):

            loader = ItemLoader(item=PeriodicTableItem(), selector = element)

            loader.add_css('symbol', '[data-tooltip="Symbol"]')
            loader.add_css('name', '[data-tooltip="Name"]')
            loader.add_css('atomic_number', '[data-tooltip="Atomic Number"]')
            loader.add_css('atomic_mass', '[data-tooltip*="Atomic Mass"]')
            loader.add_css('chemical_group', '[data-tooltip="Chemical Group Block"]')

            yield loader.load_item()