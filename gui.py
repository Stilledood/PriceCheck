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

class ResultFrame(customtkinter.CTkFrame):

    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.height = 0.1

    def create_frame_content(self,products):
        for store in products:
            self.create_product_label(store, products[store], self.height)

    def create_product_label(self,store_name,product,height):
        self.store_name = customtkinter.CTkButton(master=self,text=store_name,width=50,height=25,border_width=0,corner_radius=10)
        self.store_name.place(relx=0.2,rely=self.height)
        self.height += 0.1
















        




class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("800x640")
        self.title("Price Checker")



        self.search_button = customtkinter.CTkButton(master=self,width=40,height=20,border_width=0,corner_radius=8,text="Search",text_color='white',command=self.generate_results)
        self.search_button.place(relx=0.5,rely=0.5)
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