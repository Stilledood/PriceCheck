from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import time



class Scrapper:
    '''Class to create and automate scrpping process'''


    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=self.options, executable_path='chromedriver.exe')


    def scrape_emag(self,product):

        self.driver.get('https://www.emag.ro/')
        search_bar = self.driver.find_element(By.XPATH,'//*[@id="searchboxTrigger"]')
        search_bar.send_keys(product)
        search_button = self.driver.find_element(By.XPATH,'//*[@id="masthead"]/div/div/div[2]/div/form/div[1]/div[2]/button[2]')
        search_button.click()
        products = self.driver.find_elements(By.CLASS_NAME,'card-v2-info')
        best_product = products[0]

        try:
            link = best_product.find_elements(By.TAG_NAME,'a')[0].get_attribute('href')
        except:
            pass

        image_link =  best_product.find_element(By.CLASS_NAME,'w-100').get_attribute('src')
        price = best_product.find_element(By.XPATH,'//*[@id="card_grid"]/div[1]/div/div/div[4]/div[1]/p[2]').text

        return {'product_link':link,
               'product_image':image_link,
               'price' : price}

    def scrape_flanco(self,product):
        self.driver.get('https://www.flanco.ro/')
        search_bar = self.driver.find_element(By.XPATH,'//*[@id="searchingfield"]')
        search_bar.send_keys(product)
        search_bar.send_keys(Keys.ENTER)
        select = Select(self.driver.find_element(By.ID,'sorter'))
        select.select_by_visible_text('Pret Ascendent')

        all_products = self.driver.find_element(By.CLASS_NAME,'category-list-view')
        product_link = all_products.find_element(By.TAG_NAME,'li').find_element(By.CLASS_NAME,'product-item-info').find_element(By.XPATH,'//*[@id="product-item-info_187852"]/a[1]').get_attribute('href')
        self.driver.get(product_link)
        product_image = self.driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/figure[1]/a/img').get_attribute('src')
        product_price = self.driver.find_element(By.XPATH,'//*[@id="faddtocart"]/div[1]/div/div/span[2]/span').text

        return {
            'product_link': product_link,
            'product_image': product_image,
            'price': product_price}
        }


























sc = Scrapper()
sc.scrape_flanco('Apple iPhone 14, 128GB, 5G, Purple')




