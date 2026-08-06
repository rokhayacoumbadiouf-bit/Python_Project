import csv
# =====================================
# AJOUTER
# =====================================
domaines_valides = ["finance", "santé", "éducation", "transport", "environnement"]
def ajouter_dataset(liste):
   print("\n--- Ajout d'un dataset ---")
   nom = input("Nom : ")
   domaine = input("Domaine (finance, santé, éducation, transport, environnement) : ").lower()
   while domaine not in domaines_valides:
        print(f"/!\\ Domaine invalide. Veuillez choisir parmi : {domaines_valides}")
        domaine = input("Domaine : ").lower()
   ligne = saisir_entier("Nombre de lignes : ")
   colonne = saisir_entier("Nombre de colonnes : ")
   taille = saisir_reel("Taille (Mo) : ")
   format = input("Format (csv/json) : ")   
   public = input("Public (true/false) : ").lower() == "true"
   dataset = {
     "nom": nom,
     "domaine": domaine,
     "lignes": ligne,
     "colonnes": colonne,
     "taille": taille,
     "format": format,
     "public": public
   }
   liste.append(dataset)
   print("Dataset ajouté avec succès !")
  
# ----------------------------
# Affichage
# ---------------------------

def afficher_datasets(liste):
    # Recharge les données depuis le fichier CSV
    liste = recharger()
    # Vérifie si la liste est vide
    if len(liste) == 0:
        print("Aucun dataset enregistré.")
        return
    print("\n========== LISTE DES DATASETS ==========")
    # Affichage détaillé de chaque dataset
    for i, dataset in enumerate(liste, start=1):
        print(f"\nDataset {i}")
        print("-" * 35)
        print(f"Nom       : {dataset['nom']}")
        print(f"Domaine   : {dataset['domaine']}")
        print(f"Lignes    : {dataset['lignes']}")
        print(f"Colonnes  : {dataset['colonnes']}")
        print(f"Taille    : {dataset['taille']} Mo")
        print(f"Format    : {dataset['format']}")
        print(f"Public    : {dataset['public']}")
    print("\n========================================")
   
# =====================================
# RECHERCHER
# =====================================

def rechercher_dataset(liste):
 recherche = input("Nom du dataset : ")
 trouve = False    
 for dataset in liste:
    if dataset["nom"].lower() == recherche.lower():
     print("\nDataset trouvé :")
     print(dataset)
     trouve = True
     break
     if not trouve:
       print("Dataset introuvable.")
    
# =====================================
# MODIFIER
# =====================================

def modifier_dataset(liste):
  nom = input("Nom du dataset à modifier : ")
  for dataset in liste:
   if dataset["nom"] == nom:
    dataset["taille"] = float( input("Nouvelle taille : "))
    print("Modification réussie.")
  else:
     print("Dataset introuvable.")


# =====================================
# SUPPRIMER
# =====================================

def supprimer_dataset(liste):
   nom = input("Nom du dataset à supprimer : ")
   for dataset in liste:
    if dataset["nom"] == nom:
     liste.remove(dataset)
     print("Dataset supprimé.")
    else:
     print("Dataset introuvable.")

# =====================================
# TRIER
# =====================================

def trier_dataset(liste):
 liste.sort(key=lambda x:x["nom"] )
 print("Datasets triés par nom.")   

# ----------------------------
# Sauvegarde
# ----------------------------

def sauvegarder_datasets(liste):
    try:
        with open("datasets.csv", "w", newline="", encoding="utf-8") as fichier:
            writer = csv.writer(fichier)
            writer.writerow([
                "nom",
                "domaine",
                "lignes",
                "colonnes",
                "taille",
                "format",
                "public"
            ])
            for dataset in liste:
                writer.writerow([
                    dataset["nom"],
                    dataset["domaine"],
                    dataset["lignes"],
                    dataset["colonnes"],
                    dataset["taille"],
                    dataset["format"],
                    dataset["public"]
                ])
        print("Sauvegarde effectuée avec succès.")
    except Exception as e:
        print("/!\\Erreur lors de la sauvegarde :", e)


# =====================================
# RECHARGER
# =====================================

def recharger():
 liste = []
 with open("datasets.csv", "r", encoding="utf-8") as fichier: lecteur = csv.DictReader(fichier)
 for ligne in lecteur:
   dataset = {  "nom": ligne["nom"],
                "domaine": ligne["domaine"],
                "lignes": int(ligne["lignes"]),
                "colonnes": int(ligne["colonnes"]),
                "taille": float(ligne["taille"]),
                "format": ligne["format"],
                "public": ligne["public"] == "True"
            }
 liste.append(dataset)
 return liste

   
  


# ==========================================================
# GESTION DES EXCEPTIONS
# ==========================================================


# ----------------------------------------------------------
# SAISIE SÉCURISÉE D'UN ENTIER
# ----------------------------------------------------------

def saisir_entier(message):
    """
    Demande un entier à l'utilisateur.
    La saisie est répétée tant qu'elle est invalide.
    """

    while True:

        try:

            return int(input(message))

        except ValueError:

            print("/!\\ Erreur : veuillez saisir un nombre entier.")


# ----------------------------------------------------------
# SAISIE SÉCURISÉE D'UN NOMBRE RÉEL
# ----------------------------------------------------------

def saisir_reel(message):
    """
    Demande un nombre décimal.
    """

    while True:

        try:

            return float(input(message))

        except ValueError:

            print("/!\\ Erreur : veuillez saisir un nombre valide.")


# ----------------------------------------------------------
# RECHERCHER UN DATASET
# ----------------------------------------------------------

def rechercher_dataset(liste):
    """
    Recherche un dataset par son nom.
    """

    nom = input("Nom du dataset : ")

    for dataset in liste:

        if dataset["nom"].lower() == nom.lower():

            print("\n===== DATASET TROUVÉ =====")

            for cle, valeur in dataset.items():
                print(f"{cle.capitalize()} : {valeur}")

            return

    print("/!\\ Aucun dataset ne porte ce nom.")


# ----------------------------------------------------------
# CHARGER LES DATASETS DEPUIS LE CSV
# ----------------------------------------------------------

def recharger():
    liste = []
    try:
        with open(
            "datasets.csv",
            "r",
            encoding="utf-8"
        ) as fichier:
            lecteur = csv.DictReader(fichier)
            for ligne in lecteur:
                dataset = {
                    "nom": ligne["nom"],
                    "domaine": ligne["domaine"],
                    "lignes": int(ligne["lignes"]),
                    "colonnes": int(ligne["colonnes"]),
                    "taille": float(ligne["taille"]),
                    "format": ligne["format"],
                    "public": ligne["public"] == "True"
                }
                liste.append(dataset)

        # Vérification d'un fichier vide
        if len(liste) == 0:
            print("/!\\ Le fichier datasets.csv est vide.")
        else:
            print("Chargement terminé.")
    except FileNotFoundError:
        print("/!\\ Le fichier datasets.csv est introuvable.")
    except Exception as erreur:
        print("/!\\ Une erreur est survenue :", erreur)
    return liste


# ----------------------------------------------------------
# SAUVEGARDER LES DATASETS
# ----------------------------------------------------------

def sauvegarder(liste):
    try:
        with open(
            "datasets.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as fichier:

            writer = csv.writer(fichier)

            writer.writerow([
                "nom",
                "domaine",
                "lignes",
                "colonnes",
                "taille",
                "format",
                "public"
            ])

            for dataset in liste:

                writer.writerow([

                    dataset["nom"],
                    dataset["domaine"],
                    dataset["lignes"],
                    dataset["colonnes"],
                    dataset["taille"],
                    dataset["format"],
                    dataset["public"]

                ])

        print("✔ Sauvegarde effectuée avec succès.")

    except Exception as erreur:

        print("/!\\ Impossible de sauvegarder le fichier.")

        print(erreur)

#===================
#  BONUS
#===================

#====================
#   Sauvegarde JSON
#====================

def sauvegarder_json(liste):
    import json
    try:
        with open("datasets.json", "w", encoding="utf-8") as fichier:
            json.dump(liste, fichier, ensure_ascii=False, indent=4)
        print(" Sauvegarde JSON effectuée avec succès.")
    except Exception as erreur:
        print("/!\\ Impossible de sauvegarder le fichier JSON.")
        print(erreur)

#====================
#   Charger JSON
#====================

def charger_json():
    import json
    try:
        with open("datasets.json", "r", encoding="utf-8") as fichier:
            liste = json.load(fichier)
        print(" Chargement JSON terminé.")
        return liste
    except FileNotFoundError:
        print("/!\\ Le fichier datasets.json est introuvable.")
        return []
    except Exception as erreur:
        print("/!\\ Une erreur est survenue lors du chargement JSON :", erreur)
        return []