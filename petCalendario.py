import calendar
import datetime
import customtkinter as ctk
import tkinter as tk
from typing import Optional, Tuple, Union
from PIL import Image


class Calendario(ctk.CTkFrame):
    def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: Union[int, str, None] = None, border_width: Union[int, str, None] = None, bg_color: Union[str, Tuple[str, str]] = "transparent", fg_color: Union[str, Tuple[str, str], None] = None, border_color: Union[str, Tuple[str, str], None] = None, background_corner_colors: Union[Tuple[str, Tuple[str, str]], None] = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.year = datetime.datetime.now().year
        self.month = datetime.datetime.now().month
        self.day = datetime.datetime.now().day
        self.selected_day = None
        
        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)  
        self.rowconfigure(2, weight=15)          

        self.frame = ctk.CTkFrame(self, fg_color='#9156CD')  # Criar um Frame dentro do Calendario
        self.frame.grid(column=0, row=2, sticky='nsew', columnspan=3, padx=20, pady=20)
        
        self.frame.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure((1, 2, 3, 4, 5, 6, 7, 8), weight=1)

        # Substituir months_pt por uma lista válida de nomes dos meses em português
        self.months_pt = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        self.day_names = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']
        
        prev_button = ctk.CTkButton(self, command=lambda: self.change_month(-1), fg_color='#402160',font=('Helverica', 15), width=30, height=55, corner_radius=120, text="<")
        prev_button.grid(row=1, column=0)

        next_button = ctk.CTkButton(self, command=lambda: self.change_month(1),fg_color='#402160',font=('Helverica', 15),width=30, height=55,corner_radius=120, text=">")
        next_button.grid(row=1, column=2)

        col = 0
        for dia in self.day_names:
            label_dia = ctk.CTkLabel(self.frame, text=dia, width=50, height=50, fg_color='#402160', corner_radius=10,font=('Helverica', 20))
            label_dia.grid(row=2, column=col, sticky='nsew', padx=5, pady=5)
            col += 1
        
        year_label = ctk.CTkLabel(self, text=self.year, font=('Helverica', 24))
        year_label.grid(column=1, row=0, pady=15)
        label_h = ctk.CTkLabel(self, text=self.months_pt[self.month - 1], font=('Helverica', 24), fg_color='#402160', corner_radius=25)
        label_h.grid(column=1, row=1, pady=5 , sticky="nsew")

        self.update_days()

    def change_month(self, val):
        self.month += val
        if self.month < 1:
            self.month = 12
            self.year -= 1
        elif self.month > 12:
            self.month = 1
            self.year += 1
        self.label_h.configure(text=self.months_pt[self.month-1])
        self.year_label.configure(text=self.year)
        self.update_days()

    def select_day(self, button):
        if self.selected_day:
            self.selected_day.configure(bg='white')
        self.selected_day = button
        self.selected_day.configure(bg='lightblue')

    def update_days(self):
        # Obter o número de dias no mês e o dia da semana do primeiro dia do mês
        num_dias = calendar.monthrange(self.year, self.month)[1]
        dia_semana = calendar.weekday(self.year, self.month, 1)

        # Ajustar para que domingo seja 0, segunda-feira seja 1, etc.
        dia_semana = (dia_semana + 1) % 7

        # Atualizar os números dos dias na interface
        num = 1
        for x in range(3, 9):
            for y in range(7):
                if x == 3 and y < dia_semana:
                    label_num = ctk.CTkLabel(self.frame, text='', width=50, height=50, fg_color='#402160', corner_radius=10, font=('Helverica', 15))
                elif num == self.day and self.month == datetime.datetime.now().month and self.year == datetime.datetime.now().year:
                    button = ctk.CTkButton(self.frame, text=num, width=50, height=50, fg_color='#5E17EB', corner_radius=10, font=('Helverica', 15))
                    button.configure(command=lambda btn=button: self.select_day(btn))
                    label_num = button
                    num += 1
                elif num <= num_dias:
                    button = ctk.CTkButton(self.frame, text=num, width=50, height=50, fg_color='#402160', corner_radius=10, font=('Helverica', 15))
                    button.configure(command=lambda btn=button: self.select_day(btn))
                    label_num = button
                    num += 1
                else:
                    label_num = ctk.CTkLabel(self.frame, text='', width=50, height=50, fg_color='#402160', corner_radius=10, font=('Helverica', 15))

                label_num.grid(row=x, column=y, sticky='nsew', padx=10, pady=5)

