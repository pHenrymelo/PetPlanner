import tkinter as tk
from petPerfil import perfil
from petCalendario import mostrar_calendario
from petTela import tela_configs

#tela
root = tk.Tk()
tela_configs(root)

#frame do perfil
perfil(root)

#frame do calendario
month = 10
year = 2023
mostrar_calendario(year,month,root)

#run
root.mainloop()
