from tkinter import *
import os
from PIL import Image, ImageTk

#Funcion para cargar imagen
#E:Nombre de la imagen(str), ancho y alto
#S:Imagen redimensionada en un formato compatible con Tkinter
#R:No tiene
def cargarImagen(fichero, nombre, width, height): 
    ruta = os.path.join(fichero, nombre)
    imagenLoad = Image.open(ruta).resize((width, height))  
    imagen = ImageTk.PhotoImage(imagenLoad)
    return imagen