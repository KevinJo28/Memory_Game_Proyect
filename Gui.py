from tkinter import * 

#Modelizacion de la interfaz grafica
"""
Atributos:
@root
@Canvas
"""
class Gui:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(root)

    def configurarVentana(self):
        self.root.minsize(700, 500)
        self.root.title("Memory Game")
        self.canvas.pack(fill='both', expand=True)
        self.creacionDeTitulos()

    def creacionDeTitulos(self):
        self.canvas.create_text(320, 50, text="Memory Game", font=("Arial", 20))


    