# 🤖 Transformers 🤖
Ce cours est dédié à l'architecture du transformers. Après avoir vu ses applications dans le cours précédent. Nous allons entrer dans le détail de l'architecture pour en comprendre les mécanismes. Le premier notebook est grandement inspiré de la vidéo [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=1806s&ab_channel=AndrejKarpathy) de Andrej Karpathy et propose une implémentation pas à pas d'un encodeur transformers. Le but de ce notebook sera de créer un modèle capable de générer du "Molière" automatiquement. La seconde partie est une approche plus mathématique et la présentation de la partie encodeur du transformers. La troisième partie présente des architectures de modèle reposant sur la couche transformers pour de nombreux cas d'applications (Vision, traduction etc ...). Enfin, une dernière partie propose une implémentation du vision transformer à partir de l'article original.

## Notebook 1️⃣ : [Introduction](01_Introduction.ipynb)
Ce notebook introduit brièvement l'architecture transformer et présente un plan de cours.

## Notebook 2️⃣ : [GPT from scratch](02_GptFromScratch.ipynb)
Ce notebook présente une implémentation d'un *generative pretrained transformer* à partir de zéro.

## Notebook 3️⃣ : [Training our GPT](03_TrainingOurGpt.ipynb)
Ce notebook reprend les éléments implémentés dans le notebook précédent et entraîne un modèle GPT pour la prédiction du prochain caractère.

## Notebook 4️⃣ : [Architecture et particularités](04_ArchitectureEtParticularités.ipynb)
Ce notebook décrit formellement l'architecture du transformer en présentant les différents blocks (encoder et decoder).

## Notebook 5️⃣ : [Utilisations possibles](05_UtilisationsPossibles.ipynb)
Ce notebook présente différentes utilisations de l'architecture transformer pour divers problèmes dans le domaine du NLP et de la vision.

## Notebook 6️⃣ : [Vision Transformer Implementation](06_VisionTransformerImplementation.ipynb)
Ce notebook propose une implémentation de l'architecture du Vision Transformer.

## Notebook 7️⃣ : [Swin Transformer](07_SwinTransformer.ipynb)
Ce notebook propose une implémentation de l'architecture du Swin Transformer.