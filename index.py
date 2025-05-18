from tkinter import * 

#Ventana Principal
ventana = Tk()
ventana.minsize(1100, 800)
#Canvas y asgnacion en la ventana
canvas = Canvas(ventana)
canvas.pack(fill='both', expand=True)


ventana.mainloop()