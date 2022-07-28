
# Crawler
### splash
> render dynamic page for scrapy
```py
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
      'LOG_ENABLED': False, // Splash Logger attched to golbal logger, not good
  }

  def start_requests(self):
      yield SplashRequest(
          url=url,
          callback=self.parse,
          args={'wait': 3}
      )

  def parse(self, response):
      for url in response.xpath('//ul[@class="abc"]/li/a[@class="xyz"]/@href').getall():
          // whatever
```
