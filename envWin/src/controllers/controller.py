class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Bind view events to controller methods
        self.view.nuevo_arbol(self.nuevo_arbol)
        self.view.on_button1_click(self.boton_inserta)
        self.view.on_button2_click(self.boton_elimina)
        self.view.on_button3_click(self.boton_pre_orden)
        self.view.on_button4_click(self.boton_in_orden)
        self.view.on_button5_click(self.boton_post_orden)

    def nuevo_arbol(self):
        # Aquí reinicias tu estructura de árbol
        self.view.canvas.delete("all")
        self.model.restart_arbol()
        self.view.update_label("Nuevo Árbol")

    def boton_inserta(self):
        # inserta en model
        data = self.view.entrada.get()
        self.model.insertar(data)
        self.view.dibujar_arbol(self.model.get_arbol())
        self.view.clear_entry()
        
    def boton_elimina(self):
        # elimina en model
        data = self.view.entrada.get()
        self.model.eliminar(data)
        self.view.dibujar_arbol(self.model.get_arbol())
        self.view.clear_entry()

    def boton_pre_orden(self):
        # recorrido preOrden
        recorrido = "PreOrden: " + self.model.pre_order()
        self.view.update_label(recorrido)
        
    def boton_in_orden(self):
        # recorrido inOrden
        recorrido = "InOrden: " + self.model.in_order()
        self.view.update_label(recorrido)
        
    def boton_post_orden(self):
        # recorrido postOrden
        recorrido = "PostOrden: " + self.model.post_order()
        self.view.update_label(recorrido)

    def update_model(self, new_data):
        self.model.set_data(new_data)
        self.view.update_display(new_data)
    
    def update_view(self):
        """Update the view with data from the model."""
        data = self.model.get_data()  # Supongamos que el modelo tiene un método get_data()
        self.view.update_label(data)