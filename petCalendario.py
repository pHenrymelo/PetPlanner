import tkinter as tk
from tkinter import ttk
import calendar
import datetime

def mostrar_calendario(year, month, root):

    def selecionar_dia(day):
        selected_date.set(f"{month_names[month_var.get() - 1]} {day}, {year_var.get()}")

    def atualizar_calendario():
        cal = calendar.monthcalendar(year_var.get(), month_var.get())
        clear_calendar()
        row = 0
        col = 0
        today = datetime.datetime.now().day
        for day_name in day_names:
            day_label = tk.Label(frame, text=day_name, width=4, height=2, borderwidth=1, relief="solid")
            day_label.grid(row=row, column=col, padx=2, pady=2)
            col += 1
        for week in cal:
            row += 1
            col = 0
            for day in week:
                if day == 0:
                    day_label = tk.Label(frame, text="", width=4, height=2, borderwidth=1, relief="solid")
                else:
                    day_label = tk.Label(frame, text=day, width=4, height=2, borderwidth=1, relief="solid", anchor="center")
                    day_label.bind("<Button-1>", lambda e, day=day: selecionar_dia(day))
                day_label.grid(row=row, column=col, padx=2, pady=2)
                # Destaque o dia atual (hoje)
                if day == today and month_var.get() == datetime.datetime.now().month and year_var.get() == datetime.datetime.now().year:
                    day_label.configure(bg='lightblue')
                col += 1

    def clear_calendar():
        for widget in frame.winfo_children():
            widget.grid_forget()

    

    month_names = [calendar.month_name[i] for i in range(1, 13)]
    day_names = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']

    frame_main = tk.Frame(root,borderwidth=10,relief=tk.RIDGE)
    frame_main.pack(expand=True,fill='both')
    frame_calen = tk.Frame(frame_main,borderwidth=10,relief=tk.RIDGE)
    frame_calen.pack()
    frame_days = tk.Frame(frame_calen,borderwidth=10,relief=tk.RIDGE)
    frame_days.pack()

    selected_date = tk.StringVar()
    header_frame = tk.Frame(frame_calen,borderwidth=10,relief=tk.RIDGE)
    header_frame.pack()

    prev_button = tk.Button(header_frame, text="Anterior", command=lambda: change_month(-1))
    prev_button.grid(row=0, column=0)

    month_var = tk.IntVar()
    month_var.set(month)
    month_option = tk.OptionMenu(header_frame, month_var, *range(1, 13))
    month_option.grid(row=0, column=1)

    year_var = tk.IntVar()
    year_var.set(year)
    year_entry = tk.Entry(header_frame, textvariable=year_var)
    year_entry.grid(row=0, column=2)

    next_button = tk.Button(header_frame, text="Próximo", command=lambda: change_month(1))
    next_button.grid(row=0, column=3)

    frame = tk.Frame(frame_calen,borderwidth=10,relief=tk.RIDGE)
    frame.pack()

    selected_date_label = tk.Label(frame_main, textvariable=selected_date, font=("Helvetica", 12))
    selected_date_label.pack()

    def change_month(delta):
        current_month = month_var.get()
        new_month = current_month + delta
        if new_month < 1:
            new_month = 12
            year_var.set(year_var.get() - 1)
        elif new_month > 12:
            new_month = 1
            year_var.set(year_var.get() + 1)
        month_var.set(new_month)

    month_var.trace("w", lambda *args: atualizar_calendario())
    year_var.trace("w", lambda *args: atualizar_calendario())

    atualizar_calendario()


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

    month = 10
    year = 2023 
    mostrar_calendario(year, month,root)

    root.mainloop()