from customtkinter import *
import customtkinter
from petPerfil import Perfil
from petCalendario import Calendario
import tkinter as tk

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.rowconfigure(0, weight= 1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        
        root_width = 1000 
        root_height = 700
        display_width = self.winfo_screenwidth()
        display_height = self.winfo_screenheight()
        left = int(display_width / 2 - root_width / 2)
        top = int(display_height / 2 - root_height / 2)
        self.geometry(f'{root_width}x{root_height}+{left}+{top}')
        self.title("PetPlanner - Vacine seu pet")
        self.iconbitmap('img/logo.ico')
        #self.minsize(1400,900)
        #self.maxsize(1400,900)
        
        self.perfil = Perfil(master=self, fg_color="#9156CD")
        self.perfil.grid(row=0,rowspan=1, column=0,columnspan=1, padx=20, pady=20, sticky="nsew")
                
        self.calendario = Calendario(master=self, fg_color="#9156CD")
        self.calendario.grid(row=0,rowspan=1, column=1,columnspan=1, padx=20, pady=20, sticky="nsew")
        
        
root = App()
root.mainloop()   
        