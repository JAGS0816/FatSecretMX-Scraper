from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Food(Item):
    name = Field()
    calories = Field()
    carbs = Field()
    fat = Field()
    protein = Field()
    sodium = Field()

class FatSecretCrawler(CrawlSpider):
    name = "Fat_Secret"
    custom_settings = {
        "FEED_EXPORT_ENCODING": "latin1",
        "USER_AGENT":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        "CLOSESPIDER_PAGECOUNT":900
    }
    
    download_delay = 1
    
    allowed_domains = ["fatsecret.com.mx"]
    
    start_urls = ["https://www.fatsecret.com.mx/calor%C3%ADas-nutrici%C3%B3n/search?q=a"]
    
    def clean_number(self, text):
        """
        Cleans the input text by replacing commas with periods and stripping whitespace.

        Args:
            text (str): The input text to be cleaned.

        Returns:
            str: The cleaned text.
        """
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        translator = str.maketrans(',', '.', ''.join(alphabet))
        cleaned_text = text.translate(translator).strip()
        return cleaned_text

    def parse_items(self, response):
        """
        Parses the nutritional information from the webpage.

        Args:
            response (Response): The response object from the webpage.

        Yields:
            dict: A dictionary containing the extracted nutritional information.
        """
        item = ItemLoader(Food(), response)
        
        # Extract nutrient information
        nutrient_8 = response.xpath('//div[@class="nutrient right tRight"][8]/text()').getall()
        nutrient_6 = response.xpath('//div[@class="nutrient right tRight"][6]/text()').getall()

        # Common code for adding fields to the item
        item.add_xpath("name", "//h1/text()")
        item.add_xpath("calories", '//div[@class="nutrient right tRight"][1]/text()', MapCompose(self.clean_number))
        item.add_xpath("carbs", '//div[@class="nutrient black right tRight"][3]/text()', MapCompose(self.clean_number))
        item.add_xpath("fat", '//div[@class="nutrient black right tRight"][4]/text()', MapCompose(self.clean_number))
        item.add_xpath("protein", '//div[@class="nutrient black right tRight"][2]/text()', MapCompose(self.clean_number))
        
        # Conditional block for adding 'sodio' field
        if not nutrient_8:
            item.add_xpath("sodium", '//div[@class="nutrient right tRight"][3]/text()', MapCompose(self.clean_number))
        elif not nutrient_6:
            item.add_xpath("sodium", '//div[@class="nutrient black right tRight"][6]/text()', MapCompose(self.clean_number))
        else:
            item.add_xpath("sodium", '//div[@class="nutrient right tRight"][8]/text()', MapCompose(self.clean_number))
        
        yield item.load_item()

# Run code
# scrapy runspider Fat_secret_scrapper.py -o Fat_secret_nut_values.csv
