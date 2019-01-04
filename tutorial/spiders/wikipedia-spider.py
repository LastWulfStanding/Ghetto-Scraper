
# What do I want to do with this spider?
#   I want it to start from one page, then terminate
#   to another page that has the given topic.


import scrapy

class WikipediaSpider(scrapy.Spider):
    # Name of the quotes, names of the spiders have to be unique to one another
    name = "wikipedia"
    
    dest = None
    
    def start_requests(self):
        Global dest
        url = 'https://en.wikipedia.org/wiki/Main_Page'
        dest = getattr(self, 'dest', None)
        if dest is not None:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        global dest
        d_links = dict()
        for bg in response.css('td.MainPageBG'):
            for l in bg.css("div a"):
                name = l.css('a::text').extract_first()
                href = l.css('a::attr(href)').extract_first()
                d_links[name] = href
        yield d_links
        
    #def dest_selector(self, links):
        #if  links.keys()
        

            
        
        #page = response.url.split("/")[-2]
        #filename = 'wikipedia-%s.html' % page
        #with open(filename, 'wb') as f:
            #f.write(response.body)
        #self.log('Saved file %s' % filename)



