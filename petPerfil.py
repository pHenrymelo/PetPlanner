import customtkinter
from PIL import Image,ImageTk, ImageDraw

class Perfil(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_propagate(True)
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1,2), weight=1)
        img = customtkinter.CTkFrame(master=self)
        img.pack_propagate(False)
        img.pack(side='left',fill='y',padx=2)
        img.grid(row= 0, column = 0, pady = 15)
        portrait = customtkinter.CTkImage(light_image=Image.open("img/jinx.jpg"),dark_image=Image.open("img/jinx.jpg"),size=(250, 250))
        self.image = customtkinter.CTkLabel(img, image=portrait, text="", fg_color="#fff")
        self.image.grid(row=0, column=0)
        

        infos = customtkinter.CTkFrame(master=self, width=250, height=200, fg_color="#402160")
        infos.grid(row= 1, column = 0, sticky='ns')
        infos.grid_propagate(False)
        infos.columnconfigure((0,1),weight=1)
        infos.rowconfigure((0,1,2,3,4),weight=1)
        
        

        label_nome = customtkinter.CTkLabel(infos, text='Nome',font=('Helverica', 18))
        entry_nome = customtkinter.CTkLabel(infos,text='Pepito',justify='right')

        label_sexo = customtkinter.CTkLabel(infos,text='Sexo',font=('Helverica', 18))
        entry_sexo = customtkinter.CTkLabel(infos,text='Macho',)

        label_raca = customtkinter.CTkLabel(infos,text='Raça',font=('Helverica', 18))
        entry_raca = customtkinter.CTkLabel(infos,text='Gato preto')

        label_idade = customtkinter.CTkLabel(infos,text='Idade',font=('Helverica', 18))
        entry_idade = customtkinter.CTkLabel(infos,text='3')

        label_peso = customtkinter.CTkLabel(infos,text='Peso',font=('Helverica', 18))
        entry_peso = customtkinter.CTkLabel(infos,text='4')

        label_nome.grid(row=0,column=0,sticky='w', padx = 15)
        entry_nome.grid(row=0,column=1,sticky='w')
        label_sexo.grid(row=1,column=0,sticky='w', padx = 15)
        entry_sexo.grid(row=1,column=1,sticky='w')
        label_raca.grid(row=2,column=0,sticky='w', padx = 15)
        entry_raca.grid(row=2,column=1,sticky='w')
        label_idade.grid(row=3,column=0,sticky='w', padx = 15)
        entry_idade.grid(row=3,column=1,sticky='w')
        label_peso.grid(row=4,column=0,sticky='w', padx = 15)
        entry_peso.grid(row=4,column=1,sticky='w')
        
        botão = customtkinter.CTkButton(self, text="Agendar", command='', fg_color="#402160", width=200, height=50, font=('Helverica', 18))
        botão.grid(row=2, column=0)
