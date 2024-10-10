import tkinter as tk
from controller.usuario_controller import PostoPetroGasController

if __name__ == "__main__":
    root = tk.Tk()
    app = PostoPetroGasController(root)
    root.mainloop()
