import tkinter as tk
from tkinter import messagebox


from config.db_config import db_config
from model.usuario import PostoPetroGasModel
from view.usuario_view import PostoPetroGasView



class PostoPetroGasController:
    def __init__(self, root):
        self.model = PostoPetroGasModel(self)
        self.view = PostoPetroGasView(root, self)
        self.view.login_screen()

    def verificar_senha_administrador(self, senha):
        return senha == self.senha_administrador

    def handle_login(self):
        cpf = self.view.cpf_entry.get()
        password = self.view.password_entry.get()
        if self.model.verify_login(cpf, password):
            self.view.role_selection_screen()
        else:
            self.view.show_message("Erro", "CPF ou senha incorretos!")

    def show_role_selection(self):
        self.view.role_selection_screen()

    def show_fuel_options(self):
        self.view.fuel_options_screen()

    def show_cashier_options(self):
        self.view.cashier_options_screen()

    def fuel_pump(self):
        self.view.show_message("Bomba de Gasolina", "Funcionalidade não implementada")

    def oil_change(self):
        self.view.show_message("Troca de Óleo", "Funcionalidade não implementada")

    def register_sale(self):
        sale_data = "Venda registrada"  # Aqui você pode detalhar os dados da venda
        self.model.register_sale(sale_data)
        self.view.show_message("Cadastrar Venda", "Venda registrada com sucesso!")

    def generate_report(self):
        report = self.model.generate_report()
        self.view.show_message("Relatório", report)



# Exibe a tela de cadastro de combustível
    def show_fuel_registration(self):
        self.view.clear_screen()
        tk.Label(self.view.root, text="Cadastrar Combustível", font=("Arial", 24)).pack(pady=20)

        tk.Label(self.view.root, text="Tipo de Combustível:").pack()
        fuel_type_entry = tk.Entry(self.view.root)
        fuel_type_entry.pack()

        tk.Label(self.view.root, text="Quantidade:").pack()
        fuel_quantity_entry = tk.Entry(self.view.root)
        fuel_quantity_entry.pack()

        tk.Button(self.view.root, text="Cadastrar", command=lambda: self.register_fuel(fuel_type_entry.get(), fuel_quantity_entry.get())).pack(pady=10)
        tk.Button(self.view.root, text="Voltar", command=self.view.fuel_options_screen).pack(pady=20)

    def register_fuel(self, fuel_type, quantity):
        self.model.register_fuel(fuel_type, int(quantity))
        self.view.show_message("Sucesso", "Combustível cadastrado com sucesso!")

    # Exibe a tela de visualização de quantidade de combustível
    def show_fuel_quantity(self):
        self.view.clear_screen()
        tk.Label(self.view.root, text="Ver Quantidade Disponível", font=("Arial", 24)).pack(pady=20)

        tk.Label(self.view.root, text="Tipo de Combustível:").pack()
        fuel_type_entry = tk.Entry(self.view.root)
        fuel_type_entry.pack()

        tk.Button(self.view.root, text="Verificar", command=lambda: self.check_fuel_quantity(fuel_type_entry.get())).pack(pady=10)
        tk.Button(self.view.root, text="Voltar", command=self.view.fuel_options_screen).pack(pady=20)

    def check_fuel_quantity(self, fuel_type):
        quantity = self.model.get_fuel_quantity(fuel_type)
        self.view.show_message("Quantidade Disponível", f"{fuel_type}: {quantity} unidades")

    # Exibe a tela de cadastro de óleo
    def show_oil_registration(self):
        self.view.clear_screen()
        tk.Label(self.view.root, text="Cadastrar Óleo", font=("Arial", 24)).pack(pady=20)

        tk.Label(self.view.root, text="Tipo de Óleo:").pack()
        oil_type_entry = tk.Entry(self.view.root)
        oil_type_entry.pack()

        tk.Label(self.view.root, text="Marca:").pack()
        brand_entry = tk.Entry(self.view.root)
        brand_entry.pack()

        tk.Label(self.view.root, text="Viscosidade:").pack()
        viscosity_entry = tk.Entry(self.view.root)
        viscosity_entry.pack()

        tk.Label(self.view.root, text="Quantidade:").pack()
        oil_quantity_entry = tk.Entry(self.view.root)
        oil_quantity_entry.pack()

        tk.Button(self.view.root, text="Cadastrar", command=lambda: self.register_oil(oil_type_entry.get(), brand_entry.get(), viscosity_entry.get(), oil_quantity_entry.get())).pack(pady=10)
        tk.Button(self.view.root, text="Voltar", command=self.view.oil_options_screen).pack(pady=20)

    def register_oil(self, oil_type, brand, viscosity, quantity):
        self.model.register_oil(oil_type, brand, viscosity, int(quantity))
        self.view.show_message("Sucesso", "Óleo cadastrado com sucesso!")

    # Exibe a tela de visualização de quantidade de óleo
    def show_oil_quantity(self):
        self.view.clear_screen()
        tk.Label(self.view.root, text="Ver Quantidade Disponível", font=("Arial", 24)).pack(pady=20)

        tk.Label(self.view.root, text="Tipo de Óleo:").pack()
        oil_type_entry = tk.Entry(self.view.root)
        oil_type_entry.pack()

        tk.Button(self.view.root, text="Verificar", command=lambda: self.check_oil_quantity(oil_type_entry.get())).pack(pady=10)
        tk.Button(self.view.root, text="Voltar", command=self.view.oil_options_screen).pack(pady=20)

    def check_oil_quantity(self, oil_type):
        quantity = self.model.get_oil_quantity(oil_type)