from collections import defaultdict
from datetime import datetime
from repository.usuario_repository import PostoPetroGasRepository


class PostoPetroGasModel:

    def __init__(self, quantidade, valor_unitario, tipo_pagamento, produto):
        self.quantidade = quantidade 
        self.valor_unitario = valor_unitario 
        self.tipo_pagamento = tipo_pagamento
        self.produto = produto  
        self.data = datetime.now()
        self.valor_total = self.calcular_valor_total()

    # Verifica se o login é válido
    def verify_login(self, cpf, password):
        stored_password = self.repository.get_user_by_cpf(cpf)
        return stored_password == password

    # Registra uma venda no repositório
    def register_sale(self, sale_data):
        self.repository.save_sale(sale_data)
        self.quantidade = 10
        self.valor_unitario = 5.50
        self.tipo_pagamento = "cartão"
        self.produto = "gasolina"

    # Gera um relatório de vendas a partir do repositório
    def generate_report(self):
        sales = self.repository.get_all_sales()
        return f"Total de vendas: {len(sales)}"
    
    # Método para cadastrar combustíveis
    def register_fuel(self, fuel_type, quantity):
        self.repository.save_fuel(fuel_type, quantity)

    # Método para ver quantidade disponível de combustível
    def get_fuel_quantity(self, fuel_type):
        return self.repository.get_fuel_quantity(fuel_type)

    # Método para cadastrar óleo
    def register_oil(self, oil_type, brand, viscosity, quantity):
        self.repository.save_oil(oil_type, brand, viscosity, quantity)

    # Método para ver quantidade disponível de óleo
    def get_oil_quantity(self, oil_type):
        return self.repository.get_oil_quantity(oil_type)
    
    def calcular_valor_total(self):
        return self.quantidade * self.valor_unitario
   
    def gerar_relatorio_mensal(self, vendas):
        relatorio = defaultdict(float)
        for venda in vendas:
            mes = venda.data.strftime("%Y-%m")
            relatorio[mes] += venda.valor_total
        
        return relatorio




    

       
   
