class Nodo:
    def __init__(self, valor):
        self.__dato = valor
        self.__izquierda = None
        self.__derecha = None
        
#Metodos de la clase Nodo
#Metodos setter y getter
    def setDato(self, valor):
        self.__dato = valor
        
    def getDato(self):
        return self.__dato
    
    def setIzquierda(self, nodo):
        self.__izquierda = nodo
        
    def getIzquierda(self):
        return self.__izquierda
    
    def setDerecha(self, nodo):
        self.__derecha = nodo
        
    def getDerecha(self):
        return self.__derecha