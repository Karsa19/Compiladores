from arbol import tree, Node


class Thompson(object):

    arbol = Node(token='*')

    def __init__(self):
        self.arbol.left = Node(token='a')
        self.arbol.right = Node(token='b')
        self.arbol.right.left = Node(token='.')
        self.arbol.right.right = Node(token='x')
        self.arbol.right.right.left = Node(token='+')
        print(str(self.arbol))
        pass

    
    def crear_arbol(self, expresion):

    def exp_epsilon(self):
        pass

    def exp_a(self):
        pass

    def exp_or(self):
        pass

    def exp_concatenacion(self):
        pass

    def cerradura_estrella(self):
        pass


