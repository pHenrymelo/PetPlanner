import customtkinter
from PIL import Image,ImageTk, ImageDraw

class Perfil(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_propagate(True)
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1), weight=1)
        
        self.create_rounded_image()

        infos = customtkinter.CTkFrame(master=self, width=250, height=200, fg_color="#402160")
        infos.grid(row= 1, column = 0, sticky='ns', pady= 20)
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
        

    def create_rounded_image(self):
        # Load the image using Pillow
        image = Image.open("img/jinx.jpg")
        resized_image = image.resize((250, 250))
        
        # Create a round mask
        width, height = resized_image.size
        mask = Image.new("L", (width, height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, width, height), fill=255)

        # Apply the mask to the resized image
        rounded_image = Image.new("RGBA", (width, height))
        rounded_image.paste(resized_image, (0, 0), mask)

        # Convert the rounded image into a PhotoImage for display in Tkinter
        rounded_image_tk = ImageTk.PhotoImage(rounded_image)

        # Create a label to display the rounded image
        label = customtkinter.CTkLabel(self, image=rounded_image_tk, text="")
        label.image = rounded_image_tk  # Maintain a reference to prevent garbage collection
        label.grid(row=0, column=0, padx=10, pady=10)
        
