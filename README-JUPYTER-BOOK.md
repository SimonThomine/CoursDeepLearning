# 🎓 Cours Deep Learning - Jupyter Book Multilingue

Ce dépôt contient un cours complet de Deep Learning disponible en français et en anglais, construit avec Jupyter Book.

## 🌐 Versions linguistiques

- **🇫🇷 Français** : Cours complet en français avec tout le contenu original
- **🇺🇸 English** : Traduction anglaise (en cours de développement)

## 🚀 Démarrage rapide

### Prérequis

```bash
pip install -r requirements-jupyter-book.txt
```

### Construction et test

```bash
# Construction des deux versions
python build_multilingual.py

# Test local avec serveur
python test_local.py
```

### Visualisation

Après construction, ouvrez le sélecteur de langue :
```bash
open index.html  # macOS
xdg-open index.html  # Linux
```

## 📁 Structure du projet

```
CoursDeepLearning/
├── 🇫🇷 fr/                     # Version française complète
│   ├── _config.yml              # Configuration française
│   ├── _toc.yml                 # Table des matières française
│   ├── intro.md                 # Introduction française
│   └── [contenu du cours]/      # Tout le matériel de cours
├── 🇺🇸 en/                     # Version anglaise
│   ├── _config.yml              # Configuration anglaise
│   ├── _toc.yml                 # Table des matières anglaise
│   └── [contenu du cours]/      # Matériel de cours en anglais
├── 📚 cours/                    # Contenu original (source)
├── 🔨 build_multilingual.py    # Script de construction
├── 🧪 test_local.py            # Test local avec serveur
├── 🔄 translate_content.py     # Aide à la traduction
├── 🚀 deploy.sh               # Déploiement GitHub Pages
├── 🌐 index.html              # Sélecteur de langue
├── 📖 LANGUAGE_SWITCHING.md   # Guide technique
└── 🔧 requirements-jupyter-book.txt  # Dépendances Jupyter Book
```

## 📚 Contenu du cours

### **12 sections principales** :
1. 🧮 **Fondations** - Dérivées, gradient descent, régression logistique
2. 🔗 **Réseaux Fully Connected** - Premiers réseaux, PyTorch
3. 🖼️ **Réseaux Convolutifs** - CNN, applications vision
4. 🔄 **Autoencodeurs** - AE classiques et débruiteurs
5. 📝 **NLP** - RNN, LSTM, techniques modernes
6. 🤗 **HuggingFace** - Transformers pré-entraînés
7. ⚡ **Transformers** - Architecture, GPT, Vision Transformers
8. 🎯 **Détection** - YOLO, détection d'objets
9. 🔍 **Apprentissage Contrastif** - Techniques avancées
10. 🎓 **Transfer Learning** - Réutilisation de modèles
11. 🎨 **Modèles Génératifs** - GANs, VAEs, Diffusion
12. 🎁 **Bonus** - Sujets spécialisés (11 chapitres)

## 🔄 Changement de langue

Le système de changement de langue fonctionne automatiquement :
- Cliquez sur les boutons 🇫🇷/🇺🇸 dans le footer
- Préserve la page actuelle lors du changement
- Fonctionne en local et en déploiement

## 🛠️ Développement

### Ajouter du nouveau contenu

1. **Contenu français** : Ajouter dans le répertoire `fr/`
2. **Contenu anglais** : Ajouter dans le répertoire `en/`
3. **Mettre à jour la table des matières** : Modifier les fichiers `_toc.yml`
4. **Reconstruire** : Exécuter `python build_multilingual.py`

### Aide à la traduction

```bash
python translate_content.py  # Crée des templates anglais
```

### Déploiement

```bash
./deploy.sh  # Prépare pour GitHub Pages
```

## 🧪 Tests

- **Test local** : `python test_local.py`
- **Test de changement** : `open test_switching.html`
- **Documentation** : Voir `LANGUAGE_SWITCHING.md`

## 📄 Licence

Ce cours est open source et disponible sous licence MIT.

## 👨‍💻 Auteur

**Simon Thomine**
- GitHub : [@SimonThomine](https://github.com/SimonThomine)

---

*Apprenez le Deep Learning à partir de zéro avec des exemples pratiques et une théorie complète !*