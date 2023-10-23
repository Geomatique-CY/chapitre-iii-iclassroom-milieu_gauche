import csv
import random

# Configuration
nombres_lignes = 3
nombres_groupes_par_ligne = 3
nombres_etudiants_gauche = 3
nombres_etudiants_milieu = 2
nombres_etudiants_droit = 3

# Lecture du CSV contenant les noms/prénoms
students = []
with open('data/noms_m1.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:
        students.append({'firstname': row[0], 'lastname': row[1]})

# Mélange de la liste des étudiants
random.shuffle(students)

# méthode pour "prélever" un élève
def eleve():
    return students.pop()['lastname'] if students else "Personne"

# remplissage de la classroommmm
classe = []
for i in range(nombres_lignes):
    ligne = {}
    for j in range(nombres_groupes_par_ligne):
        nom_groupe = "groupe gauche" if j == 0 else "groupe milieu" if j == 1 else "groupe droit "
        if nom_groupe == "groupe gauche":
            nombres_etudiants = nombres_etudiants_gauche
        elif nom_groupe == "groupe milieu":
            nombres_etudiants = nombres_etudiants_milieu
        else:
            nombres_etudiants = nombres_etudiants_droit
        groupe = [eleve() for _ in range(nombres_etudiants)]
        ligne[nom_groupe] = groupe
    classe.append({f"ligne{i+1}": ligne})

# Affichage de la classe
for ligne in classe:
    for rang, groupes in ligne.items():
        print(f"\n{rang} :\n")
        for nom_groupe, etudiants in groupes.items():
            print(f"  {nom_groupe} : {etudiants}")
