# 🖼️ Réseaux convolutifs 🖼️ 
Ce cours aborde tout d'abord le principe de fonctionnement des couches de convolution puis montre comment on les utilise au sein d'un réseau de neurones. Plusieurs exemples sont ensuite abordés pour montrer les capacités d'un réseau convolutif : classification sur MNIST, classification sur CIFAR-10 et segmentation sur "Oxford-IIIT Pet Dataset".

## Notebook 1️⃣ : [Couches de convolutions](01_CouchesDeConvolutions.ipynb)
Ce notebook introduit les couches de convolutions en expliquant la motivation principale derrière cette architecture puis en introduisant les différents paramètres pour les utiliser. Les couches de pooling sont également introduites.

## Notebook 2️⃣ : [Réseau Convolutif](02_RéseauConvolutif.ipynb)
Ce notebook introduit l'architecture du réseau de neurones convolutifs avec une explication de la logique derrière cette architecture ainsi que la description du concept de champ réceptif.

## Notebook 3️⃣ : [Conv Implementation](03_ConvImplementation.ipynb)
Ce notebook propose une implémentation d'une couche de convolution 1D à partir de zéro et son utilisation pour la classification sur le dataset MNIST. Une implémentation de la convolution 2D est ensuite proposée pour voir si l'on obtient de meilleurs résultats.

## Notebook 4️⃣ : [Réseau Convolutif Pytorch](04_RéseauConvolutifPytorch.ipynb)
Ce notebook propose une implémentation d'un premier réseau convolutif sur le dataset MNIST.

## Notebook 5️⃣ : [Application Classification](05_ApplicationClassification.ipynb)
Ce notebook montre l'intêret des réseaux convolutifs en proposant une implémentation d'un modèle de classification sur le dataset CIFAR-10.

## Notebook 6️⃣ : [Application Segmentation](06_ApplicationSegmentation.ipynb)
Dans ce notebook, le problème de la segmentation d'objets est introduit et une implémentation est proposée pour segmenter les chiens et les chats sur le dataset Oxford-IIIT Pet.