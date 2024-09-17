import scrapy

#centros = //script[contains(.,,'const ')]/text()


class DrupalSpider(scrapy.Spider):
    name = 'drupal'
    start_urls = ['https://web.arba.gov.ar/atencion']

    def parse(self, response):
        """ yield {
            'title': response.css('h1.page-title::text').extract_first(),
            'version': response.css('h2.page-subtitle::text').extract_first(),
            'description': response.css('div.field-name-body p::text').extract_first(),
            'downloads': response.css('div.field-name-field-downloads-count::text').extract_first(),
            'categories': response.css('div.field-name-field-categories a::text').extract(),
            'tags': response.css('div.field-name-field-tags a::text').extract(),
        } """
        #with open('resultados.html', 'w', encoding='utf-8') as f:
        #    f.write(response.text)
        centros = response.xpath('//script[contains(.,\'const \')]/text()').get()
        yield {
            'centros': centros
        }