# micrograd en français
Cette library reprend l'implémentation de [micrograd](https://github.com/karpathy/micrograd/tree/master) de Andrej Karpathy avec un ajout de commentaire en version française. 
Pour comprendre micrograd dans son entiereté, veuillez vous réferer à la [vidéo youtube](https://www.youtube.com/watch?v=VMj-3S1tku0&t=3s&ab_channel=AndrejKarpathy) d'Andrej Karpathy qui montre la création de la librairy et qui est une excellente introduction aux réseaux de neurones. 
Le but étant d'utiliser une library compréhensible par un étudiant plutôt que pytorch directement

<p align="left">
  <img width="700" height="500" src="images/microgradFR.png">
</p>

Cette library contient petit Autograd engine qui permet d'effectuer la retropropagation du gradient sur un graphe construit dynamiquement et contient également une library pour construire un petit réseau de neurones. L'API est similaire à celle de Pytorch. Les deux fichiers sont petits (50 et 100 lignes environ). Le graphe n'opére que sur des scalaires et il est donc nécessaire de découper chaque neurone en petites additions et multiplications. C'est cependant suffisant pour construie des réseaux de neurones de base pouvant être utilisé à des fins éducatives. 

### Installation
Il est possible d'installer micrograd directement avec pip.

```bash
pip install micrograd
```


### Exemple d'utilisation

En dessous, voici un petit exemple montrant les opérations possibles pour la classe Value()

```python
from micrograd.engine import Value

a = Value(-4.0)
b = Value(2.0)
c = a + b
d = a * b + b**3
c += c + 1
c += 1 + c + (-a)
d += d * 2 + (b + a).relu()
d += 3 * d + (b - a).relu()
e = c - d
f = e**2
g = f / 2.0
g += 10.0 / f
print(f'{g.data:.4f}') # prints 24.7041, La sortie
g.backward() # Calcule la rétropropagation du gradient
print(f'{a.grad:.4f}') # prints 138.8338, i.e. la valeur numérique dg/da
print(f'{b.grad:.4f}') # prints 645.5773, i.e. la valeur numérique of dg/db
```

### Entrainement d'un réseau de neurones
Le notebook 'demo.ipynb' offre une démonstration complète de l'entrainement d'un réseau de neurones (MLP) de deux couches pour la classification binaire. C'est réalisé en initialisant un réseau de neurones depuis le module micrograd.nn, en implémentant un svm "max-margin" loss de classification et utilisant la descente de gradient stochastique pour l'optimisation (SGD). Comme montré dans le notebook, un réseau de neurones de 2 couches de 16 neurones chacune permet d'obtenir la classification suivante sur le dataset moon : 

![2d neuron](images/moon_mlp.png)

### Visualisation

Pour plus de simplicité, le notebook `trace_graph.ipynb` montre comment produite une visualisation graphviz. La visualisation ci-dessous est un simple neurone 2D, que l'on a tracé en appelant la fonction `draw_dot` du code ci-dessous. Cette visualisation montre à la fois les données (nombre de gauche de chaque noeud) et le gradient (nombre de droite de chaque noeud).

```python
from micrograd import nn
n = nn.Neuron(2)
x = [Value(1.0), Value(-2.0)]
y = n(x)
dot = draw_dot(y)
```

![2d neuron](images/gout.svg)

### Test unitaires
Pour lancer les tests unitaires, vous devez installer [PyTorch](https://pytorch.org/), que les tests utilisent comme une réference pour vérifier la valeur des gradients calculés. Ensuite il suffit de faire :

```bash
python -m pytest
```

### License

MIT