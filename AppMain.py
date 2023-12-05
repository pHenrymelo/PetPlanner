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
        
        #configurações da tela
        root_width = 1000
        root_height = 700
        display_width = self.winfo_screenwidth()
        display_height = self.winfo_screenheight()
        left = int(display_width / 2 - root_width / 2)
        top = int(display_height / 2 - root_height / 2)
        self.geometry(f'{root_width}x{root_height}+{left}+{top}')
        self.title("PetPlanner - Vacine seu pet")
        #self.iconbitmap('img/logo.ico')
        #self.minsize(1400,900)
        #self.maxsize(1400,900)
        
        # Inicio parte de Login
        def confirmar():
            nome = entry_name.get()
            key = entry_key.get()
            if entry_name.get() != '' and entry_key.get() != '':
                frame_main.place_forget()

                self.perfil = Perfil(master=self, fg_color="#9156CD")
                self.perfil.grid(row=0,rowspan=1, column=0,columnspan=1, padx=20, pady=20, sticky="nsew")
                        
                self.calendario = Calendario(master=self, fg_color="#9156CD")
                self.calendario.grid(row=0,rowspan=1, column=1,columnspan=1, padx=20, pady=20, sticky="nsew")
        
        def cadastrar():
            from petTelaCadastro import Cadastro
            frame_main.place_forget()
            cadastro = Cadastro(self)
                        

        set_default_color_theme('green')

        frame_main = CTkFrame(self, width=200, height=250,border_width=2,corner_radius=15)
        frame_main.pack_propagate(False)
        frame_main.grid_propagate(False)
        frame_main.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        frame_main.rowconfigure((0,1,2,3,4),weight=1)
        frame_main.columnconfigure(0,weight=1)

        label_log = CTkLabel(frame_main,text='Login',width=100,font=('Helverica', 15))


        entry_name = CTkEntry(frame_main,placeholder_text='nome')
        entry_key = CTkEntry(frame_main,placeholder_text='senha',show='*')
        button_entrar = CTkButton(frame_main,text='Entrar',command= confirmar)
        button_cadastro = CTkButton(frame_main,text='Cadastrar',command= cadastrar)


        label_log.grid(row=0,column=0)
        entry_name.grid(row=1,column=0)
        entry_key.grid(row=2,column=0)
        button_entrar.grid(row=3,column=0)
        button_cadastro.grid(row=4,column=0)
        #fim Login

        
if __name__ == '__main__':       
    root = App()


    root.mainloop()   
            