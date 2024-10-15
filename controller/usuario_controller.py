import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#from config.db_config import db_config
from model.usuario import Model
from view.usuario_view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def iniciar(self):
        self.view.iniciar_menu()

    def validar_login(self):
        cpf = self.view.cpf_entry.get()
        for funcionario in self.model.listar_funcionarios():
            if funcionario.cpf == cpf and funcionario.funcao == "Frentista":
                self.view.mostrar_menu_admin()  # Trocar para menu frentista, se houver
                return
        self.view.mostrar_mensagem_erro("Funcionário não encontrado ou função inválida!")

    def abrir_tela_senha(self):
        self.view.mostrar_tela_senha()

    def validar_senha_admin(self):
        senha = self.view.senha_entry.get()
        if senha == self.model.admin_senha:
            self.view.mostrar_menu_admin()
        else:
            self.view.mostrar_mensagem_erro("Senha inválida!")

    def abrir_cadastrar_funcionario(self):
        # Aqui chamamos a view para exibir a tela de cadastro de funcionário
        pass

    def abrir_listar_funcionarios(self):
        funcionarios = [(f.nome, f.cpf, f.funcao) for f in self.model.listar_funcionarios()]
        self.view.mostrar_listagem("Listar Funcionários", funcionarios, ["Nome", "CPF", "Função"])