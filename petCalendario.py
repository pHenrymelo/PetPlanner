import tkinter as tk
from tkinter import ttk
import calendar
import datetime
from ttkthemes import ThemedStyle

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
selected_day = None


def calendario(windows,nextimg,pastimg):


    def change_month(val):
        global month
        global year
        month += val
        if month < 1:
            month = 12
            year -= 1
        elif month > 12:
            month = 1
            year += 1
        label_h.config(text=months_pt[month-1])
        year_label.config(text=year)
        update_days()

    def select_day(button):
        global selected_day
        if selected_day:
            selected_day.config(bg='white')
        selected_day = button
        selected_day.config(bg='lightblue')

    def update_days():
        # Obter o número de dias no mês e o dia da semana do primeiro dia do mês
        num_dias = calendar.monthrange(year, month)[1]
        dia_semana = calendar.weekday(year, month, 1)

        # Ajustar para que domingo seja 0, segunda-feira seja 1, etc.
        dia_semana = (dia_semana + 1) % 7

        # Atualizar os números dos dias na interface
        num = 1
        for x in range(3, 9):
            for y in range(7):
                if x == 3 and y < dia_semana:
                    label_num = tk.Label(frame, text='', width=5, height=2, borderwidth=1, relief="solid", background='gray')
                elif num == day and month == datetime.datetime.now().month and year == datetime.datetime.now().year:
                    button = tk.Button(frame, text=num, width=5, height=2, borderwidth=1, relief="solid", background='lightblue')
                    button.config(command=lambda btn=button: select_day(btn))
                    label_num = button
                    num += 1
                elif num <= num_dias:
                    button = tk.Button(frame, text=num, width=5, height=2, borderwidth=1, relief="solid", background='white')
                    button.config(command=lambda btn=button: select_day(btn))
                    label_num = button
                    num += 1
                else:
                    label_num = tk.Label(frame, text='', width=5, height=2, borderwidth=1, relief="solid", background='gray')

                label_num.grid(row=x, column=y)


    year_var = tk.IntVar()
    year_var.set(year)
    month_var = tk.IntVar()
    month_var.set(month)

    #main_frame = tk.Frame(windows,relief=tk.RIDGE,background='black')
    #main_frame.pack(expand=True,fill='both')


    frame = ttk.Frame(windows, width=400, height=400, relief=tk.RIDGE)
    frame.grid_propagate(False)
    frame.pack_propagate(False)
    frame.pack(expand=True,fill='both')

    
    frame.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
    frame.rowconfigure(0, weight=0)
    frame.rowconfigure((1, 2, 3, 4, 5, 6, 7, 8), weight=1)

    months_pt = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    day_names = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']

    year_label = tk.Label(frame, text=year,font=('Helverica', 14))
    year_label.grid(row=0,columnspan=7,sticky='nesw',padx=1,pady=1)
    label_h = tk.Label(frame, text=months_pt[month-1],font=('Helverica', 14))
    label_h.grid(row=1, columnspan=7, sticky='nesw',padx=1)


    prev_button = tk.Button(frame, image=pastimg, borderwidth=0, command=lambda: change_month(-1))
    prev_button.grid(row=1, column=0)

    next_button = tk.Button(frame, image=nextimg, borderwidth=0, command=lambda: change_month(1))
    next_button.grid(row=1, column=6)

    col = 0
    for dia in day_names:
        label_dia = tk.Label(frame, text=dia, width=5, height=2, borderwidth=1, relief="solid", background='lightgray')
        label_dia.grid(row=2, column=col)
        col += 1

    update_days()

    style = ThemedStyle(windows)
    style.set_theme('clam')


if __name__ == '__main__':
    
    windows = tk.Tk()
    windows.title('Tabelas')
    windows.geometry('600x600')

    nextimg = tk.PhotoImage(file='next.png')
    pastimg = tk.PhotoImage(file='past.png')
    calendario(windows,nextimg,pastimg)

    windows.mainloop()
    


