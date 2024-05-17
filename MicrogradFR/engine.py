
class Value:
    """ Classe permettant de stocker un scalaire et son gradient, permet aussi de faire des opérations sur cet objet"""

    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0 # le gradient est initialisé à 0
        
        self._backward = lambda: None # initilisation avec la fonction None 
        self._prev = set(_children) # Initialise la valeur en amont dans le graphe
        self._op = _op # L'opération qui a produit ce noeud pour visualisation et debugging

    # Méthode d'ajout, la méthode __add__ sur une classe python correspond à l'opérateur '+'
    def __add__(self, other): #self+other
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')

        # Le backward permet de définir l'opération à effectuer lors de la descente de gradient
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward

        return out

    # Méthode de multiplication, la méthode __mul__ sur une classe python correspond à l'opérateur '*'
    def __mul__(self, other): #self*other
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward

        return out

    # Méthode de puissance, la méthode __pow__ sur une classe python correspond à l'opérateur '**'
    def __pow__(self, other): ##self**other
        assert isinstance(other, (int, float)), "ne supporte que les int et float pour le moment"
        out = Value(self.data**other, (self,), f'**{other}')

        def _backward():
            self.grad += (other * self.data**(other-1)) * out.grad
        out._backward = _backward

        return out

    # La fonction d'activation ReLU, l'output vaut 0 si l'input est inférieur à 0, sinon il est égal à l'input
    def relu(self):
        out = Value(0 if self.data < 0 else self.data, (self,), 'ReLU')

        def _backward():
            self.grad += (out.data > 0) * out.grad
        out._backward = _backward

        return out

    # Fonction backward qui permet de calculer les gradients sur l'ensemble du graphe relativement à ce noeud
    def backward(self):

        # ordre topologique de tous les noeuds enfant du graphe 
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        # Calcule le gradient de chaque varible une par une et applique la règle de la chaîne pour calculer son gradient
        self.grad = 1
        for v in reversed(topo):
            v._backward()

    # Méthode de négation, la méthode __neg__ sur une classe python correspond à l'opérateur pour passer de x à -x
    def __neg__(self): # -self
        return self * -1
    
    # Méthode de négation, la méthode __neg__ sur une classe python correspond à l'opérateur pour passer de x à -x
    def __radd__(self, other): # other + self
        return self + other

    # Méthode de soustraction, la méthode __neg__ sur une classe python correspond à l'opérateur '-'
    def __sub__(self, other): # self - other
        return self + (-other)

    # Méthode de soustraction, permet de pouvoir réaliser l'opération other - self même si other n'est pas une Value
    def __rsub__(self, other): # other - self
        return other + (-self)

    # Méthode de multiplication, permet de pouvoir réaliser l'opération other * self même si other n'est pas une Value
    def __rmul__(self, other): # other * self
        return self * other

    # Méthode de division, la méthode __truediv__ sur une classe python correspond à l'opérateur '/'
    def __truediv__(self, other): # self / other
        return self * other**-1
    
    # Méthode de division, permet de pouvoir réaliser l'opération other / self même si other n'est pas une Value
    def __rtruediv__(self, other): # other / self
        return other * self**-1

    # Méthode de representation d'un objet, donne les informations importantes d'un objet, c'est ce qui va 
    # s'afficher lorsqu'on fait print()
    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"