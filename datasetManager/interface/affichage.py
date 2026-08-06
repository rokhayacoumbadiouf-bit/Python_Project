

def afficher_datasets(liste):
    """Affiche tous les datasets actuellement en mémoire."""
    if not liste:
        print("Aucun dataset enregistré.")
        return

    print("\n========== LISTE DES DATASETS ==========")
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
    print("\n==========================================")
