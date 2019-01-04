
import scrapy

class QuotesSpider(scrapy.Spider):
    # Name of the quotes, names of the spiders have to be unique to one another
    name = "quotes"
    
    def start_requests(self):
        url = 'http://quotes.toscrape.com/'     # The url that the spider starts with
        tag = getattr(self, 'tag', None) 
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # for loop gets every <div class="quote" ...> for information extraction
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),       # Extracts the text inside the <span class="text"> tags
                'author': quote.css('small.author::text').extract_first(),  # Extracts the text inside the <small class="author"> tags 
            }

        for href in response.css('li.next a'):                  # get all the information within the tags <li class="next"><a> one by one
            yield response.follow(href, callback=self.parse)    # response.follow uses the <a>'s href tags automatically

### quotes spider #1
'''
import scrapy

class QuotesSpider(scrapy.Spider):
    # Name of the quotes, names of the spiders have to be unique to one another
    name = "quotes"
    
    # The urls that the spider starts with
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        # for loop gets every <div class="quote" ...> for information extraction
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),       # Extracts the text inside the <span class="text"> tags
                'author': quote.css('small.author::text').extract_first(),  # Extracts the text inside the <small class="author"> tags 
                'tags': quote.css('div.tags a.tag::text').extract(),        # Extracts the text inside the <div class="tags"><a class="tag"> tags
            }

        for href in response.css('li.next a'):                  # get all the information within the tags <li class="next"><a> one by one
            yield response.follow(href, callback=self.parse)    # response.follow uses the <a>'s href tags automatically
        
        
        #next_page = response.css('li.next a::attr(href)').extract_first()   # Extracts the href inside the <li class="next"><a> tags
        #if next_page is not None:
            #yield response.follow(next_page, callback=self.parse())
            #-----#
            #next_page = response.urljoin(next_page)
            #yield scrapy.Request(next_page, callback=self.parse)
'''
        

### quotes spider #0
'''
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

#instanceSpider = QuotesSpider
#instanceSpider.start_requests()
'''

