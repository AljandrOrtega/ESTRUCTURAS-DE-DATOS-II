class NodoArbol:
    def __init__(self, claves, hijos):
        self.__claves = claves      # Lista de claves (keys)
        self.__hijos = hijos        # Lista de hijos (children)

    # Getter para claves
    @property
    def claves(self):
        return self.__claves

    # Setter para claves
    @claves.setter
    def claves(self, nuevas_claves):
        self.__claves = nuevas_claves

    # Getter para hijos
    @property
    def hijos(self):
        return self.__hijos

    # Setter para hijos
    @hijos.setter
    def hijos(self, nuevos_hijos):
        self.__hijos = nuevos_hijos
