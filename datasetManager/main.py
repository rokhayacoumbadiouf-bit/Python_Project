

from datasets.gestion import (
    ajouter_dataset,
    rechercher_dataset,
    modifier_dataset,
    supprimer_dataset,
    trier_dataset,
)
from datasets.statistiques import generer_rapport_txt, statistiques
from interface.menu import afficher_menu
from interface.affichage import afficher_datasets
from stockage.csv_manager import recharger, sauvegarder
from stockage.json_manager import charger_json, sauvegarder_json


def sauvegarder_tout(liste_datasets):
    """Répartit les datasets par format et les sauvegarde chacun
    dans le bon fichier (CSV / JSON)."""
    datasets_csv = [d for d in liste_datasets if d["format"].lower() == "csv"]
    datasets_json = [d for d in liste_datasets if d["format"].lower() == "json"]

    if not datasets_csv and not datasets_json:
        print("Aucun dataset à sauvegarder.")
        return

    if datasets_csv:
        sauvegarder(datasets_csv)
    if datasets_json:
        sauvegarder_json(datasets_json)


def recharger_tout():
    """Recharge les datasets CSV et JSON et les fusionne en une seule liste."""
    liste_csv = recharger()
    liste_json = charger_json()
    liste = liste_csv + liste_json
    print(f"Total rechargé : {len(liste)} dataset(s).")
    return liste


def main():
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
            sauvegarder_tout(liste_datasets)
        elif choix == "8":
            liste_datasets = recharger_tout()
        elif choix == "9":
            statistiques(liste_datasets)
            generer_rapport_txt(liste_datasets)
        elif choix == "10":
            print("Fin du programme.")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
