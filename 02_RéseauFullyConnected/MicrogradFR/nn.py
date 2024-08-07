import random
from engine import Value

# Definnition de la classe Module
class Module:
    # Mise à zéro des gradients 
    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0

    def parameters(self):
        return []

# Définition de la classe Neuron
class Neuron(Module):

    def __init__(self, nin, nonlin=True):
        # Chaque neurone a un vecteur de poids w et un biais bs
        self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]
        self.b = Value(0)
        # Utilisation ou non de la fonction d'activation ReLU
        self.nonlin = nonlin


    def __call__(self, x):
        act = sum((wi*xi for wi,xi in zip(self.w, x)), self.b)
        return act.relu() if self.nonlin else act

    def parameters(self):
        return self.w + [self.b]

    def __repr__(self):
        return f"{'ReLU' if self.nonlin else 'Linear'}Neuron({len(self.w)})"

# Définition de la classe Layer
class Layer(Module):

    def __init__(self, nin, nout, **kwargs):
        # Permet de créer nout neurones prenant nin entrées
        self.neurons = [Neuron(nin, **kwargs) for _ in range(nout)]

    def __call__(self, x):
        out = [n(x) for n in self.neurons]
        return out[0] if len(out) == 1 else out

    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]

    def __repr__(self):
        return f"Layer of [{', '.join(str(n) for n in self.neurons)}]"

# Définition de la classe MLP
class MLP(Module):

    def __init__(self, nin, nouts):
        sz = [nin] + nouts
        # Permet de créer nin input et avec des couches de taille nouts[i]
        self.layers = [Layer(sz[i], sz[i+1], nonlin=i!=len(nouts)-1) for i in range(len(nouts))]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]

    def __repr__(self):
        return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"