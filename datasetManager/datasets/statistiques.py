"""
datasets/statistiques.py
Calcul et affichage des statistiques globales sur le catalogue.
"""
import os
from datetime import datetime


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


# =====================================================================
#                               Bonus
# =====================================================================


def generer_rapport_txt(liste_datasets):
    """Génère un rapport d'analyse textuel complet des datasets."""
    if not liste_datasets:
        print("/!\\ Aucun dataset en mémoire pour générer un rapport.")
        return

    # Calculs des statistiques
    total_datasets = len(liste_datasets)
    total_lignes = sum(d.get('lignes', 0) for d in liste_datasets)
    total_taille = sum(d.get('taille', 0) for d in liste_datasets)
    
    # Compte des formats
    nb_csv = sum(1 for d in liste_datasets if d.get('format', '').lower() == 'csv')
    nb_json = sum(1 for d in liste_datasets if d.get('format', '').lower() == 'json')

    # Création du dossier data s'il n'existe pas
    os.makedirs("data", exist_ok=True)
    chemin_rapport = "data/rapport_statistiques.txt"

    try:
        with open(chemin_rapport, "w", encoding="utf-8") as fichier:
            fichier.write("==================================================\n")
            fichier.write("         RAPPORT AUTOMATIQUE DES DATASETS         \n")
            fichier.write(f"  Généré le : {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}\n")
            fichier.write("==================================================\n\n")
            
            fichier.write("--- STATISTIQUES GLOBALES ---\n")
            fichier.write(f"Nombre total de datasets : {total_datasets}\n")
            fichier.write(f"Nombre cumulé de lignes  : {total_lignes:,}\n".replace(',', ' '))
            fichier.write(f"Volume total stocké      : {total_taille:.2f} Mo\n\n")
            
            fichier.write("--- RÉPARTITION PAR FORMAT ---\n")
            fichier.write(f"Fichiers CSV  : {nb_csv}\n")
            fichier.write(f"Fichiers JSON : {nb_json}\n\n")
            
            fichier.write("--- INVENTAIRE DES JEUX DE DONNÉES ---\n")
            fichier.write(f"{'Nom':<15} | {'Domaine':<15} | {'Format':<8} | {'Taille':<10}\n")
            fichier.write("-" * 56 + "\n")
            for d in liste_datasets:
                fichier.write(f"{d.get('nom', 'Inconnu'):<15} | {d.get('domaine', 'N/A'):<15} | {d.get('format', 'N/A').upper():<8} | {d.get('taille', 0):<6} Mo\n")
                
            fichier.write("\n==================================================\n")
            fichier.write("Fin du rapport.\n")
            
        print(f" Fin du rapport générée avec succès dans : {chemin_rapport}")
    
    except Exception as e:
        print(f"/!\\ Erreur lors de la génération du rapport : {e}")
