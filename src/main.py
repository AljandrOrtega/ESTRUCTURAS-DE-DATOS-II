# filepath: /tkinter-mvc-app/tkinter-mvc-app/src/main.py

import tkinter as tk
from views.view import View
from controllers.controller import Controller
from models.model import DataModel as Model

def main():
    root = tk.Tk()
    root.title("MVC Árbol Binario de Búsqueda")
    # Tamaño deseado de la ventana
    ancho_ventana = 800
    alto_ventana = 600
    ventana = str(ancho_ventana) + "x" + str(alto_ventana)

    # Obtener dimensiones de la pantalla
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()

    # Calcular posición para centrar
    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2)
    ventana += "+" + str(x) + "+" + str(y)

    # Establecer tamaño y posición de la ventana
    root.geometry(ventana)
    
    model = Model()
    model.add_data("PreOrden")
    view = View(root)
    controller = Controller(model, view)
    
    root.mainloop()

if __name__ == "__main__":
    main()