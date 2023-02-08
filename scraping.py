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
        try:
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
            name  =  best_product.find_element(By.CSS_SELECTOR,'#card_grid > div:nth-child(1) > div > div > div.card-v2-info > div > h2 > a').text



            return {'product_link':link,
                   'product_image':image_link,
                   'price' : price[:-3],
                    'name':name}
        except:
            return {"emag":"No results"}

    def scrape_flanco(self,product):
        try:
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
            product_price = self.driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/span/span').text
            product_name = self.driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/div/h1/span').text


            return {
                'product_link': product_link,
                'product_image': product_image,
                'price': product_price,
                'name': product_name,
            }
        except:
            return {"flanco":"No results"}


    def scrape_altex(self,product):
        try:
            self.driver.get('https://altex.ro/cauta/?q='+"%20".join([x for x in product.split() if len(x) > 0]))
            best_product = self.driver.find_elements(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div[2]/ul[2]')[0]
            product_link = best_product.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div[2]/ul[2]/li[1]/a').get_attribute('href')
            product_image = best_product.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div[2]/ul[2]/li[1]/a/div[1]/img').get_attribute('src')
            product_price = best_product.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div[2]/ul[2]/li[1]/a/div[4]/div/div[2]/span/span[1]').text
            product_name = best_product.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div[2]/ul[2]/li[1]/a/h2').text

            return {
                'product_link':product_link,
                'product_image':product_image,
                'price':product_price,
                'name':product_name,
            }
        except:
            return {"altex":"no results"}

    def scrape_cel(self,product):
        try:
            self.driver.get('https://www.cel.ro/')
            search_bar = self.driver.find_element(By.ID,"keyword")
            search_bar.send_keys(product)
            search_bar.send_keys(Keys.ENTER)
            best_products = []
            for i in range(1,5):
                best_products.append(self.driver.find_element(By.CSS_SELECTOR,f"#bodycode > div.listingPageWrapper > div.listingWrapper > div.productlisting > div:nth-child({i})"))
            best_item_price = None
            best_item_link = None
            best_item_image = None
            best_item_name = None
            for element in best_products:
                product_name = element.find_element(By.CLASS_NAME,"productTitle").text
                corect_product = True if all(x in product_name for x in product.split()) else False
                if corect_product:
                    product_price =int( element.find_element(By.CLASS_NAME,"pret_n").text[:-3])
                    product_link = element.find_element(By.TAG_NAME,"a").get_attribute("href")
                    product_image = element.find_element(By.TAG_NAME,"img").get_attribute("src")
                    if best_item_price is None:
                        best_item_price = product_price
                        best_item_image = product_image
                        best_item_link = product_link
                        best_item_name = product_name
                    elif product_price < best_item_price:
                        best_item_price = product_price
                        best_item_image = product_image
                        best_item_link = product_link
                        best_item_name = product_name

            return {
                'product_link':best_item_link,
                'product_image':best_item_image,
                'price':best_item_price,
                'name':best_item_name
            }
        except:
            return {"cel":"No results"}

    def scrape_sites(self,product):
        return {
            "emag":self.scrape_emag(product),
            "flanco":self.scrape_flanco(product),
            "cel": self.scrape_cel(product),
            "altex":self.scrape_altex(product)
        }











































