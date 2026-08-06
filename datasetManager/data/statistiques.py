# -------------------------
 # STATISTIQUES
# -------------------------
def statistiques(liste):
  print("\n===== STATISTIQUES =====")
  if len(liste)==0:
      print("Aucun dataset.")
  else:
            nombre_dataset = len(liste)
            total_lignes = 0
            total_colonnes = 0
            public = 0
            prive = 0
            csv = 0
            json = 0
            domaines = {}
            for dataset in liste:
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