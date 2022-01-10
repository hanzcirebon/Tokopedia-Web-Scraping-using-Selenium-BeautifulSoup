import time
from selenium import webdriver
import pandas as pd


class PageScraper(webdriver.Chrome):
    def __init__(self, url=""):
        self.web_url = url
        self.web_element = None
        self.df = None
        super(PageScraper, self).__init__()

    # Scroll to the botom of the page
    def scroll(self):
        # Time wait before scrolling
        SCROLL_PAUSE_TIME = 2

        # Get scroll height
        last_height = self.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break

            last_height = new_height

    # scrape content element
    def get_content_element(self):
        class_ = "css-974ipl"
        self.web_element = self.find_elements_by_xpath(f'div[@class="{class_}"]')

    # scrape title
    # return string of title
    def get_title(self, webElement):
        class_ = "css-12fc2sy"
        info = webElement.find_elements_by_xpath(f'//a[@class="{class_}"]').text()

        return info
        
    # scrape price
    # return int of price
    def get_price(self, webElement):
        class_ = "css-a94u6c"
        info = webElement.find_elements_by_xpath(f'//div[@class="{class_}"]').text()
        
        return info
    
    # scrape sold
    # return string of total sold
    def get_sold(self, webElement):
        class_ = "css-1agvax3"
        info = webElement.find_elements_by_xpath(f'//span[@class="{class_}"]').text()
        
        return info

    # scrape rating
    # return float of rating
    def get_rating(self, webElement):
        class_ = "css-1ffszw6"
        info = webElement.find_elements_by_xpath(f'//span[@class="{class_}"]').text()
        
        return info
    
    # scrape discount
    # return int of discount
    def get_discount(self, webElement):
        id_ = "spnSRPProdDisc"
        info = webElement.find_elements_by_xpath(f'//div[@data-test-id="{id_}"]').text()
        
        return info
    
    # scrape discount price
    # return int of discounted price
    def get_discounted_price(self, webElement):
        id_ = "lblProductSlashPrice"
        info = webElement.find_elements_by_xpath(f'//div[@class="{id_}"]').text()
        
        return info
        
    # scrape price
    # return array of store information
    def get_store_info(self, webElement):
        class_ = "css-1rn0irl"
        info = webElement.find_elements_by_xpath(f'//div[@class="{class_}"]').text().split('\n')
        
        return info
        
    # scrape item link
    # return a url to the item
    def get_item_link(self, webElement):
        class_ = "pcv3__info-content css-gwkf0u"
        info = webElement.find_elements_by_xpath(f'//a[@class="{class_}"]').get_attribute('href')
    
        return info

    # Scrape all the data available within the page
    # return data in pandas form
    def get_data(self):
        self.get_content_element()

        # loop for each product
        for product in self.web_element:
            break
        
        return None

    # Load page
    def get_page(self):
        self.get(self.web_url)
        self.scroll()
        self.get_data()

    # get page source
    def get_source(self):
        return self.page_source 

    # Close the browser
    def close_page(self):
        self.close()