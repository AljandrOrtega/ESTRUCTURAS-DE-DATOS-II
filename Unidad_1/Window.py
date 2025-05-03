from sNodo import Nodo
from ABB import ABB
import tkinter as tk
from tkinter import messagebox

class InterfazABB:
    def __init__(self, raiz):
        self.ventana = raiz
        self.arbol = ABB()
        self.ventana.title("Árbol Binario de Búsqueda")
        self.ventana.geometry("800x600")

        self.crear_menu()
        self.crear_widgets()

    def crear_menu(self):
        barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=barra_menu)

        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Nuevo Árbol Binario de Búsqueda", command=self.nuevo_arbol)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.ventana.quit)

    def crear_widgets(self):
        frame_controles = tk.Frame(self.ventana)
        frame_controles.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Entrada de elementos
        self.entrada = tk.Entry(frame_controles)
        self.entrada.pack(pady=5)

        # Botones de operaciones
        tk.Button(frame_controles, text="Insertar", command=self.insertar).pack(pady=5)
        tk.Button(frame_controles, text="Eliminar", command=self.eliminar).pack(pady=5)
        tk.Button(frame_controles, text="PreOrden", command=self.preorden).pack(pady=5)
        tk.Button(frame_controles, text="InOrden", command=self.inorden).pack(pady=5)
        tk.Button(frame_controles, text="PostOrden", command=self.postorden).pack(pady=5)

        # Frame derecho que contiene resultado + canvas
        frame_derecho = tk.Frame(self.ventana)
        frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Etiqueta de resultado arriba del canvas
        self.resultado = tk.Label(frame_derecho, text="", font=("Arial", 12), bg="white", anchor="w", justify="left", wraplength=380)
        self.resultado.pack(fill=tk.X, pady=(0, 10))

        # Canvas para dibujar el árbol
        self.canvas = tk.Canvas(frame_derecho, bg="white", width=400, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def nuevo_arbol(self):
        # Aquí reinicias tu estructura de árbol
        messagebox.showinfo("Nuevo", "Nuevo árbol creado.")
        self.arbol = ABB()
        self.canvas.delete("all")
        self.resultado.config(text="")

    def insertar(self):
        valor = self.entrada.get()
        if valor:
            # Aquí llamas a tu método de insertar en el árbol
            self.arbol.insertarNodo(int(valor))
            print(f"Insertar: {valor}")
            self.dibujar_arbol()
            # Redibujar árbol aquí
        self.entrada.delete(0, tk.END)

    def eliminar(self):
        valor = self.entrada.get()
        if valor:
            # Aquí llamas a eliminar
            self.arbol.eliminarNodo(int(valor))
            print(f"Eliminar: {valor}")
            self.dibujar_arbol()
            # Redibujar árbol aquí
        self.entrada.delete(0, tk.END)

    def preorden(self):
        # Llamas a tu método de recorrido preorden
        recorrido = self.arbol.preOrden()
        self.resultado.config(text=f"PreOrden: {recorrido}")

    def inorden(self):
        recorrido = self.arbol.inOrden()
        self.resultado.config(text=f"InOrden: {recorrido}")

    def postorden(self):
        recorrido = self.arbol.postOrden()
        self.resultado.config(text=f"PostOrden: {recorrido}")
        
    def dibujar_arbol(self):
        self.canvas.delete("all")
        if self.arbol.getRaiz():
            self._dibujar_nodo(self.arbol.getRaiz(), 200, 20, 100)

    def _dibujar_nodo(self, nodo, x, y, espacio):
        if nodo is None:
            return

        r = 15  # radio del nodo

        # Dibuja el círculo y el valor
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="black")
        self.canvas.create_text(x, y, text=str(nodo.getDato()), fill="white", font=20)

        # Si tiene hijo izquierdo
        if nodo.getIzquierda():
            self.canvas.create_line(x, y + r, x - espacio, y + 60 - r, fill="red")
            self._dibujar_nodo(nodo.getIzquierda(), x - espacio, y + 60, espacio // 2)

        # Si tiene hijo derecho
        if nodo.getDerecha():
            self.canvas.create_line(x, y + r, x + espacio, y + 60 - r, fill="red")
            self._dibujar_nodo(nodo.getDerecha(), x + espacio, y + 60, espacio // 2)