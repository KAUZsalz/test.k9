import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class View:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Posto de Combustíveis")
        self.root.geometry("400x200")

    def iniciar_menu(self):
        tk.Label(self.root, text="CPF do Funcionário:").grid(row=0, column=0, padx=10, pady=10)
        self.cpf_entry = tk.Entry(self.root)
        self.cpf_entry.grid(row=0, column=1, padx=10)

        tk.Button(self.root, text="Login", command=self.controller.validar_login).grid(row=1, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text="Admin?").grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Entrar como Admin", command=self.controller.abrir_tela_senha).grid(row=2, column=1, padx=10, pady=10)

        self.root.mainloop()

    def mostrar_tela_senha(self):
        self.tela_senha = tk.Toplevel()
        self.tela_senha.title("Login Administrador")
        self.tela_senha.geometry("400x200")

        tk.Label(self.tela_senha, text="Senha do Administrador:").grid(row=0, column=0, padx=10, pady=10)
        self.senha_entry = tk.Entry(self.tela_senha, show="*")
        self.senha_entry.grid(row=0, column=1, padx=10)

        tk.Button(self.tela_senha, text="Entrar", command=self.controller.validar_senha_admin).grid(row=1, column=0, columnspan=2, pady=10)

    def mostrar_menu_admin(self):
        self.tela_senha.destroy()
        tela_admin = tk.Toplevel()
        tela_admin.title("Menu Administrador")
        tela_admin.geometry("600x400")

        tk.Label(tela_admin, text="Menu Administrador", font=("Arial", 24)).grid(row=0, column=0, columnspan=2, pady=20)

        tk.Button(tela_admin, text="Cadastrar Funcionário", command=self.controller.abrir_cadastrar_funcionario, width=20).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(tela_admin, text="Listar Funcionários", command=self.controller.abrir_listar_funcionarios, width=20).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(tela_admin, text="Sair", command=tela_admin.destroy, width=20).grid(row=2, column=0, columnspan=2, pady=10)

    def mostrar_listagem(self, title, data, columns):
        tela_listar = tk.Toplevel()
        tela_listar.title(title)
        tela_listar.geometry("600x400")

        tree = ttk.Treeview(tela_listar, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)

        for item in data:
            tree.insert("", tk.END, values=item)

        tree.pack(pady=20)
        tk.Button(tela_listar, text="Voltar", command=tela_listar.destroy, width=20).pack(pady=10)
    
    def mostrar_mensagem_erro(self, mensagem):
        messagebox.showerror("Erro", mensagem)
    
    def mostrar_mensagem_sucesso(self, mensagem):
        messagebox.showinfo("Sucesso", mensagem)

