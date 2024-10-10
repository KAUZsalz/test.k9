import tkinter as tk
from tkinter import messagebox, StringVar

class PostoPetroGasView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Posto PetroGas - Sistema")
        self.root.geometry("400x400")
        self.cpf_entry = None
        self.password_entry = None
        self.produto_var = StringVar(self.root)
        self.produto_var.set("Produtos")

        self.pagamento_var = StringVar(self.root)
        self.pagamento_var.set("Dinheiro")

        self.create_login_screen()


    def login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Posto PetroGas", font=("Arial", 24)).pack(pady=20)

        tk.Label(self.root, text="Insira CPF:").pack()
        self.cpf_entry = tk.Entry(self.root)
        self.cpf_entry.pack()

        tk.Label(self.root, text="Insira senha:").pack()
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.controller.handle_login).pack(pady=10)

    def role_selection_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Posto PetroGas", font=("Arial", 24)).pack(pady=20)

        tk.Button(self.root, text="Frentista", width=20, command=self.controller.show_fuel_options).pack(pady=10)
        tk.Button(self.root, text="Caixa", width=20, command=self.controller.show_cashier_options).pack(pady=10)

    def fuel_options_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Posto PetroGas", font=("Arial", 24)).grid(row=0, column=0, columnspan=2, pady=20)

        tk.Button(self.root, text="Bomba de Gasolina", width=30, command=self.controller.fuel_pump).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Troca de Óleo", width=30, command=self.controller.oil_change).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Voltar", command=self.controller.show_role_selection).grid(row=2, column=0, columnspan=2, pady=20)

    def cashier_options_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Posto PetroGas", font=("Arial", 24)).pack(pady=20)

        tk.Button(self.root, text="Cadastrar Venda", width=30, command=self.controller.register_sale).pack(pady=10)
        tk.Button(self.root, text="Gerar Relatório Mensal", width=30, command=self.controller.generate_report).pack(pady=10)

        tk.Button(self.root, text="Voltar", command=self.controller.show_role_selection).pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def create_widgets(self):
        # Aqui, criamos as telas correspondentes, como a de cadastro de combustível e óleo
        pass

    def fuel_options_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Bomba de Gasolina", font=("Arial", 24)).pack(pady=20)

        tk.Button(self.root, text="Cadastrar Combustível", width=30, command=self.controller.show_fuel_registration).pack(pady=10)
        tk.Button(self.root, text="Ver Quantidade Disponível", width=30, command=self.controller.show_fuel_quantity).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.controller.show_role_selection).pack(pady=20)

    def oil_options_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Troca de Óleo", font=("Arial", 24)).grid(row=0, column=0, columnspan=2, pady=20)


        tk.Button(self.root, text="Cadastrar Óleo", width=30, command=self.controller.show_oil_registration).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Ver Quantidade Disponível", width=30, command=self.controller.show_oil_quantity).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Voltar", command=self.controller.show_role_selection).grid(row=2, column=0, columnspan=2, pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_message(self, title, message):
        messagebox.showinfo(title, message)


    def create_login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Tela de Login").pack(pady=10)
        tk.Label(self.root, text="Usuário:").pack()
        self.entry_usuario = tk.Entry(self.root)
        self.entry_usuario.pack()

        tk.Label(self.root, text="Senha:").pack()
        self.entry_senha = tk.Entry(self.root, show="*")
        self.entry_senha.pack()

        button_login = tk.Button(self.root, text="Login", command=self.controller.verificar_login)
        button_login.pack(pady=20)

    def create_vendas_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Produto Vendido:").pack(pady=5)
        opcoes_produtos = ["Sorvete", "Refrigerante", "Cerveja"]
        menu_produto = tk.OptionMenu(self.root, self.produto_var, *opcoes_produtos)
        menu_produto.pack(pady=5)

        tk.Label(self.root, text="Quantidade:").pack(pady=5)
        self.entry_quantidade = tk.Entry(self.root)
        self.entry_quantidade.pack(pady=5)

        tk.Label(self.root, text="Valor Unitário (R$):").pack(pady=5)
        self.entry_valor = tk.Entry(self.root)
        self.entry_valor.pack(pady=5)

        tk.Label(self.root, text="Tipo de Pagamento:").pack(pady=5)
        opcoes_pagamento = ["Dinheiro", "Cartão de Crédito", "Cartão de Débito"]
        menu_pagamento = tk.OptionMenu(self.root, self.pagamento_var, *opcoes_pagamento)
        menu_pagamento.pack(pady=5)

        button_registrar = tk.Button(self.root, text="Registrar Venda", command=self.controller.registrar_venda)
        button_registrar.pack(pady=10)

        button_relatorio = tk.Button(self.root, text="Gerar Relatório Mensal", command=self.controller.gerar_relatorio)
        button_relatorio.pack(pady=10)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def show_error(self, title, message):
        messagebox.showerror(title, message)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()