import csv
import os

CHEMIN_CSV = os.path.join("data", "datasets.csv")


def sauvegarder(liste):
    
    try:
       
        os.makedirs(os.path.dirname(CHEMIN_CSV), exist_ok=True)

        with open(CHEMIN_CSV, "w", newline="", encoding="utf-8") as fichier:
            writer = csv.writer(fichier)
            writer.writerow(["nom", "domaine", "lignes", "colonnes", "taille", "format", "public"])
            for dataset in liste:
                writer.writerow([
                    dataset["nom"], dataset["domaine"], dataset["lignes"],
                    dataset["colonnes"], dataset["taille"], dataset["format"], dataset["public"]
                ])
        print(" Sauvegarde CSV effectuée avec succès.")

    except Exception as erreur:
        print("/!\\ Impossible de sauvegarder le fichier CSV :", erreur)


def recharger():
    """Recharge la liste des datasets depuis data/datasets.csv."""
    liste = []
    try:
        with open(CHEMIN_CSV, "r", encoding="utf-8") as fichier:
            lecteur = csv.DictReader(fichier)
            # La boucle est bien À L'INTÉRIEUR du bloc `with` cette fois,
            # sinon le fichier est fermé avant qu'on ait fini de le lire.
            for ligne in lecteur:
                try:
                    dataset = {
                        "nom": ligne["nom"],
                        "domaine": ligne["domaine"],
                        "lignes": int(ligne["lignes"]),
                        "colonnes": int(ligne["colonnes"]),
                        "taille": float(ligne["taille"]),
                        "format": ligne["format"],
                        "public": ligne["public"] == "True"
                    }
                    liste.append(dataset)  # append DANS la boucle, pas après
                except (ValueError, KeyError) as e:
                    print("/!\\ Ligne CSV ignorée (données corrompues) :", e)

        if not liste:
            print("/!\\ Le fichier datasets.csv est vide.")
        else:
            print(f" {len(liste)} dataset(s) CSV rechargé(s).")

    except FileNotFoundError:
        print("/!\\ Le fichier datasets.csv est introuvable.")
    except Exception as erreur:
        print("/!\\ Une erreur est survenue lors du chargement CSV :", erreur)

    return liste
