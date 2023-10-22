import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk, ImageDraw

def round_image(image_path, label):
    # Carregar a imagem original
    imagem_original = Image.open(image_path)
    resized_image = imagem_original.resize((300,300))

    # Criar uma máscara circular
    mascara = Image.new("L", (resized_image.width, resized_image.height), 0)
    draw = ImageDraw.Draw(mascara)
    draw.ellipse((0, 0, resized_image.width, resized_image.height), fill=255)

    # Aplicar a máscara à imagem original
    imagem_redonda = Image.new("RGBA", (resized_image.width, resized_image.height), (0, 0, 0, 0))
    imagem_redonda.paste(resized_image, mask=mascara)

    # Converter a imagem para o formato suportado pelo Tkinter
    imagem_redonda_tk = ImageTk.PhotoImage(imagem_redonda)

    # Exibir a imagem no label do portraid
    label.config(image=imagem_redonda_tk)
    label.image = imagem_redonda_tk  # Garantir que a referência persista

def perfil(root):
    div = tk.Frame(root,width= 350, height=600, borderwidth=10,relief=tk.RIDGE)
    div.pack_propagate(False)
    div.pack(side='left',fill='y')

    portrait = tk.Label(div, background='#f2762e')
    portrait.pack(pady=10)
    round_image("img/jinx.jpg", portrait)

    frame_status = tk.Frame(div,width= 250,height=200,borderwidth=10,relief=tk.RIDGE)
    frame_status.grid_propagate(False)
    frame_status.pack()

    root.columnconfigure((0,1),weight=1)
    root.rowconfigure((0,1,2,3,4),weight=1)

    label_nome = ttk.Label(frame_status, text='Nome',font=('Helverica', 20), background='#f2913d')
    label_sexo = ttk.Label(frame_status,text='Sexo',font=('Helverica', 20), background='#f2913d')
    label_raca = ttk.Label(frame_status,text='Raça',font=('Helverica', 20), background='#f2913d')
    label_idade = ttk.Label(frame_status,text='Idade',font=('Helverica', 20), background='#f2913d')
    label_peso = ttk.Label(frame_status,text='Peso',font=('Helverica', 20), background='#f2913d')

    label_nome.grid(row=0,column=0,sticky='w')
    label_sexo.grid(row=1,column=0,sticky='w')
    label_raca.grid(row=2,column=0,sticky='w')
    label_idade.grid(row=3,column=0,sticky='w')
    label_peso.grid(row=4,column=0,sticky='w')

    editButton = tk.Button(div, text='Cadastrar Vacinação', font=('Helverica', 10), bg='#f2913d')
    editButton.pack()

    #tema
    style = ThemedStyle(root)
    style.set_theme('clam')



if __name__ == '__main__':

    root = tk.Tk()
    root.title('PetPlanner - Vacine seu pet')
    root.minsize(1000,600)
    #root.iconbitmap('logo.ico')
    root_width = 1000
    root_height = 700
    display_width = root.winfo_screenwidth()
    display_height = root.winfo_screenheight()

    left = int(display_width / 2 - root_width / 2)
    top = int(display_height / 2 - root_height / 2)
    root.geometry(f'{root_width}x{root_height}+{left}+{top}')

    perfil(root)
    root.mainloop()