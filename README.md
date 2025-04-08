# ⚽ Prédiction de Résultats de Matchs de Football & Recommandation de Paris Sportifs

## 🎬 Vidéo de présentation du projet

https://www.loom.com/share/7d0f04edb2434e4b8c6ea6de5346ee4f?sid=55c7a88a-51eb-4c38-9417-5c86ff8af451

## 📁 Structure du projet
Le dossier contient :  
- les fichiers générés via google collab pour la phase de résultats
- le google collab
- App.js : pour l'interface Streamlit
- Requirements.txt : technologies nécessaires
- un sous-dossier CSV : contenant les CSV du site https://www.football-data.co.uk/downloadm.php
- Ce READMe, pour vous servir 

## 📌 Objectif

Ce projet a pour but de prédire les résultats des matchs de football (Victoire à domicile, Nul ou Victoire à l’extérieur) à partir de données historiques enrichies, tout en fournissant des recommandations de paris en identifiant les "values" potentielles (écarts entre probabilité prédite et cote attendue).

---

## 🚀 Fonctionnalités

- 🔧 Feature engineering avancé : résultats saison précédente, moyennes glissantes, dynamiques d’équipes...
- 🧠 Entraînement de plusieurs modèles : Random Forest, KNN, Logistic Regression, XGBoost, Voting Classifier
- 📊 Évaluation des performances avec `accuracy`, `f1-score`, `confusion matrix`
- 🔍 Interprétation avec SHAP : importance des variables pour chaque prédiction
- 💸 Calcul de **value betting** : pari recommandé si la cote est supérieure à la cote minimale attendue
- 🖥️ Interface interactive avec Streamlit pour visualiser et tester les prédictions

---

## 🧰 Stack Technique

- **Python** : pandas, numpy, scikit-learn, xgboost, shap
- **Streamlit** : application web interactive
- **Google Colab** : pour l'exploration et le prototypage initial
- **VS Code** : développement local
- **GitHub** : versioning et déploiement

---

## 🧠 Modélisation et Résultats

| Modèle               | Accuracy | F1-score |
|----------------------|----------|----------|
| Random Forest        | 0.90     | 0.90     |
| KNN                  | 0.57     | 0.57     |
| Logistic Regression  | 1.00     | 1.00     |
| XGBoost              | 0.99     | 0.99     |
| Voting Classifier    | **1.00** | **1.00** |

**Choix final** : `XGBoost` pour son excellent compromis entre performance et interprétabilité (compatible SHAP).

---

## 🔍 Interprétation avec SHAP

Grâce à SHAP, nous avons pu identifier les variables les plus influentes sur le modèle :

- `B365_Correct` : Prédiction correcte selon les cotes B365
- `SecondHalf_Home_Goals` et `SecondHalf_Away_Goals`
- `B365_Prob_H`, `B365_Prob_A` : Probabilités implicites des bookmakers
- `HalfTime_Home_Goals`, `HalfTime_Away_Goals`

Les graphiques SHAP permettent de visualiser l’influence de chaque variable sur une prédiction spécifique.

---

## 💡 Système de Value Betting

Un **pari est recommandé** uniquement si la probabilité prédite par le modèle justifie une cote supérieure à celle attendue :
Si la **cote réelle** proposée par le bookmaker est supérieure à ce seuil, on considère qu’il y a une **value** et le pari est recommandé.

---

## 🌐 Interface Web (Streamlit)

### ▶️ Lancer l'application :

```bash
streamlit run streamlit_app.py



