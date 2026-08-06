import json
import os

CHEMIN_JSON = os.path.join("data", "datasets.json")


def sauvegarder_json(liste):
    """Écrit la liste des datasets dans data/datasets.json."""
    try:
        os.makedirs(os.path.dirname(CHEMIN_JSON), exist_ok=True)
        with open(CHEMIN_JSON, "w", encoding="utf-8") as fichier:
            json.dump(liste, fichier, ensure_ascii=False, indent=4)
        print("✔ Sauvegarde JSON effectuée avec succès.")
    except Exception as erreur:
        print("/!\\ Impossible de sauvegarder le fichier JSON :", erreur)


def charger_json():
    """Recharge la liste des datasets depuis data/datasets.json."""
    try:
        with open(CHEMIN_JSON, "r", encoding="utf-8") as fichier:
            liste = json.load(fichier)
        if not liste:
            print("/!\\ Le fichier datasets.json est vide.")
        else:
            print(f" {len(liste)} dataset(s) JSON rechargé(s).")
        return liste
    except FileNotFoundError:
        print("/!\\ Le fichier datasets.json est introuvable.")
        return []
    except json.JSONDecodeError as erreur:
        print("/!\\ Le fichier datasets.json est corrompu :", erreur)
        return []
    except Exception as erreur:
        print("/!\\ Une erreur est survenue lors du chargement JSON :", erreur)
        return []
