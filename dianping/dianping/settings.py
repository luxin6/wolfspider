# Scrapy settings for dianping project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'dianping'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['dianping.spiders']
NEWSPIDER_MODULE = 'dianping.spiders'
DEFAULT_ITEM_CLASS = 'dianping.items.DianpingShopItem'
#USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
USER_AGENT = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'
LOG_LEVEL = 'DEBUG'

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = '/tmp/scrapy/cache/'
DOWNLOADER_MIDDLEWARES = [ 
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware',
    'dianping.middlewares.IgnoreVisitedUrlMiddleware',
    'dianping.middlewares.PeepMiddleware',
]
DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 20
RANDOMIZE_DOWNLOAD_DELAY = True
# LOG_FILE = 'crawl.log'
ITEM_PIPELINES = ['dianping.pipelines.DianpingPipeline']