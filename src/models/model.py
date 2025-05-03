from arbol_binario.ABB import ABB
class DataModel:
    def __init__(self):
        self.data = []
        self.arbol = ABB()

    def add_data(self, item):
        self.data.append(item)

    def get_data(self):
        return self.data[0] if self.data else "No Data Available"

    def clear_data(self):
        self.data.clear()
        
    def restart_arbol(self):
        self.arbol = None
        self.arbol = ABB()
        
    def get_arbol(self):
        return self.arbol
        
    def insertar(self, valor):
        self.arbol.insertarNodo(valor)
        
    def eliminar(self, valor):
        self.arbol.eliminarNodo(valor)
        
    def in_order(self):
        return self.arbol.inOrden()
    
    def pre_order(self):
        return self.arbol.preOrden()
    
    def post_order(self):
        return self.arbol.postOrden()