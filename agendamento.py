import customtkinter as ctk

class Agendamento(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.master.title("Agendamento de Vacina")
        
        self.frame = ctk.CTkFrame(self, fg_color='#9156CD')  # Criar um Frame dentro do Calendario
        self.frame.grid(column=0, row=2, sticky='nsew', columnspan=3, padx=20, pady=20)
        
        self.grid_propagate(True)
        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure((0,1,2), weight=1)
        
        
        self.titulo_var = ctk.StringVar()
        self.descricao_var = ctk.StringVar()
        self.data_var = ctk.StringVar()

        # Criando os widgets do formulário
        ctk.CTkLabel(master, text="Título:").grid(row=0, column=1, padx=10, pady=5)
        ctk.CTkEntry(master, textvariable=self.titulo_var).grid(row=0, column=2, padx=10, pady=5)

        ctk.CTkLabel(master, text="Descrição:").grid(row=1, column=1, padx=10, pady=5)
        ctk.CTkEntry(master, textvariable=self.descricao_var).grid(row=1, column=2, padx=10, pady=5)

        ctk.CTkLabel(master, text="Data:").grid(row=2, column=1, padx=10, pady=5)
        ctk.CTkEntry(master, textvariable=self.data_var).grid(row=2, column=2, padx=10, pady=5)

        ctk.CTkButton(master, text="Agendar", command=self.agendar_vacina).grid(row=3, column=1, columnspan=2, pady=10)

    def agendar_vacina(self):
        # Função chamada quando o botão "Agendar" é clicado
        titulo = self.titulo_var.get()
        descricao = self.descricao_var.get()
        data = self.data_var.get()

        # Aqui você pode adicionar a lógica para agendar a vacina com os dados fornecidos
        print(f"Vacina agendada - Título: {titulo}, Descrição: {descricao}, Data: {data}")

if __name__ == "__main__":
    master = ctk.CTk()
    app = Agendamento(master)
    master.mainloop()
