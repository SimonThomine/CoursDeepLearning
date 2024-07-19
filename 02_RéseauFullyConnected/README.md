# 🧠 Réseau Fully Connected 🧠 
Ce cours introduit le fonctionnement d'un réseau de neurones avec d'abord un exemple d'un réseau codé avec [micrograd](https://github.com/karpathy/micrograd/tree/master) pour permettre d'explorer cette library pour bien comprendre le fonctionnement. Une [version française MicrogradFR](../MicrogradFR/README.md) est disponible dans ce repository.   
Ensuite, pour introduire la library pytorch, le même exemple est reconstruit mais en utilisant pytorch au lieu de micrograd.  
Le dernier notebook de cette partie introduit des techniques avancées d'entraînement de réseau de neurones qu'il est utile de connaître pour améliorer les performances de nos réseaux. 

## Notebook 1️⃣ : [Mon premier réseau](01_MonPremierRéseau.ipynb)
Ce notebook propose une première implementation d'un réseau de neurones avec la library micrograd. Un dataset aléatoire est crée et on utilise la descente du gradient stochastique pour entraîner le modèle.

## Notebook 2️⃣ : [Pytorch introduction](02_PytorchIntroduction.ipynb)
Ce notebook résout exactement le même problème que le notebook précédent mais en utilisant la library pytorch. La library pytorch est l'une des library les plus utilisées en Deep Learning et il est important de savoir s'en servir.

## Notebook 3️⃣ : [Techniques avancées](03_TechniquesAvancées.ipynb)
Ce notebook s'attaque au problème plus complexe de classification de chiffres sur la dataset MNIST. Des techniques de régularisation ainsi que la BatchNorm sont également introduites.