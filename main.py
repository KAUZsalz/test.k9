import tkinter as tk
from tkinter import ttk
from controller.usuario_controller import Controller
if __name__ == "__main__":
    root =tk.Tk()
    app = Controller()
    app.iniciar()
