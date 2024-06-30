<p align="center">
  <h1><center> 	🚀 Apprendre le Deep Learning à partir de zéro 🚀</h1>
</p>

# 📚 Description
Ce repository propose des cours d'initiation au deep learning se basant sur des notebooks.
Pour un débutant, les cours sont à faire dans l'ordre pour une meilleur compréhension globale. 

## 🛠️ Installation de l'environnement de travail 
L'ensemble des library nécessaires pour le cours sont disponibles dans requirements.txt, vous pouvez choisir d'installer tout d'un coup ou au fur et à mesure de votre avancement dans le cours.   
Il est conseillé d'utiliser un environnement de travail conda pour éviter tout conflit avec des library déjà installé sur votre ordinateur.  

```
`pip install -r requirements.txt`
```

# 🗺️ Plan du cours
## 1. 🏗️ Fondations
Le premier cours "Fondations" introduit les bases de l'optimisation par descente du gradient avec une compréhension intuitive. La règle de la chaîne est introduite puis un premier exemple de regression logistique est présenté. 

## 2. 🧠 Réseau Fully Connected
Le deuxième cours "RéseauFullyConnected" introduit le fonctionnement d'un réseau de neurones avec d'abord un exemple d'un réseau codé avec [micrograd](https://github.com/karpathy/micrograd/tree/master) pour permettre d'explorer cette library pour bien comprendre le fonctionnement. Une version française MicrogradFR est disponible dans ce repository.   
Ensuite, pour introduire la library pytorch, le même exemple est reconstruit mais en utilisant pytorch au lieu de micrograd.  
Le dernier notebook de cette partie introduit des techniques avancées d'entraînement de réseau de neurones qu'il est utile de connaître pour améliorer les performances de nos réseaux. 

## 3. 🖼️ Réseaux convolutifs
Le troisième cours "RéseauConvolutifs" aborde tout d'abord le principe de fonctionnement des couches de convolution puis montre comment on les utilise au sein d'un réseau de neurones. Plusieurs exemples sont ensuite abordés pour montrer les capacités d'un réseau convolutif : classification sur MNIST, classification sur CIFAR-10 et segmentation sur "Oxford-IIIT Pet Dataset". 

## 4. 🔄 Autoencodeurs
Le quatrième cours "Autoencodeurs" aborde la notion d'entraînement non supervisé en présentant les différences entre supervisé et non supervisé. L'exemple de l'autoencodeur est ensuite abordé ainsi que son application pour la détection d'anomalies non supervisée. Pour finir, un notebook montre le potentiel de l'autoencodeur pour le problème du "denoising". 

## 5. 🗨️ NLP
Le cinquième cours "NLP" est grandement inspiré de la série de vidéo de Andrej Karpathy ["Building makemore"](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) qui traîte les NLP avec une approche de prédiction du prochain token. Le cours aborde d'abord des modèles très simples pour avoir une intuition sur le traîtement de données discrètes avec un réseau neurones puis les modèles se complexifient petit à petit. 

## 6. 🤗 Hugging Face
Le sixième cours "HuggingFace" est dédié à une exploration des librarys, des modèles, des datasets et autres de [Hugging Face](https://huggingface.co/). C'est une plateforme regroupant énormement des modèles open source pour une grande variété de tâches avec une library pour les implémenter rapidement et efficacement en python. Le cours présente d'abord le site de Hugging Face pour ensuite présenter les fonctionnalités des différentes librarys (transformers et diffusers principalement) sur différents cas d'usage. Le dernier notebook présente brièvement gradio, une library pour créer des interfaces simples de démo.

## 7. 🤖 Transformers
Le septième cours "Transformers" est dédié à l'architecture du transformers. Après avoir vu ses applications dans le cours précédent. Nous allons entrer dans le détail de l'architecture pour en comprendre les mécanismes. Le premier notebook est grandement inspiré de la vidéo [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=1806s&ab_channel=AndrejKarpathy) de Andrej Karpathy et propose une implémentation pas à pas d'un encodeur transformers. Le but de ce notebook sera de créer un modèle capable de générer du "Molière" automatiquement. La seconde partie est une approche plus mathématique et la présentation de la partie encodeur du transformers. La troisième partie présente des architectures de modèle reposant sur la couche transformers pour de nombreux cas d'applications (Vision, traduction etc ...). Enfin, une dernière partie propose une implémentation du vision transformer à partir de l'article original.

## 8. 🔍 Detection
Le huitième cours "Detection" présente le fonctionnement de la détection d'objets sur des images. L'introduction présente ce qu'est la détection et les deux méthodes classiques (two-stage et one-stage). Le notebook suivant propose une description précise du fonctionnement de [YOLO](https://arxiv.org/pdf/1506.02640) et le dernier notebook présente la library [ultralytics](https://www.ultralytics.com/) qui permet d'accèder aux modèles YOLO très simplement.

## 9. 🎯 Entrainement contrastif
Le neuvième cours "Entrainement contrastif" présente le concept de l'entraînement contrastif. Un premier notebook présente ce qu'est l'entraînement contrastif en se basant sur l'implémentation d'un article de "face verification". Le second notebook présente la place de l'entraînment contrastif dans le deep learning récent et notamment son intêret pour l'entrainement non supervisé. 

## 10. 🤝 Transfer learning et distillation
Le dixième cours "Transfer learning et distillation" présente deux concepts majeurs en deep learning : le transfer learning et la distillation des connaissances. La première partie de ce cours présente le transfer learning dans sa globalité puis propose une implémentation pratique. La seconde partie présente le concept de distillation des connaissances et ses variantes puis propose un cas d'application de la distillation des connaissances pour la détection d'anomalies non supervisée.

## Bonus 🌟 Cours spécifiques
Ce cours présente des concepts très intéressant à comprendre mais non essentiels dans une pratique courante du deep learning. Si vous êtes intéressé par comprendre le fonctionnement d'un réseau de neurones de manière plus approfondie et de découvrir la raison de l'utilisation de techniques comme la BatchNorm, les connexions résiduelles, les optimizers, le dropout, la data augmentation etc ..., ce cours est fait pour vous ! 

# 📌 TODO
 - [x] Cours sur les fondations
 - [x] Cours sur les réseau fully connected 
 - [x] Cours sur les CNN  
 - [x] Cours sur les AutoEncoders 
 - [x] Cours sur le NLP (Karpathy makemore)
 - [x] Cours sur Hugging Face
 - [x] Cours sur les Transformers (Concept et applications sur NLP + vidéo karpathy)
 - [x] Cours sur la détection d'objets(Yolo principalement)
 - [x] Cours sur les RNN (inclu dans NLP)
 - [x] Cours sur le transfer learning et distillation 
 - [x] Cours sur le contrastive training (siamese nets, triplet loss, entrainement non supervisé)
 - [x] Cours spécifique sur l'initialisation 
 - [x] Cours spécifique sur BatchNorm 
 - [x] Cours spécifique sur Regularization (l2 et dropout)
 - [x] Cours spécifique sur les connections résiduelles 
 - [x] Cours spécifique sur les optimizers
 - [x] Cours spécifique sur la data augmentation
 - [ ] Cours sur la génération d'images


**License**

Ce travail est mis à disposition selon les termes de la licence MIT