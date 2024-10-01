import tkinter as tk
from tkinter import messagebox

class CadastroFuncionario:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Funcionário")

        # Lista para armazenar funcionários
        self.funcionarios = {}

        # Labels e Entradas
        self.label_nome = tk.Label(master, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nome = tk.Entry(master)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        self.label_cargo = tk.Label(master, text="Cargo:")
        self.label_cargo.grid(row=1, column=0, padx=10, pady=10)
        self.entry_cargo = tk.Entry(master)
        self.entry_cargo.grid(row=1, column=1, padx=10, pady=10)

        self.label_salario = tk.Label(master, text="Salário:")
        self.label_salario.grid(row=2, column=0, padx=10, pady=10)
        self.entry_salario = tk.Entry(master)
        self.entry_salario.grid(row=2, column=1, padx=10, pady=10)

        # Botão para cadastrar 
        self.button_cadastrar = tk.Button(master, text="Cadastrar", command=self.cadastrar)
        self.button_cadastrar.grid(row=3, columnspan=2, pady=10)

        # Botão para buscar
        self.button_buscar = tk.Button(master, text="Buscar", command=self.buscar)
        self.button_buscar.grid(row=4, columnspan=2, pady=10)

        # Botão para abrir tela de administrador
        self.button_admin = tk.Button(master, text="Tela Administrador", command=self.abrir_tela_admin)
        self.button_admin.grid(row=5, columnspan=2, pady=10)

        # Centralizar a janela
        self.centralizar_janela()

    def centralizar_janela(self):
        # Obtém a largura e altura da tela
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()

        # Obtém a largura e altura da janela
        largura_janela = 400  # Defina um tamanho fixo ou use self.master.winfo_width()
        altura_janela = 300   # Defina um tamanho fixo ou use self.master.winfo_height()

        # Calcula a posição x e y para centralizar a janela
        x = (largura_tela // 2) - (largura_janela // 2)
        y = (altura_tela // 2) - (altura_janela // 2)

        # Define a geometria da janela
        self.master.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

    def cadastrar(self):
        nome = self.entry_nome.get()
        cargo = self.entry_cargo.get()
        salario = self.entry_salario.get()

        if nome and cargo and salario:
            self.funcionarios[nome] = {'cargo': cargo, 'salario': salario}
            messagebox.showinfo("Cadastro", f"Funcionário {nome} cadastrado com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")

    def buscar(self):
        nome = self.entry_nome.get()
        if nome in self.funcionarios:
            funcionario = self.funcionarios[nome]
            cargo = funcionario['cargo']
            salario = funcionario['salario']
            messagebox.showinfo("Funcionário Encontrado", f"Nome: {nome}\nCargo: {cargo}\nSalário: {salario}")
        else:
            messagebox.showwarning("Atenção", "Funcionário não encontrado!")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_cargo.delete(0, tk.END)
        self.entry_salario.delete(0, tk.END)

    def abrir_tela_admin(self):
        self.admin_window = tk.Toplevel(self.master)
        self.admin_window.title("Cadastro Administrador")

        # Centralizar a janela do administrador
        self.centralizar_janela_admin()

        # Labels e Entradas para Admin
        tk.Label(self.admin_window, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
        self.admin_entry_nome = tk.Entry(self.admin_window)
        self.admin_entry_nome.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.admin_window, text="CPF:").grid(row=1, column=0, padx=10, pady=10)
        self.admin_entry_cpf = tk.Entry(self.admin_window)
        self.admin_entry_cpf.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.admin_window, text="Cargo:").grid(row=2, column=0, padx=10, pady=10)
        self.admin_entry_cargo = tk.Entry(self.admin_window)
        self.admin_entry_cargo.grid(row=2, column=1, padx=10, pady=10)

        # Botão para cadastrar na tela de administrador
        self.button_cadastrar_admin = tk.Button(self.admin_window, text="Cadastrar", command=self.cadastrar_admin)
        self.button_cadastrar_admin.grid(row=3, columnspan=2, pady=10)

    def centralizar_janela_admin(self):
        # Obtém a largura e altura da tela
        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()

        # Obtém a largura e altura da janela de admin
        largura_janela = 400  # Defina um tamanho fixo
        altura_janela = 300   # Defina um tamanho fixo

        # Calcula a posição x e y para centralizar a janela
        x = (largura_tela // 2) - (largura_janela // 2)
        y = (altura_tela // 2) - (altura_janela // 2)

        # Define a geometria da janela
        self.admin_window.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

    def cadastrar_admin(self):
        nome = self.admin_entry_nome.get()
        cpf = self.admin_entry_cpf.get()
        cargo = self.admin_entry_cargo.get()

        if nome and cpf and cargo:
            self.funcionarios[nome] = {'cpf': cpf, 'cargo': cargo}
            messagebox.showinfo("Cadastro", f"Administrador {nome} cadastrado com sucesso!")
            self.admin_entry_nome.delete(0, tk.END)
            self.admin_entry_cpf.delete(0, tk.END)
            self.admin_entry_cargo.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroFuncionario(root)
    root.mainloop()
