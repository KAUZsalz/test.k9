import psycopg2
from psycopg2 import sql

class PostoPetroGasRepository:
    def __init__(self):
        
        self.users = {
            "62357104376": "2814",  
        }
        self.sales = []
        self.fuel_data = {}
        self.oil_data = {}
        self.vendas = []

    
    def get_user_by_cpf(self, cpf):
        return self.users.get(cpf)

    def save_sale(self, sale_data):
        self.sales.append(sale_data)

    def get_all_sales(self):
        return self.sales
    
     # Armazenar informações de combustíveis
    def save_fuel(self, fuel_type, quantity):
        self.fuel_data[fuel_type] = self.fuel_data.get(fuel_type, 0) + quantity

    # Obter a quantidade de combustível disponível
    def get_fuel_quantity(self, fuel_type):
        return self.fuel_data.get(fuel_type, 0)

    # Armazenar informações de óleo
    def save_oil(self, oil_type, brand, viscosity, quantity):
        self.oil_data[oil_type] = {
            "brand": brand,
            "viscosity": viscosity,
            "quantity": self.oil_data.get(oil_type, {}).get("quantity", 0) + quantity
        }

    # Obter a quantidade de óleo disponível
    def get_oil_quantity(self, oil_type):
        return self.oil_data.get(oil_type, {}).get("quantity", 0)
    
    def salvar_venda(self, venda):
        self.vendas.append(venda)

    def obter_vendas(self):
        return self.vendas
    