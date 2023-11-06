from customtkinter import *
import tkinter as tk
from petPerfil import Perfil
from App import App

class Login():
    def __init__(self,permissao=False):
        self.perissao = permissao


    def login(self,win):

        def confirmar():
            nome = entry_name.get()
            key = entry_key.get()
            if entry_name.get() != '' and entry_key.get() != '':
                frame_main.place_forget()
                per = Perfil()
                per.criar_perfil(win)

        set_default_color_theme('green')

        frame_main = CTkFrame(win, width=200, height=250,border_width=2,corner_radius=15)
        frame_main.pack_propagate(False)
        frame_main.grid_propagate(False)
        frame_main.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        frame_main.rowconfigure((0,1,2,3),weight=1)
        frame_main.columnconfigure(0,weight=1)

        label_log = CTkLabel(frame_main,text='Login',width=100,font=('Helverica', 15))


        entry_name = CTkEntry(frame_main,placeholder_text='nome')
        entry_key = CTkEntry(frame_main,placeholder_text='senha',show='*')
        button_entrar = CTkButton(frame_main,text='Entrar',command= confirmar)


        label_log.grid(row=0,column=0)
        entry_name.grid(row=1,column=0)
        entry_key.grid(row=2,column=0)
        button_entrar.grid(row=3,column=0)




if __name__ == '__main__':

    tela_config = App()
    win = CTk()
    tela_config.tela_configs(win)

    lo = Login()
    lo.login(win)

    win.mainloop()