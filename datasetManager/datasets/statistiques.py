"""
datasets/statistiques.py
Calcul et affichage des statistiques globales sur le catalogue.
"""


def statistiques(liste):
    """Affiche : nombre total, lignes, moyenne colonnes, public/privé,
    répartition par format et par domaine (Partie 6 — compréhensions)."""
    print("\n===== STATISTIQUES =====")

    if not liste:
        print("Aucun dataset.")
        return

    nombre_dataset = len(liste)

    total_lignes = sum(d["lignes"] for d in liste)
    total_colonnes = sum(d["colonnes"] for d in liste)
    moyenne_colonnes = total_colonnes / nombre_dataset

    nb_publics = sum(1 for d in liste if d["public"])
    nb_prives = nombre_dataset - nb_publics

    nb_csv = sum(1 for d in liste if d["format"].lower() == "csv")
    nb_json = sum(1 for d in liste if d["format"].lower() == "json")

    domaines = {}
    for dataset in liste:
        domaine = dataset["domaine"]
        domaines[domaine] = domaines.get(domaine, 0) + 1

    print("Nombre de datasets :", nombre_dataset)
    print("Total lignes        :", total_lignes)
    print("Moyenne colonnes    :", round(moyenne_colonnes, 2))
    print("Publics             :", nb_publics)
    print("Privés              :", nb_prives)
    print("CSV                 :", nb_csv)
    print("JSON                :", nb_json)
    print("\nRépartition par domaine :")
    for domaine, nombre in domaines.items():
        print(f"  {domaine} : {nombre}")
