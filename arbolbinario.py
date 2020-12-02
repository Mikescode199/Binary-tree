import os
import time

segundos = 0.8

class node():
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato

class arbol():
    def __init__(self):
        self.root = None
        
    def insert(self, a, dato):
        if a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d:
                a.left = self.insert(a.left, dato)
            else:
                a.right = self.insert(a.right, dato)
        return a

    def inorder(self, a):
        if a == None:
            return None
        else:
            self.inorder(a.left)
            print(a.dato)
            self.inorder(a.right)

    def preorder(self, a):
        if a == None:
            return None
        else:
            print(a.dato)
            self.preorder(a.left)
            self.preorder(a.right)

    def postorder(self, a):
        if a == None:
            return None
        else:
            self.postorder(a.left)
            self.postorder(a.right)
            print(a.dato)

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)

tree = arbol()

while True:
    try: 
        os.system("clear")
        print("Arbol Mike")
        opc = input("\n1.-Insertar nodo \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Salir \n\nElige una opcion -> ")
    
    except ValueError:
        print("\nIngresa solo digitos...")
        time.sleep(segundos)

    if opc == '1':
        try:
            nodo = input("\nIngresa el nodo -> ")
            nodo = int(nodo)
            tree.root = tree.insert(tree.root, nodo)
            
        except ValueError:
            print("\nIngresa solo digitos...")

    elif opc == '2':
        if tree.root == None:
            print("Vacio")
        else:
            tree.inorder(tree.root)

    elif opc == '3':
        if tree.root == None:
            print("Vacio")
        else:
            tree.preorder(tree.root)

    elif opc == '4':
        if tree.root == None:
            print("Vacio")
        else:

            tree.postorder(tree.root)
    elif opc == '5':
        try:
            nodo = int(input("\nIngresa el nodo a buscar -> "))
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) == None:
                print("\nNodo no encontrado...")
            else:
                print("\nNodo encontrado -> ",tree.buscar(nodo, tree.root), " si existe...")
        except ValueError:
            print("\nIngresa solo digitos...") 

    elif opc == '6':
        print("\nElegiste salir...\n")
        time.sleep(segundos)
        break
    time.sleep(segundos)