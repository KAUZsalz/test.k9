import psycopg2 
from psycopg2 import sql

from model import Funcionario, Combustivel, Oleos

class Repository:
    def __init__(self):
        self.funcionarios = [
            Funcionario("João", "12345678900", "Frentista"),
            Funcionario("Maria", "09876543211", "Frentista"),
        ]
        self.combustiveis = []
        self.oleos = []

    def add_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def add_combustivel(self, combustivel):
        self.combustiveis.append(combustivel)

    def add_oleo(self, oleo):
        self.oleos.append(oleo)

    def get_funcionarios(self):
        return self.funcionarios

    def get_combustiveis(self):
        return self.combustiveis

    def get_oleos(self):
        return self.oleos
