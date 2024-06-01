<p align="center">
  <h1><center> 	&#127979; Apprendre le Deep Learning à partir de zéro &#127979; </center></h1>
</p>

# Description
Ce repository propose des cours d'initiation au deep learning se basant sur des notebooks.
Pour un débutant, les cours sont à faire dans l'ordre pour une meilleur compréhension globale. 

### Installation de l'environnement de travail 
L'ensemble des library nécessaires pour le cours sont disponibles dans requirements.txt, vous pouvez choisir d'installer tout d'un coup ou au fur et à mesure de votre avancement dans le cours.   
Il est conseillé d'utiliser un environnement de travail conda pour éviter tout conflit avec des library déjà installé sur votre ordinateur.  

```
`pip install -r requirements.txt`
```


## Fondations
Le premier cours "Fondations" introduit les bases de l'optimisation par descente du gradient avec une compréhension intuitive. La règle de la chaîne est introduite puis un premier exemple de regression logistique est présenté. 
<!-- Lorsque le premier cours est bien compris, il est recommandé de faire la partie exercice avant de passer aux cours suivants.  -->

## Réseau Fully Connected
Le second cours "RéseauFullyConnected" introduit le fonctionnement d'un réseau de neurones avec d'abord un exemple d'un réseau codé avec [micrograd](https://github.com/karpathy/micrograd/tree/master) pour permettre d'explorer cette library pour bien comprendre le fonctionnement. Une version française MicrogradFR est disponible dans ce repository.   
Ensuite, pour introduire la library pytorch, le même exemple est reconstruit mais en utilisant pytorch au lieu de micrograd.  
Le dernier notebook de cette partie introduit des techniques avancées d'entraînement de réseau de neurones qu'il est utile de connaître pour améliorer les performances de nos réseaux. 



## TODO
 - [x] Cours sur les fondations
 - [x] Cours sur les réseau fully connected 
 - [x] Cours sur les CNN  
 - [x] Cours sur les AutoEncoders 
 - [ ] Cours sur les Transformers (Concept et Hugging Face library)
 - [ ] Cours sur les RNN 
 - [ ] Cours sur le transfer learning (fine tuning surtout)
 - [ ] Exercices d'entraînement Fondations  
 - [ ] Exercices d'entraînement RéseauFullyConnected  
 - [ ] Cours spécifiques sur Regularization (intuition etc)  
 - [ ] Cours spécifiques sur Dropout (intuition etc)  
 - [ ] Cours spécifiques sur BatchNorm (intuition etc)  
