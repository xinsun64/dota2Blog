# -*- coding: utf-8 -*-

# Scrapy settings for dota2Blog project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dota2Blog'

SPIDER_MODULES = ['dota2Blog.spiders']
NEWSPIDER_MODULE = 'dota2Blog.spiders'

OOKIES_ENABLED = False

ITEM_PIPELINES = {
    'dota2Blog.pipelines.Dota2BlogPipeline':300
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dota2Blog (+http://www.yourdomain.com)'
