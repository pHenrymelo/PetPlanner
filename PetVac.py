import tkinter as tk, calendar, datetime
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk, ImageDraw

def create_label(parent, text, row, column):
    label = tk.Label(parent, background='#f2913d', text=text, font=("Helvetica", 25), width=1, height=1)
    label.grid(column=column, row=row, columnspan=1, rowspan=1, sticky='nsew', padx=5, pady=5)
    return label
 
def show_calendar(year, month):
    cal_text.config(text=calendar.month(year, month))

def next_month():
    global year, month
    month += 1
    if month > 12:
        year += 1
        month = 1
    show_calendar(year, month)

def prev_month():
    global year, month
    month -= 1
    if month < 1:
        year -= 1
        month = 12
    show_calendar(year, month)

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


data_atual = datetime.datetime.now()
ano_atual = data_atual.year
mes_atual = data_atual.month
primeiro_dia_do_mes = datetime.date(data_atual.year, data_atual.month, 1)
primeiro_dia_do_mes_diasem =  primeiro_dia_do_mes.weekday()
dias = ['Seg','Ter','Qua','Qui','Sex','Sab','Dom']
primeiro_dia = dias[primeiro_dia_do_mes_diasem]

#window
root = tk.Tk()
root.title('PetPlanner - Vacine seu pet')
root.configure(bg='#f0f2a0')
root.minsize(1000,600)
#root.iconbitmap('logo.ico')
root_width = 1500
root_height = 900
display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

left = int(display_width / 2 - root_width / 2)
top = int(display_height / 2 - root_height / 2)
root.geometry(f'{root_width}x{root_height}+{left}+{top}')


#frame do perfil
div = tk.Frame(root, padx=10, pady=10, background='#f2762e')
div.grid(row=0, column=0, sticky='nsew', padx=10, pady=10, rowspan=2)

portrait = tk.Label(div, padx=10, pady=10, background='#f2762e')
portrait.pack(pady= 25)
round_image("jinx.jpg", portrait)

label = tk.Label(div, padx=10, pady=10, background='#f2913d', text='Nome do Pet', anchor='center', font=('Helverica', 20))
label.pack()

editButton = tk.Button(div,padx=10, pady=10, width=15, text='Cadastrar Vacinação', font=('Helverica', 10), bg='#f2913d')
editButton.pack(pady= 10)

#calendario linhas e colunas
year, month = ano_atual, mes_atual

root.columnconfigure(0, weight= 1)
root.columnconfigure(1, weight= 4)
root.rowconfigure(0, weight=1)

#frame do calendario

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembo',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

schedule = tk.Frame(root, padx=10, pady=10, background='#f2762e')
schedule.grid(row=0, column=1, sticky='nsew', padx=10, pady=10, rowspan=1)
#cor de fundo #f2762e cor das labels #f2913d
for i in range(7):
    schedule.columnconfigure(i, weight=1)
for j in range(7):
    schedule.rowconfigure(j, weight=1)


ma = tk.Label(schedule, background='#f2913d', text=f'{meses[month]}, {ano_atual}', font=("Helvetica", 35))
ma.grid(column=0, row=0, columnspan=7, rowspan=1, sticky='nsew', padx=5, pady= 5)

dias_da_semana = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
for i, dia in enumerate(dias_da_semana):
    create_label(schedule, dia, row=1, column=i)
    
dias_no_mes = 31  
for i in range(0, dias_no_mes):
    create_label(schedule, str(i+1), row=(i // 7) + 2, column=i % 7)


'''prev_button = tk.Button(schedule, text="Mês Anterior", command=prev_month, bg='#836FFF')
prev_button.grid(row=0, column=1, sticky= 'w')

next_button = tk.Button(schedule, text="Próximo Mês", command=next_month, bg='#836FFF')
next_button.grid(row=0, column=5, sticky= 'e')'''

#tema
style = ThemedStyle(root)
style.set_theme('clam')

#run
root.mainloop()
