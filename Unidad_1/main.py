import tkinter as tk
from Window import InterfazABB

def main():
    raiz = tk.Tk()
    app = InterfazABB(raiz)
    raiz.mainloop()
    
if __name__ == "__main__":
    main()