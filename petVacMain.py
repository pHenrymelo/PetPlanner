import tkinter as tk
from petTela import Tela
from petCalendario import calendario
from petPerfil import Perfil


#tela
root = tk.Tk()
config_perfil = Tela()
config_perfil.tela_configs(root)

#frame do perfil
perfil = Perfil()
perfil.criar_perfil(root)

#frame do calendario
nextimg = tk.PhotoImage(file='next.png')
pastimg = tk.PhotoImage(file='past.png')
calendario(root,nextimg,pastimg)

#run
root.mainloop()
