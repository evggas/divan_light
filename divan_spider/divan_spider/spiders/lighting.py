import scrapy

class DivanSpider(scrapy.Spider):
    name = "divan_spider"
    allowed_domains = ["divan.ru"]
    start_urls = ['https://www.divan.ru/category/svet']

    def parse(self, response):
        products = response.css("div._Ud0k")

        for product in products:
            yield {
             "name" : product.css("div.lsooF span::text").get(), # ищем название класса для блока в коде странице на сайте, а потом тег
             "price": product.css("div.pY3d2 span::text").get(),
             "url": product.css("a").attrib ["href"]
            }

        # Пагинация, если есть ссылки на следующие страницы
        next_page = response.css('a.pagination-next::attr(href)').get()
        if next_page is not None:
           yield response.follow(next_page, self.parse)
#scrapy crawl divan_spider -o lights.csv
