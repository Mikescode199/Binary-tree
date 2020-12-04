numeros = [3,5,8,8,4,6,4,6,8,36]
letras = ['A','H','J','C','B']

class Tree(): 
    def inOrder(self, Lista_ordenar):
        self.Lista_ordenar = Lista_ordenar
        print(sorted(Lista_ordenar))
        
t = Tree()
t.inOrder(letras)
t.inOrder(numeros)


