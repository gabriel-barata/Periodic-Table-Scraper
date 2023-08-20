from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags
import scrapy

class PeriodicTableItem(scrapy.Item):

    symbol = scrapy.Field(
        input_processor = MapCompose(remove_tags, str.strip),
        output_processor = TakeFirst()
    )
    name = scrapy.Field(
        input_processor = MapCompose(remove_tags, str.strip),
        output_processor = TakeFirst()
    )
    atomic_number = scrapy.Field(
        input_processor = MapCompose(remove_tags, str.strip, int),
        outuput_processor = TakeFirst()
    )
    atomic_mass = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip, float),
        outuput_processor=TakeFirst()
    )
    chemical_group = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        outuput_processor=TakeFirst()
    )