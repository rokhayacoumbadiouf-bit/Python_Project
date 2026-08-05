import csv

# Demande des métadonnées du dataset


print("Veuillez saisir les métadonnées du dataset :")
nom_dataset = input("Nom du dataset : ")

domaines_autorises = (
    "santé", 
    "finance",
    "agriculture",
    "transport", 
    "education"
    )

domaine = input("Domaine( santé, finance, agriculture, transport, education) : ").lower()
while domaine not in domaines_autorises:
    print("Domaine invalide. Veuillez choisir parmi les domaines autorisés :", domaines_autorises)
    domaine = input("Domaine : ").lower()

nombre_lignes = int(input("Nombre de lignes : "))
nombre_colonnes = int(input("Nombre de colonnes : "))
taille_mo = float(input("Taille en Mo : "))
format_dataset = input("Format (csv ou json) : ")
public = input("Public (true ou false) : ").lower() == "true"


print("\nRésumé du dataset :")
print(f"Nom : {nom_dataset}")
print(f"Domaine : {domaine}")
print(f"Nombre de lignes : {nombre_lignes}")
print(f"Nombre de colonnes : {nombre_colonnes}")
print(f"Taille : {taille_mo} Mo")
print(f"Format : {format_dataset}")
print(f"Public : {public}")



print("================================")
print("\nMenu interactif :")
while True:
    print("\n1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Quitter")
    
    choix = input("Veuillez choisir une option (1-4) : ")
    
    if choix == "1":
       print("Option 1 sélectionnée : Ajouter un dataset")
    elif choix == "2":
        print("Option 2 sélectionnée : Afficher les datasets")
    elif choix == "3":
        print("Option 3 sélectionnée : Rechercher")
    elif choix == "4":
        print("Option 4 sélectionnée : Quitter")
        break

print("================================")


Dataset = {
    "nom": nom_dataset, 
    "domaine": domaine,
    "lignes": nombre_lignes,
    "colonnes": nombre_colonnes,
    "taille": taille_mo,
    "format": format_dataset,
    "public": public
}   


liste_datasets = []


while True:

    print("\n========= MENU DATASETS =========")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher un dataset")
    print("4. Modifier un dataset")
    print("5. Supprimer un dataset")
    print("6. Trier les datasets")
    print("7. Statistiques")
    print("8. Quitter")

    choix = input("Votre choix : ")

    
    # -------------------------
    # AJOUTER UN DATASET
    # -------------------------

    if choix == "1":

        print("\n--- Ajout d'un dataset ---")

        dataset = {
            "nom": input("Nom : "),
            "domaine": input("Domaine : ").lower(),
            "lignes": int(input("Nombre de lignes : ")),
            "colonnes": int(input("Nombre de colonnes : ")),
            "taille": float(input("Taille (Mo) : ")),
            "format": input("Format (csv/json) : "),
            "public": input("Public (true/false) : ").lower() == "true"
        }


        liste_datasets.append(dataset)

        print("Dataset ajouté avec succès !")



    # -------------------------
    # AFFICHER LES DATASETS
    # -------------------------

    elif choix == "2":

        print("\n--- Liste des datasets ---")

        if len(liste_datasets) == 0:
            print("Aucun dataset disponible.")

        else:

            for i, dataset in enumerate(liste_datasets):

                print("\nDataset", i+1)

                print("Nom :", dataset["nom"])
                print("Domaine :", dataset["domaine"])
                print("Lignes :", dataset["lignes"])
                print("Colonnes :", dataset["colonnes"])
                print("Taille :", dataset["taille"], "Mo")
                print("Format :", dataset["format"])
                print("Public :", dataset["public"])




    # -------------------------
    # RECHERCHER
    # -------------------------

    elif choix == "3":

        recherche = input("Nom du dataset : ")

        trouve = False


        for dataset in liste_datasets:

            if dataset["nom"].lower() == recherche.lower():

                print("\nDataset trouvé :")

                print(dataset)

                trouve = True

                break


        if not trouve:
            print("Dataset introuvable.")




    # -------------------------
    # MODIFIER
    # -------------------------

    elif choix == "4":

        nom = input("Nom du dataset à modifier : ")

        for dataset in liste_datasets:

            if dataset["nom"] == nom:

                dataset["taille"] = float(
                    input("Nouvelle taille : ")
                )

                print("Modification réussie.")

                break

        else:

            print("Dataset introuvable.")




    # -------------------------
    # SUPPRIMER
    # -------------------------

    elif choix == "5":

        nom = input("Nom du dataset à supprimer : ")


        for dataset in liste_datasets:

            if dataset["nom"] == nom:

                liste_datasets.remove(dataset)

                print("Dataset supprimé.")

                break


        else:

            print("Dataset introuvable.")




    # -------------------------
    # TRIER
    # -------------------------

    elif choix == "6":
        liste_datasets.sort(
            key=lambda x:x["nom"]
        )

        print("Datasets triés par nom.")
    # -------------------------
    # STATISTIQUES
    # -------------------------

    elif choix == "7":
        print("\n===== STATISTIQUES =====")
        if len(liste_datasets)==0:
             print("Aucun dataset.")
        else:
            nombre_dataset = len(liste_datasets)
            total_lignes = 0
            total_colonnes = 0
            public = 0
            prive = 0
            csv = 0
            json = 0
            domaines = {}
            for dataset in liste_datasets:
                total_lignes += dataset["lignes"]
                total_colonnes += dataset["colonnes"]
                if dataset["public"]:
                    public += 1
                else:
                    prive += 1
                if dataset["format"].lower()=="csv":
                    csv += 1
                elif dataset["format"].lower()=="json":
                    json += 1
                domaine = dataset["domaine"]
                if domaine in domaines:
                    domaines[domaine]+=1
                else:
                    domaines[domaine]=1
            moyenne_colonnes = total_colonnes / nombre_dataset
            print("Nombre de datasets :", nombre_dataset)
            print("Total lignes :", total_lignes)
            print("Moyenne colonnes :", moyenne_colonnes)
            print("Publics :", public)
            print("Privés :", prive)
            print("CSV :", csv)
            print("JSON :", json)
            print("\nRépartition domaines :")
            for domaine,nombre in domaines.items():
                print(
                    domaine,
                    ":",
                    nombre
                )
    # -------------------------
    # QUITTER
    # -------------------------

    elif choix == "8":
        print("Fin du programme.")
        break

    else:
        print("Choix invalide.")

import csv

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
        for dataset in liste_datasets:
            writer.writerow([
                dataset["nom"],
                dataset["domaine"],
                dataset["lignes"],
                dataset["colonnes"],
                dataset["taille"],
                dataset["format"],
                dataset["public"]
            ])
print("Sauvegarde terminée.")


liste = []

with open("datasets.csv", "r", encoding="utf-8") as fichier:
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


#Fonctions

# ----------------------------
# Affichage
# ----------------------------
def afficher_datasets(liste):
 print("\n--- Liste des datasets ---")

 if len(liste_datasets) == 0:
    print("Aucun dataset disponible.")

 else:
     for i, dataset in enumerate(liste_datasets):
      print("\nDataset", i+1)
      print("Nom :", dataset["nom"])
      print("Domaine :", dataset["domaine"])
      print("Lignes :", dataset["lignes"])
      print("Colonnes :", dataset["colonnes"])
      print("Taille :", dataset["taille"], "Mo")
      print("Format :", dataset["format"])
      print("Public :", dataset["public"])


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
        print("Erreur lors de la sauvegarde :", e)



# ----------------------------
# Chargement
# ----------------------------
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

            print("❌ Erreur : veuillez saisir un nombre entier.")


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

            print("❌ Erreur : veuillez saisir un nombre valide.")


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

    print("❌ Aucun dataset ne porte ce nom.")


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

            print("⚠ Le fichier datasets.csv est vide.")

        else:

            print("✔ Chargement terminé.")

    except FileNotFoundError:

        print("❌ Le fichier datasets.csv est introuvable.")

    except Exception as erreur:

        print("❌ Une erreur est survenue :", erreur)

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

        print("❌ Impossible de sauvegarder le fichier.")

        print(erreur)

# =====================================
# AFFICHER LE MENU
# =====================================

def afficher_menu():

    print("\n========== MENU ==========")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher un dataset")
    print("4. Modifier un dataset")
    print("5. Supprimer un dataset")
    print("6. Trier les datasets")
    print("7. Sauvegarder")
    print("8. Recharger")
    print("9. Statistiques")
    print("10. Quitter")


# =====================================
# AJOUTER
# =====================================

def ajouter_dataset(liste):

    ...
    # ton code d'ajout


# =====================================
# AFFICHER
# =====================================

def afficher_datasets(liste):

    ...
    # ton code d'affichage


# =====================================
# RECHERCHER
# =====================================

def rechercher_dataset(liste):

    ...
    # ton code de recherche


# =====================================
# MODIFIER
# =====================================

def modifier_dataset(liste):

    ...
    # ton code de modification


# =====================================
# SUPPRIMER
# =====================================

def supprimer_dataset(liste):

    ...
    # ton code de suppression


# =====================================
# TRIER
# =====================================

def trier_dataset(liste):

    ...
    # ton code de tri


# =====================================
# SAUVEGARDER
# =====================================

def sauvegarder(liste):

    ...
    # ton code CSV


# =====================================
# RECHARGER
# =====================================

def recharger():

    ...
    # ton code CSV

    return liste


# =====================================
# STATISTIQUES
# =====================================

def statistiques(liste):

    ...
    # ton code statistiques

liste_datasets = []

while True:
    afficher_menu()
    choix = input("Votre choix : ")

    if choix == "1":

        ajouter_dataset(liste_datasets)

    elif choix == "2":

        afficher_datasets(liste_datasets)

    elif choix == "3":

        rechercher_dataset(liste_datasets)

    elif choix == "4":

        modifier_dataset(liste_datasets)

    elif choix == "5":

        supprimer_dataset(liste_datasets)

    elif choix == "6":

        trier_dataset(liste_datasets)

    elif choix == "7":

        sauvegarder(liste_datasets)

    elif choix == "8":

        liste_datasets = recharger()

    elif choix == "9":

        statistiques(liste_datasets)

    elif choix == "10":

        print("Fin du programme.")

        break

    else:

        print("Choix invalide.")

