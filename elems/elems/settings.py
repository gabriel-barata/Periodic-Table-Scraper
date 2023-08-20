BOT_NAME = "elems"

SPIDER_MODULES = ["elems.spiders"]
NEWSPIDER_MODULE = "elems.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "elems.pipelines.SaveToMySQL": 300,
    "elems.pipelines.GroupElements": 400
}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
FEED_EXPORT_ENCODING = "utf-8"

# Playwright configuration
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

# MySQL container configurations
MYSQL_HOST = 'localhost'
MYSQL_USER = 'crawler_user'
MYSQL_PASSWORD = 'daniella'
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'periodic_table'