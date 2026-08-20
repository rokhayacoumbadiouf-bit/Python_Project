# 🐍 Application Python – datasetManager

## 📌 Contexte

Application console développée pour aider des Data Scientists à gérer un catalogue de jeux de données (CSV/JSON) : enregistrement des caractéristiques, recherche, statistiques, sauvegarde/rechargement automatique et gestion des erreurs.

Atelier réalisé dans le cadre du cours **Python pour ML et IA** – P1 IA, Orange Digital Center (ODC) .

## 🎯 Objectifs

- Gérer un catalogue de jeux de données
- Enregistrer leurs caractéristiques (métadonnées)
- Effectuer des recherches
- Afficher des statistiques
- Sauvegarder/charger automatiquement les données
- Gérer les erreurs d'utilisation

## 🗂️ Structure du projet

```
datasetManager/
├── main.py
├── datasets/
│   ├── __init__.py
│   ├── gestion.py          # ajout, recherche, tri, modification, suppression
│   └── statistiques.py     # calcul des statistiques du catalogue
├── interface/
│   ├── __init__.py
│   ├── menu.py             # menu interactif
│   └── affichage.py        # affichage formaté
├── stockage/
│   ├── __init__.py
│   ├── csv_manager.py      # sauvegarde/chargement CSV
│   └── json_manager.py     # sauvegarde/chargement JSON
└── data/
    ├── datasets.csv
    ├── datasets.json
    └── rapport_statistiques.txt   # bonus
```

## 🧩 Fonctionnalités par partie

| Partie | Sujet |
|---|---|
| 1 | Types de base, variables, entrées/sorties (saisie des métadonnées) |
| 2 | Structures de contrôle (menu interactif) |
| 3 | Dictionnaires (métadonnées d'un dataset) |
| 4 | Tuples (domaines autorisés + validation) |
| 5 | Listes (ajouter, trier, rechercher, modifier, supprimer) |
| 6 | Compréhensions & statistiques du catalogue |
| 7 | Fichiers (sauvegarde/rechargement CSV) |
| 8 | Exceptions (saisie invalide, fichier manquant, dataset introuvable, fichier vide) |
| 9 | Fonctions (refactorisation complète) |
| 10 | Modules (`main.py`, `menu.py`, `gestion.py`, `statistiques.py`) |
| 11 | Packages (architecture finale ci-dessus) |
| 12 | Bonus – génération d'un rapport automatique |

## 📋 Métadonnées d'un dataset

```json
{
  "nom": "Titanic",
  "domaine": "Transport",
  "lignes": 891,
  "colonnes": 12,
  "taille": 48,
  "format": "CSV",
  "public": true
}
```

Domaines autorisés : `Santé`, `Finance`, `Agriculture`, `Transport`, `Education`.

## ▶️ Utilisation

```bash
cd datasetManager
python main.py
```

Menu proposé :
```
1. Ajouter un dataset
2. Afficher les datasets
3. Rechercher un dataset
4. Modifier un dataset
5. Supprimer un dataset
6. Trier les datasets
7. Statistiques
8. Sauvegarder
9. Recharger
10. Quitter
```

## 📊 Statistiques calculées

- Nombre de datasets
- Nombre total / moyen de lignes et colonnes
- Répartition public / privé
- Répartition par format (CSV / JSON)
- Répartition par domaine

## 🎁 Bonus

Génération d'un rapport d'analyse textuel complet (`data/rapport_statistiques.txt`) : statistiques globales, répartition par format, inventaire détaillé des datasets.

## 📦 Livrables

1. Dossier `datasetManager/` (code source complet)
2. Document PDF illustrant la réalisation, avec la réponse sous chaque question

## 👤 Auteure

**Rokhaya Coumba Diouf** – parcours IA (P1 IA) Orange Digital Center (ODC)
