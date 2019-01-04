 
import scrapy

class TwitchSpider(scrapy.Spider):
    name = "twitch"
    
    start_urls = ['https://www.twitch.tv/directory']

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
    
    
    
