from tkinter import *
from Gui import Gui
if __name__ == "__main__":
    #Ventana Principal
    root = Tk()
    app = Gui(root)
    app.configurarVentana()
    root.mainloop()
