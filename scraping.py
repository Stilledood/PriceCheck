from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



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

    

















sc = Scrapper()
sc.scrape_flanco('Apple iPhone 14, 128GB, 5G, Purple')




