from tkinter import Label, Button, Frame, Menu, Canvas
import tkinter as Tk

class View:
    def __init__(self, master):
        self.master = master

        self.frame = Frame(master)
        self.frame.pack()
        
        self.barra_menu = Menu(self.master)
        self.master.config(menu=self.barra_menu)

        self.menu_archivo = Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Inicio", menu=self.menu_archivo)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.master.quit)
        
        frame_controles = Frame(self.master)
        frame_controles.pack(side=Tk.LEFT, fill=Tk.Y, padx=10, pady=10)

        # Entrada de elementos
        self.entrada = Tk.Entry(frame_controles)
        self.entrada.pack(pady=5)
        
        # Botones de operaciones
        self.button1 = Button(frame_controles, text="Insertar")
        self.button1.pack(pady=5)
        self.button2 = Button(frame_controles, text="Eliminar")
        self.button2.pack(pady=5)
        self.button3 = Button(frame_controles, text="PreOrden")
        self.button3.pack(pady=5)
        self.button4 = Button(frame_controles, text="InOrden")
        self.button4.pack(pady=5)
        self.button5 = Button(frame_controles, text="PostOrden")
        self.button5.pack(pady=5)
        
        # Frame derecho que contiene resultado + canvas
        frame_derecho = Frame(self.master)
        frame_derecho.pack(side=Tk.RIGHT, fill=Tk.BOTH, expand=True, padx=10, pady=10)
        
        self.label = Label(frame_derecho, text="Hello, MVC!", font=("Arial", 12), bg="white", anchor="w", justify="left")
        self.label.pack(fill=Tk.X, pady=(0, 10))
        
        # Canvas para dibujar el árbol
        self.canvas = Canvas(frame_derecho, bg="white", width=400, height=400)
        self.canvas.pack(fill=Tk.BOTH, expand=True)
        

    def nuevo_arbol(self, callback):
        self.menu_archivo.insert_command(0, label="Nuevo Árbol", command=callback)
        
    def on_button1_click(self, callback):
        self.button1.config(command=callback)
        
    def on_button2_click(self, callback):
        self.button2.config(command=callback)

    def on_button3_click(self, callback):
        self.button3.config(command=callback)
        
    def on_button4_click(self, callback):
        self.button4.config(command=callback)
        
    def on_button5_click(self, callback):
        self.button5.config(command=callback)
        
    def clear_entry(self):
        self.entrada.delete(0, Tk.END)
        
    def update_label(self, text):
        """Update the label with the given text."""
        self.label.config(text=text)
        
    def dibujar_arbol(self, arbol):
        self.canvas.delete("all")
        if arbol.getRaiz():
            self._dibujar_nodo(arbol.getRaiz(), 300, 25, 100)

    def _dibujar_nodo(self, nodo, x, y, espacio):
        if nodo is None:
            return

        r = 20  # radio del nodo

        # Dibuja el círculo y el valor
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="white", outline="green", width=2)
        self.canvas.create_text(x, y, text=str(nodo.getDato()), fill="black", font=30)

        # Si tiene hijo izquierdo
        if nodo.getIzquierda():
            self.canvas.create_line(x, y + r, x - espacio, y + 60 - r, fill="red", width=2)
            self._dibujar_nodo(nodo.getIzquierda(), x - espacio, y + 60, espacio // 2)

        # Si tiene hijo derecho
        if nodo.getDerecha():
            self.canvas.create_line(x, y + r, x + espacio, y + 60 - r, fill="red", width=2)
            self._dibujar_nodo(nodo.getDerecha(), x + espacio, y + 60, espacio // 2)