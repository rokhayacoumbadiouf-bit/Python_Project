from datasets.gestion import ajouter_dataset, afficher_datasets, charger_json, rechercher_dataset, modifier_dataset, sauvegarder_json, supprimer_dataset, trier_dataset, sauvegarder, recharger 
from data.statistiques import statistiques 
from interface.menu import afficher_menu

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
        
        for dataset in liste_datasets:
            if dataset['format'] == 'csv':
             sauvegarder(liste_datasets)
            if dataset['format'] == 'json':
             sauvegarder_json(liste_datasets)

    elif choix == "8":

        for dataset in liste_datasets:
            if dataset['format'] == 'csv':
                 liste_datasets = recharger()
            if dataset['format'] == 'json':
                 liste_datasets = charger_json()

    elif choix == "9":

        statistiques(liste_datasets)

    elif choix == "10":

        print("Fin du programme.")

        break

    else:

        print("Choix invalide.")

