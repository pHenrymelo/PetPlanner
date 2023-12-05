from customtkinter import *
import tkinter as tk



class Cadastro(tk.Frame):
    def __init__(self,win):

        def voltar():           
            frame_main.place_forget()
            from AppMain import App
            login = App()

        set_default_color_theme('green')

        frame_main = CTkFrame(win, width=200, height=250,border_width=2,corner_radius=15)
        frame_main.pack_propagate(False)
        frame_main.grid_propagate(False)
        frame_main.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        frame_main.rowconfigure((0,1,2,3,4),weight=1)
        frame_main.columnconfigure(0,weight=1)

        label_log = CTkLabel(frame_main,text='Cadastro',width=100,font=('Helverica', 15))


        entry_name = CTkEntry(frame_main,placeholder_text='nome')
        entry_key = CTkEntry(frame_main,placeholder_text='senha',show='*')
        button_entrar = CTkButton(frame_main,text='Salvar')
        button_cadastro = CTkButton(frame_main,text='Voltar', command=voltar)


        label_log.grid(row=0,column=0)
        entry_name.grid(row=1,column=0)
        entry_key.grid(row=2,column=0)
        button_entrar.grid(row=3,column=0)
        button_cadastro.grid(row=4,column=0)



if __name__ == '__main__':


    win = CTk()


    lo = Cadastro(win)
    win.mainloop()