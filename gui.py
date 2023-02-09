import customtkinter
from tkinter import *
from PIL import Image
from PIL import ImageTk
import requests
from scraping import Scrapper
import webbrowser



customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")



class SingleProductFrame(customtkinter.CTkFrame):

    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

    def add_data(self,name,prod):
        def open_page():
            webbrowser.open(prod['product_link'])

        if len(prod) > 1:
            self.store_name = customtkinter.CTkLabel(master=self,width=100,height=30,text=f"Store: {name.title()}",fg_color='#E74C3C',corner_radius=10)
            self.store_name.place(relx=0.4,rely=0.3)

            self.store_name_background = customtkinter.CTkLabel(master=self, width=106, height=36,
                                                                text=f"{prod['name'].title()}",
                                                                fg_color='#E74C3C', corner_radius=10, )
            self.store_name_background.place(relx=0.1, rely=0.035)
            self.store_name = customtkinter.CTkLabel(master=self, width=100, height=30, text=f"{prod['name'].title()}",
                                                     fg_color='#ECF0F1', corner_radius=10,)
            self.store_name.place(relx=0.1, rely=0.05)
            self.product_price_label = customtkinter.CTkLabel(master=self,width=100,height=30,text=f"Price: {prod['price']} Lei",fg_color='#E74C3C',corner_radius=10)
            self.product_price_label.place(relx=0.4,rely=0.5)
            self.product_link_button = customtkinter.CTkButton(master=self,text='Product Link',height=30,width=100,fg_color='#E74C3C',corner_radius=10,command=open_page)
            self.product_link_button.place(relx=0.4,rely=0.7)

            self.product_image = customtkinter.CTkImage(Image.open(requests.get(prod['product_image'],stream=True).raw),size=(100,100))
            self.product_label_image = customtkinter.CTkLabel(self,image=self.product_image,width=100,height=100,corner_radius=10,text='')
            self.product_label_image.place(relx=0.1,rely=0.3)









class ResultFrame(customtkinter.CTkFrame):

    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.row = 0


    def create_frame_content(self,products):
        for store in products:
            if None in products[store].values():
                pass
            else:
                self.create_product_label(store, products[store])

    def create_product_label(self,store_name,product):
        self.product_frame = SingleProductFrame(master=self,width=500,height=200,fg_color="white")
        self.product_frame.add_data(store_name,product)
        self.product_frame.grid(row=self.row,column=1,padx=10,pady=10)
        self.row+=1


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("800x640")
        self.title("Price Checker")



        self.search_button = customtkinter.CTkButton(master=self,width=40,height=20,border_width=0,corner_radius=8,text="Search",text_color='white',command=self.generate_results,fg_color='#E74C3C')
        self.search_button.place(relx=0.2,rely=0.5)
        self.search_entry = customtkinter.CTkEntry(master=self,placeholder_text="Enter product name",width=220,height=40,border_width=2,corner_radius=10,fg_color='#ECF0F1',border_color='#E74C3C')
        self.search_entry.place(relx=0.2,rely=0.6)
        self.image = ResultFrame(master=self,width=600,height=800,fg_color="white")
        self.image.place(relx=0.6,rely=0.1)

    def generate_results(self):
        #scrapper_instance = Scrapper()
        #product = self.search_entry.get()
        #result = scrapper_instance.scrape_sites(product)
        #rint(result)
        res = {'emag': {'product_link': 'https://www.emag.ro/telefon-mobil-apple-iphone-14-128gb-5g-midnight-mpuf3rx-a/pd/DR2Y4LMBM/?X-Search-Id=af1c18212eef94c41807&X-Product-Id=101075717&X-Search-Page=1&X-Search-Position=0&X-Section=search&X-MB=0&X-Search-Action=view', 'product_image': 'https://s13emagst.akamaized.net/products/48592/48591192/images/res_749904e2b5777dea6eb322cfb68742a1.jpg?width=720&height=720&hash=A31AEC0C4CD4D28F3C10772C8315D943', 'price': '4.529,99 ', 'name': 'Telefon mobil Apple iPhone 14, 128GB, 5G, Midnight'}, 'flanco': {'product_link': 'https://www.flanco.ro/telefon-mobil-apple-iphone-14-5g-128gb-pur', 'product_image': 'https://www.flanco.ro/media/catalog/product/cache/e53d4628cd85067723e6ea040af871ec/i/p/iphone_14_purple_1.jpg', 'price': '4.599,99 lei', 'name': 'Telefon mobil Apple iPhone 14 5G, 128GB, Purple'}, 'cel': {'product_link': 'https://www.cel.ro/telefon-mobil-apple-iphone-14-5g-dual-sim-6gb-256gb-midnight-pNiEyMjQsNQ-l/', 'product_image': 'https://s1.cel.ro/images/Products/2022/12/16/Telefon-Mobil-Apple-iPhone-14-5G-Dual-SIM-6GB-256GB-Midnight.jpg', 'price': '5107 lei', 'name': 'Telefon Mobil Apple iPhone 14 5G Dual SIM 6GB 256GB Midnight'}, 'altex': {'product_link': 'https://altex.ro/telefon-apple-iphone-14-5g-256gb-blue/cpd/SMTIP142BL/', 'product_image': 'https://lcdn.altex.ro/resize/media/catalog/product/i/p/16fa6a9aef7ffd6209d5fd9338ffa0b1/iphone_14_blue-1_d611427e.jpg', 'price': '4.978', 'name': 'Telefon APPLE iPhone 14 5G, 256GB, Blue'}}



        self.image.create_frame_content(res)










app = App()
app.configure(fg_color='white')
app.resizable(width=True,height=True)
app.mainloop()