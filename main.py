from Arbol_M_Vias import ArbolMVias

def main():
    """
    Función principal que crea un árbol M-vías, inserta claves,
    realiza búsquedas y muestra el recorrido inorden.
    """
    # Crear un árbol M-vías con orden 4
    arbol_m = ArbolMVias(4)

    # Insertar valores
    arbol_m.insertar(10)
    arbol_m.insertar(20)
    arbol_m.insertar(5)
    arbol_m.insertar(15)
    arbol_m.insertar(25)
    arbol_m.insertar(30)
    arbol_m.insertar(7)
    arbol_m.insertar(12)

    # Buscar claves
    print(f"Buscar 15: {arbol_m.buscar(15)}")
    print(f"Buscar 100: {arbol_m.buscar(100)}")

    # Recorrido inorden
    print("Recorrido Inorden:")
    arbol_m.recorrido_inorden(arbol_m.raiz)
    print()

if __name__ == "__main__":
    main()
