from collections import defaultdict
from datetime import datetime
from repository.usuario_repository import PostoPetroGasRepository


class Funcionario:
    def __init__(self, nome, cpf, funcao):
        self.nome = nome
        self.cpf = cpf
        self.funcao = funcao

class Combustivel:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class Oleo:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class Model:
    def __init__(self):
        self.funcionarios = [
            Funcionario("João", "12345678900", "Frentista"),
            Funcionario("Maria", "09876543211", "Frentista")
        ]
        self.combustiveis = []
        self.oleos = []
        self.admin_senha = "admin123"

    # Métodos de gerenciamento de funcionários
    def adicionar_funcionario(self, nome, cpf, funcao):
        funcionario = Funcionario(nome, cpf, funcao)
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        return self.funcionarios

    # Métodos de gerenciamento de combustíveis
    def adicionar_combustivel(self, nome, quantidade):
        combustivel = Combustivel(nome, quantidade)
        self.combustiveis.append(combustivel)

    def listar_combustiveis(self):
        return self.combustiveis

    # Métodos de gerenciamento de óleos
    def adicionar_oleo(self, nome, quantidade):
        oleo = Oleo(nome, quantidade)
        self.oleos.append(oleo)

    def listar_oleos(self):
        return self.oleos