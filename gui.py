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

    def __init__(self,master,result = None,**kwargs):
        super().__init__(master,**kwargs)
        if result:
            image =Image.open( requests.get('https://s13emagst.akamaized.net/products/48592/48591194/images/res_386d8b602076b952c56b1d3411c2e473.jpg?width=720&height=720&hash=0CAE43D3D9DA08F8D44D298826D7C9CF',stream=True).raw)
            ph = ImageTk.PhotoImage(image)
            self.immage = customtkinter.CTkImage(light_image=image,size=(100,100))
            label = customtkinter.CTkLabel(image=self.immage,master=self,fg_color='white',text='')
            label.place(relx=0,rely=0)
        else:
            pass



        




class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("800x640")
        self.title("Price Checker")

        self.search_frame = SearchFrame(master=self)
        self.search_frame.grid(row=0,column=0,padx=20,pady=20,sticky='nsew')
        self.search_button = customtkinter.CTkButton(master=self,width=40,height=20,border_width=0,corner_radius=8,text="Search",text_color='white',command=self.generate_results)
        self.search_button.place(relx=0.5,rely=0.5)
        self.search_entry = customtkinter.CTkEntry(master=self,placeholder_text="Enter product name",width=220,height=40,border_width=2,corner_radius=10,fg_color='light blue')
        self.search_entry.place(relx=0.6,rely=0.6)

        self.progress_bar = customtkinter.CTkProgressBar(master=self)
        self.progress_bar.place(relx=0.7,rely=0.5)
        self.image = ResultFrame(master=self,width=100,height=100,fg_color="white")
        self.image.grid(row=1,column=0,padx=0,pady=20)

    def generate_results(self):
        scrapper_instance = Scrapper()
        product = self.search_entry.get()
        result = scrapper_instance.scrape_sites(product)
        result_frame = ResultFrame(result)










app = App()
app.configure(fg_color=("#fab1a0","#e17055"))
app.resizable(width=True,height=True)
app.mainloop()