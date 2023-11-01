import tkinter as tk
from tkinter import ttk

class Tela():
   
        
    def tela_configs(self,root):
        root.title('PetPlanner - Vacine seu pet')
        root.minsize(700,570)
        root.iconbitmap('img/logo.ico')
        root_width = 1000
        root_height = 700
        display_width = root.winfo_screenwidth()
        display_height = root.winfo_screenheight()

        left = int(display_width / 2 - root_width / 2)
        top = int(display_height / 2 - root_height / 2)
        root.geometry(f'{root_width}x{root_height}+{left}+{top}')

if __name__ == '__main__':
    root = tk.Tk()
    tela = Tela()
    tela.tela_configs(root)
    root.mainloop()