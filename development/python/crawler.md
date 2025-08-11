# Crawler

## Splash

> Render dynamic pages for Scrapy using Splash.

```python
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy_splash import SplashRequest

# Start the scraping process
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(TestScraper)
process.start()

class TestScraper(scrapy.Spider):
    name = 'test'
    custom_settings = {
        'SPLASH_URL': SPLASH_URL,
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware': 725,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
        },
        'SPIDER_MIDDLEWARES': {
            'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
        },
        'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
        'HTTPCACHE_STORAGE': 'scrapy_splash.SplashAwareFSCacheStorage',
        # Disable Splash logger (it attaches to the global logger, which is noisy)
        'LOG_ENABLED': False,
    }

    def start_requests(self):
        yield SplashRequest(
            url=self.start_urls[0],
            callback=self.parse,
            args={'wait': 3}
        )

    def parse(self, response):
        # Example: extract URLs from a list
        for url in response.xpath('//ul[@class="abc"]/li/a[@class="xyz"]/@href').getall():
            # Process each URL as needed
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        # Implement detail page parsing here
        pass
```

