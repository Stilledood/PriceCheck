import customtkinter
from tkinter import *
from PIL import Image
from PIL import ImageTk
import requests
from scraping import Scrapper




customtkinter.set_appearance_mode("dark")

class SearchFrame(customtkinter.CTkFrame):

    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.label = customtkinter.CTkLabel(self,text='Search Products',text_color='white')
        self.label.grid(row=0,column=0,padx=120,pady=200)

class SingleProductFrame(customtkinter.CTkFrame):

    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

    def add_data(self,name,prod):
        if len(prod) > 1:
            self.store_name = customtkinter.CTkButton(text=name,master=self,width=70,height=25,border_width=0,corner_radius=10)
            self.store_name.place(relx=0.1,rely=0.1)
            self.product_image = customtkinter.CTkImage(Image.open(requests.get(prod['product_image'],stream=True).raw))
            self.product_label_image = customtkinter.CTkLabel(self,image=self.product_image,width=100,height=100,corner_radius=10)
            self.product_label_image.place(relx=0.3,rely=0.1)
        




class ResultFrame(customtkinter.CTkFrame):

    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.row = 0


    def create_frame_content(self,products):
        for store in products:
            self.create_product_label(store, products[store],)

    def create_product_label(self,store_name,product):
        self.product_frame = SingleProductFrame(master=self)
        self.product_frame.add_data(store_name,product)
        self.product_frame.grid(row=self.row,column=1,padx=10,pady=10)
        self.row+=1


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("800x640")
        self.title("Price Checker")



        self.search_button = customtkinter.CTkButton(master=self,width=40,height=20,border_width=0,corner_radius=8,text="Search",text_color='white',command=self.generate_results)
        self.search_button.place(relx=0.7,rely=0.5)
        self.search_entry = customtkinter.CTkEntry(master=self,placeholder_text="Enter product name",width=220,height=40,border_width=2,corner_radius=10,fg_color='light blue')
        self.search_entry.place(relx=0.6,rely=0.6)

        self.progress_bar = customtkinter.CTkProgressBar(master=self)
        self.progress_bar.place(relx=0.7,rely=0.5)
        self.image = ResultFrame(master=self,width=500,height=400,fg_color="light grey")
        self.image.grid(row=1,column=1,padx=10,pady=20)

    def generate_results(self):
        scrapper_instance = Scrapper()
        product = self.search_entry.get()
        result = scrapper_instance.scrape_sites(product)
        self.image.create_frame_content(result)










app = App()
app.configure(fg_color=("#fab1a0","#e17055"))
app.resizable(width=True,height=True)
app.mainloop()