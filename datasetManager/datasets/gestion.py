
DOMAINES_VALIDES = ["finance", "santé", "éducation", "transport", "environnement"]


# =====================================================================
#                          SAISIES SÉCURISÉES 
# =====================================================================

def saisir_entier(message):
    """Redemande tant que l'utilisateur ne saisit pas un entier valide."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("/!\\ Erreur : veuillez saisir un nombre entier.")


def saisir_reel(message):
    """Redemande tant que l'utilisateur ne saisit pas un nombre valide."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("/!\\ Erreur : veuillez saisir un nombre valide.")


# =====================================================================
#                             AJOUTER
# =====================================================================

def ajouter_dataset(liste):
    """Demande les métadonnées d'un dataset et l'ajoute à la liste."""
    print("\n--- Ajout d'un dataset ---")

    nom = input("Nom : ")

    domaine = input(f"Domaine ({', '.join(DOMAINES_VALIDES)}) : ").lower()
    while domaine not in DOMAINES_VALIDES:
        print(f"/!\\ Domaine invalide. Choisissez parmi : {DOMAINES_VALIDES}")
        domaine = input("Domaine : ").lower()

    lignes = saisir_entier("Nombre de lignes : ")
    colonnes = saisir_entier("Nombre de colonnes : ")
    taille = saisir_reel("Taille (Mo) : ")
    format_dataset = input("Format (csv/json) : ").lower()
    public = input("Public (true/false) : ").lower() == "true"

    dataset = {
        "nom": nom,
        "domaine": domaine,
        "lignes": lignes,
        "colonnes": colonnes,
        "taille": taille,
        "format": format_dataset,
        "public": public
    }

    liste.append(dataset)
    print("Dataset ajouté avec succès !")


# =====================================================================
#                             RECHERCHER
# =====================================================================

def rechercher_dataset(liste):
    """Cherche un dataset par son nom (insensible à la casse)."""
    nom = input("Nom du dataset : ")

    for dataset in liste:
        if dataset["nom"].lower() == nom.lower():
            print("\n===== DATASET TROUVÉ =====")
            for cle, valeur in dataset.items():
                print(f"{cle.capitalize()} : {valeur}")
            return dataset

    print("/!\\ Aucun dataset ne porte ce nom.")
    return None


# =====================================================================
#                              MODIFIER
# =====================================================================

def modifier_dataset(liste):
    """Modifie la taille d'un dataset identifié par son nom."""
    nom = input("Nom du dataset à modifier : ")

    for dataset in liste:
        if dataset["nom"] == nom:
            dataset["taille"] = saisir_reel("Nouvelle taille (Mo) : ")
            print("Modification réussie.")
            break
    else:

        print("Dataset introuvable.")


# =====================================================================
#                             SUPPRIMER
# =====================================================================

def supprimer_dataset(liste):
    """Supprime un dataset identifié par son nom."""
    nom = input("Nom du dataset à supprimer : ")

    for dataset in liste:
        if dataset["nom"] == nom:
            liste.remove(dataset)
            print("Dataset supprimé.")
            break
    else:
        print("Dataset introuvable.")


# =====================================================================
#                                TRIER
# =====================================================================

def trier_dataset(liste):
    """Trie la liste des datasets par nom, ordre alphabétique."""
    liste.sort(key=lambda d: d["nom"].lower())
    print("Datasets triés par nom.")
