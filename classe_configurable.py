import csv
import random

# Configuration
nombres_lignes = 3
nombres_groupes_par_ligne = 3
nombres_etudiants = {"groupe gauche": 3, "groupe milieu": 2, "groupe droit": 3}

# Lecture du CSV contenant les noms/prénoms
with open('data/noms_m1.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    students = [{'firstname': row[0], 'lastname': row[1]} for row in csvreader]

# Mélange de la liste des étudiants
random.shuffle(students)

# Méthode pour "prélever" un élève
def eleve():
    return students.pop()['lastname'] if students else "Personne"

# Remplissage de la salle de classe
classe = []
for i in range(nombres_lignes):
    ligne = {}
    for nom_groupe, nombre_etudiants in nombres_etudiants.items():
        groupe = [eleve() for _ in range(nombre_etudiants)]
        ligne[nom_groupe] = groupe
    classe.append({f"ligne{i+1}": ligne})

# Affichage de la classe
for ligne in classe:
    for rang, groupes in ligne.items():
        print(f"\n{rang} :\n")
        for nom_groupe, etudiants in groupes.items():
            print(f"  {nom_groupe} : {etudiants}")
