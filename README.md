# Projet de détection de fausses nouvelles avec MLflow et modèles de Machine Learning

## 🌎 Contexte général

La propagation rapide des fausses nouvelles ("fake news") sur les réseaux sociaux et les plateformes en ligne constitue une menace majeure pour la société moderne. Ces informations trompeuses peuvent manipuler l'opinion publique, influencer des élections ou encore alimenter des tensions sociales. Dans ce contexte, il devient crucial de développer des systèmes intelligents capables de détecter automatiquement ces fausses informations.

Ce projet a pour objectif de concevoir un système de détection de fausses nouvelles à l'aide d'algorithmes de machine learning. Il intègre également MLflow pour le suivi, la comparaison et la gestion des expériences d'entraînement de modèles.

---

## Architecture du projet
[NewsAPI] → [Script Python avec cron / scheduler] → [Base PostgreSQL]
                                           ↓
                                    (stockage structuré)
                                           ↓
                              [Requêtes d’analyse / ML]
                                            ↓
                                      [MLflow Tracking]
                                            ↓
                                      [Modèles ML]
                                            ↓
                                  [API Web (Flask/FastAPI)]

## 🔧 Mise en place technique

### 1. Prétraitement & Vectorisation

* Nettoyage des textes (lemmatisation, suppression des stopwords, etc.)
* Vectorisation avec **TF-IDF**

- Naive Bayes
- Régression Logistique
- SVM (kernel RBF par défaut)
- Linear SVM (LinearSVC)

### 4. Suivi des expériences avec MLflow

![Experience with Mlflow ](https://github.com/dona-eric/System-detection-of-the-Fake-and-True-News/blob/master/News%20_dataset/images/mlflow.png)

* Installation de MLflow : `pip install mlflow`
* Lancement du serveur MLflow : `mlflow ui`
* Enregistrement des expériences MLflow dans le répertoire `mlruns/`
* Utilisation de `mlflow.start_run()` pour chaque exécution d'entraînement
* Enregistrement des modèles et des métriques dans `mlartifacts/`
### 2. Entraînement des modèles
Pour chaque modèle entraîné :

* Enregistrement automatique des métriques (à l'aide de `mlflow.log_metric`)
* Enregistrement du modèle (`mlflow.sklearn.log_model`)
* Gestion de l'environnement Python (dépendances, YAML, etc.)

Chaque exécution est accessible via l'interface de suivi MLflow :
`http://127.0.0.1:5000/#/experiments/0`

[Execution date and performances of each models training](https://github.com/dona-eric/System-detection-of-the-Fake-and-True-News/blob/master/News%20_dataset/images/experiment_mlflow.webm)
---

## 🤖 Modèles entraînés et évalués

### 1. **Naive Bayes**

* **Pourquoi ce choix** :
  Simple, rapide, souvent très performant pour le texte grâce à l’hypothèse d’indépendance conditionnelle.
* **Résultats** :

  `Accuracy : 0.937 F1 Score : 0.937 Matrice de confusion : [[4404 329] [ 235 4012]]`
* **Limites** :

  * Hypothèse d’indépendance trop forte
  * Moins robuste sur des textes complexes ou ambigus

---

### 2. **Régression Logistique**

* **Pourquoi ce choix** :
  Modèle linéaire robuste, efficace pour les données linéairement séparables, très populaire en NLP.
* **Résultats** :`Accuracy : 0.987 F1 Score : 0.987 Matrice de confusion : [[4675 58] [ 58 4189]]`
* **Observations** :

  * Très bon équilibre entre précision et rappel.
  * Moins sensible au bruit que Naive Bayes.

---

### 3. **SVM (kernel par défaut)**

* **Pourquoi ce choix** :
  Puissant pour séparer les classes dans des espaces de grande dimension. Kernel RBF permet de capter des relations non linéaires.
* **Résultats** :
* `Accuracy : 0.993 F1 Score : 0.993 Matrice de confusion : [[4702 31] [ 27 4220]]`
* **Limites** :

  * Temps d'entraînement plus long
  * Moins adapté aux très grands jeux de données

---

### 4. **LinearSVC**

* **Pourquoi ce choix** :
  Variante optimisée de SVM pour les données linéairement séparables. Très rapide, scalable, efficace sur les grands jeux de textes vectorisés par TF-IDF.
* **Résultats** :

  `Accuracy : 0.995 F1 Score : 0.995 Matrice de confusion : [[4711 22] [ 19 4228]]`
* **Avantages** :

  * Précision exceptionnelle
  * Temps de calcul faible
  * Idéal pour les problèmes de classification binaire avec texte vectorisé

---

## 📊 Choix du meilleur modèle : **LinearSVC**

Après comparaison des métriques, **LinearSVC** a été retenu comme modèle final pour son équilibre optimal entre performance (F1 = 99.5%) et rapidité. Il gère très bien les vecteurs sparsely représentés issus du TF-IDF.

---

## 🚀 Suite du projet

* Le modèle final est enregistré dans `mlartifacts/` et peut être rechargé via MLflow pour une intégration dans une API web (Flask/FastAPI).

* Une interface sera mise en place pour :

  * Charger des articles
  * Prédire s'ils sont vrais ou faux
  * Afficher les statistiques liées aux prédictions

---

## 📄 Fichiers clés

* `fake_news.py` : script principal d'analyse et d'entraînement
* `mlruns/` : historiques des expériences MLflow
* `mlartifacts/` : stockage des modèles enregistrés

---

## 🚫 Limitations

* Dataset binaire (vrai/faux), mais certains articles peuvent être partiellement trompeurs
* Pas de traitement multilingue pour l'instant

---

## 🚀 Perspectives

* Intégration d'une API REST pour détection en ligne
* Ajout d'un système d'explication des prédictions (ex : SHAP, LIME)
* Prétraitement plus fin (NER, sentiments, détection de ton manipulatif)

---

## 📅 Auteur

* Projet réalisé par \[KOULODJI Dona Eric] dans le cadre d'une exploration pratique de la détection de fake news avec machine learning.
