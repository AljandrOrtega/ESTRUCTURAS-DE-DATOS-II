from arbol_binario.sNodo import Nodo

class ABB:
    __raiz = Nodo
    
    def __init__(self, valor):
        self.__raiz = Nodo(valor)
        
    def __init__(self):
        self.__raiz = None
        
    def getRaiz(self):
        """ Devuelve la raíz del árbol. """
        return self.__raiz
    
    def setRaiz(self, valor):
        """ Asigna un nodo como la raíz del árbol. """
        self.__raiz = Nodo(valor)   
        
    def insertarNodo(self, valor):
        if self.__raiz is None:
            self.__raiz = Nodo(valor)
        else:
            actual = self.__raiz
            while valor != actual.getDato():
                if valor < actual.getDato():
                    if actual.getIzquierda() is None:
                        actual.setIzquierda(Nodo(valor))
                    actual = actual.getIzquierda()
                else:
                    if actual.getDerecha() is None:
                        actual.setDerecha(Nodo(valor))
                    actual = actual.getDerecha()
                
    def esVacio(self):
        return self.__raiz is None
    
    def esHoja(self, nodo):
        return nodo.getIzquierda() is None and nodo.getDerecha() is None
    
    def buscar(self, valor):
        nodo_buscar = self.__raiz
        while nodo_buscar is not None:
            if valor < nodo_buscar.getDato():
                nodo_buscar = nodo_buscar.getIzquierda()
            elif valor > nodo_buscar.getDato():
                nodo_buscar = nodo_buscar.getDerecha()
            else:
                return nodo_buscar
        return None
    
    def inOrden(self):
        resultado = []
        pila = []
        actual = self.__raiz

        while pila or actual:
            # Ir lo más a la izquierda posible
            while actual:
                pila.append(actual)
                actual = actual.getIzquierda()
        
            actual = pila.pop()
            resultado.append(str(actual.getDato()))  # Agregar dato al resultado
            actual = actual.getDerecha()

        return ", ".join(resultado)

    
    def postOrden(self):
        if self.__raiz is None:
            return ""

        resultado = []
        pila = [self.__raiz]

        while pila:
            nodo = pila.pop()
            resultado.insert(0, str(nodo.getDato()))  # Insertar al inicio como texto

            if nodo.getIzquierda():
                pila.append(nodo.getIzquierda())
            if nodo.getDerecha():
                pila.append(nodo.getDerecha())

        return ", ".join(resultado)
    
    def preOrden(self):
        if self.__raiz is None:
            return ""

        resultado = []
        pila = [self.__raiz]

        while pila:
            nodo = pila.pop()
            resultado.append(str(nodo.getDato()))

            # Primero derecha, luego izquierda (para que la izquierda se procese primero)
            if nodo.getDerecha():
                pila.append(nodo.getDerecha())
            if nodo.getIzquierda():
                pila.append(nodo.getIzquierda())

        return ", ".join(resultado)

    def contarNodos(self):
        return self.__contarNodos(self.__raiz)

    def __contarNodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.__contarNodos(nodo.getIzquierda()) + self.__contarNodos(nodo.getDerecha())
    
    def DFS(self):
        return self.preOrden()

    def BFS(self):
        if self.__raiz is None:
            return ""

        resultado = []
        cola = [self.__raiz]
        while cola:
            nodo = cola.pop(0)  # Sacamos el nodo más antiguo de la cola
            resultado.append(str(nodo.getDato()))  # Procesamos el nodo

            # Agregamos los hijos izquierdo y derecho a la cola
            if nodo.getIzquierda():
                cola.append(nodo.getIzquierda())
            if nodo.getDerecha():
                cola.append(nodo.getDerecha())

        return " ".join(resultado)
    
    # Metodos de Eliminacion
    def __buscarPadre(self, nodo):
        padre = self.__raiz
        while padre:
            if padre.getDerecha() == nodo:
                return padre
                
            elif padre.getIzquierda() == nodo:
                return padre
                
            elif padre.getDato() < nodo.getDato():
                padre = padre.getDerecha()
            
            else:
                padre = padre.getIzquierda()
        
        return None
    
    
    def __encontrarSucesor(self, nodo):
        sucesor = nodo.getDerecha()
        while sucesor.getIzquierda():
            sucesor = sucesor.getIzquierda()
            
        return sucesor
    
    def __eliminar1(self, nodo):
        if nodo == self.__raiz:
            self.__raiz = None
        else:
            padre = self.__buscarPadre(nodo)
            if padre:
                if padre.getIzquierda() == nodo:
                    padre.setIzquierda(None)
                else:
                    padre.setDerecha(None)
    
    
    def __esIncompleto(self, nodo):
        return nodo.getIzquierda() is None or nodo.getDerecha() is None
    
    
    def __eliminar2(self, nodo):
        if nodo == self.__raiz:
            if nodo.getDerecha():
                self.__raiz = nodo.getDerecha()
            else:
                self.__raiz = nodo.getIzquierda()
            return
                
        padre = self.__buscarPadre(nodo)
        if padre.getDerecha() == nodo:
            if nodo.getDerecha():
                padre.setDerecha(nodo.getDerecha())
            
            else:
                padre.setDerecha(nodo.getIzquierda())
                
        else:
            if nodo.getDerecha() is not None:
                padre.setIzquierda(nodo.getDerecha())
            
            else:
                padre.setIzquierda(nodo.getIzquierda())
    
    
    def __esCompleto(self, nodo):   
        return nodo.getDerecha() is not None and nodo.getIzquierda() is not None
    
    
    def __eliminar3(self, nodo):
        sucesor = self.__encontrarSucesor(nodo)
        dato = sucesor.getDato()
        if self.esHoja(sucesor):
            self.__eliminar1(sucesor) 
        else:
            self.__eliminar2(sucesor)
        nodo.setDato(dato)
    
    
    def eliminarNodo(self, x):
        nodo = self.buscar(x)
        
        # Caso 1: El nodo es Hoja
        if self.esHoja(nodo):
            self.__eliminar1(nodo)
            
        # Caso 2: El nodo es Incompleto
        elif self.__esIncompleto(nodo):
            self.__eliminar2(nodo)
            
        # Caso 3: El nodo es Completo
        elif self.__esCompleto(nodo):
            self.__eliminar3(nodo)