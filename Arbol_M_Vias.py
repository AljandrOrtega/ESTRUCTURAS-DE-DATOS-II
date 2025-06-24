from Nodo import NodoArbol

class ArbolMVias:
    """
    Representa un árbol M-vías, donde cada nodo puede tener hasta M hijos y M-1 claves.
    Este tipo de árbol es útil para organizar datos jerárquicamente, como en bases de datos o sistemas de archivos.
    """

    def __init__(self, m):
        """
        Inicializa el árbol M-vías con un orden dado.

        :param m: Orden del árbol (número máximo de hijos por nodo)
        """
        self.__m = m  # Orden del árbol (máximo número de hijos)
        self.__raiz = None

    def insertar(self, clave):
        """
        Inserta una clave en el árbol M-vías.

        :param clave: La clave a insertar
        """
        if self.__raiz is None:
            # Árbol vacío, se crea la raíz con la clave
            self.__raiz = NodoArbol([clave], [])
            return

        nodo_actual = self.__raiz
        camino = []

        # Buscar la hoja apropiada para insertar la clave
        while nodo_actual:
            camino.append(nodo_actual)
            i = 0
            while i < len(nodo_actual.claves) and clave > nodo_actual.claves[i]:
                i += 1

            if i < len(nodo_actual.claves) and clave == nodo_actual.claves[i]:
                return  # La clave ya existe, no se inserta

            if len(nodo_actual.hijos) > 0:
                # Continuar al hijo correspondiente
                if i < len(nodo_actual.hijos):
                    nodo_actual = nodo_actual.hijos[i]
                else:
                    nodo_actual = None  # Caso anómalo, no debería pasar
            else:
                break  # Nodo hoja alcanzado

        # Insertar la clave en el nodo hoja
        padre = camino[-1]
        i = 0
        while i < len(padre.claves) and clave > padre.claves[i]:
            i += 1
        padre.claves.insert(i, clave)

        # Dividir nodos si se excede el número de claves permitidas
        while len(padre.claves) > self.__m - 1:
            if padre == self.__raiz:
                self.dividir_raiz()
                break
            elif len(camino) >= 2:
                padre_anterior = camino[-2]
                self.dividir_hijo(padre_anterior, padre)
                camino.pop()  # Quitar el nodo que fue dividido
                padre = padre_anterior  # Subir un nivel
            else:
                break  # No hay más niveles hacia arriba


    def dividir_raiz(self):
        """
        Divide la raíz si excede la cantidad máxima de claves permitidas.
        Crea una nueva raíz con la clave del medio y dos hijos.
        """
        vieja_raiz = self.__raiz
        medio = vieja_raiz.claves[(self.__m - 1) // 2]
        nueva_raiz = NodoArbol([medio], [])

        # Dividir las claves e hijos en dos nodos hijos
        hijo_izquierdo = NodoArbol(
            vieja_raiz.claves[:(self.__m - 1) // 2],
            vieja_raiz.hijos[:len(vieja_raiz.hijos)//2 + 1 if len(vieja_raiz.hijos) > 0 else 0]
        )

        hijo_derecho = NodoArbol(
            vieja_raiz.claves[(self.__m - 1) // 2 + 1:],
            vieja_raiz.hijos[len(vieja_raiz.hijos)//2 + 1 if len(vieja_raiz.hijos) > 0 else 0:]
        )

        # Actualizar hijos de la nueva raíz
        nueva_raiz.hijos.append(hijo_izquierdo)
        nueva_raiz.hijos.append(hijo_derecho)
        self.raiz = nueva_raiz

    def dividir_hijo(self, padre, hijo):
        """
        Divide un hijo que se ha llenado con demasiadas claves.

        :param padre: Nodo padre del hijo a dividir
        :param hijo: Nodo que debe dividirse
        """
        indice = padre.hijos.index(hijo)
        medio = hijo.claves[(self.__m - 1) // 2]

        # Crear nodos izquierdo y derecho del hijo
        hermano_izquierdo = NodoArbol(
            hijo.claves[:(self.__m - 1) // 2],
            hijo.hijos[:len(hijo.hijos)//2 + 1 if len(hijo.hijos) > 0 else 0]
        )

        hermano_derecho = NodoArbol(
            hijo.claves[(self.__m - 1) // 2 + 1:],
            hijo.hijos[len(hijo.hijos)//2 + 1 if len(hijo.hijos) > 0 else 0:]
        )

        # Insertar clave media en el padre
        padre.claves.insert(indice, medio)

        # Reemplazar el hijo dividido por los dos nuevos hijos
        padre.hijos.pop(indice)
        padre.hijos.insert(indice, hermano_derecho)
        padre.hijos.insert(indice, hermano_izquierdo)

    def buscar(self, clave):
        """
        Busca una clave en el árbol.

        :param clave: Clave a buscar
        :return: True si la clave se encuentra, False si no
        """
        nodo_actual = self.raiz
        while nodo_actual:
            i = 0
            while i < len(nodo_actual.claves) and clave > nodo_actual.claves[i]:
                i += 1
            if i < len(nodo_actual.claves) and clave == nodo_actual.claves[i]:
                return True  # Clave encontrada
            if len(nodo_actual.hijos) > 0:
                if i < len(nodo_actual.hijos):
                    nodo_actual = nodo_actual.hijos[i]
                else:
                    return False  # Estructura inconsistente
            else:
                return False  # Nodo hoja y no encontrada
        return False

    def recorrido_inorden(self, nodo):
        """
        Realiza un recorrido inorden del árbol (izquierda, raíz, derecha).

        :param nodo: Nodo actual a recorrer
        """
        if nodo:
            for i in range(len(nodo.claves)):
                # Recorrer hijo izquierdo si existe
                if len(nodo.hijos) > i:
                    self.recorrido_inorden(nodo.hijos[i])
                print(nodo.claves[i], end=" ")
            # Recorrer último hijo si existe
            if len(nodo.hijos) > len(nodo.claves):
                self.recorrido_inorden(nodo.hijos[len(nodo.claves)])
