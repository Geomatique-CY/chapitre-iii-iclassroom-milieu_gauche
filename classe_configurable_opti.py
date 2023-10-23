import csv
import random

config = {
    'nombres_lignes': 3,
    'nombres_etudiants': {"groupe gauche": 3, "groupe milieu": 2, "groupe droit": 3}
}

try:
    with open('data/noms_m1.csv', 'r', encoding='utf-8') as csvfile:
        students = [{'firstname': row[0], 'lastname': row[1]} for row in csv.reader(csvfile, delimiter=';')]
except FileNotFoundError:
    students = []

def eleve():
    return students.pop()['lastname'] if students else "Personne"

classe = [
    {
        f"ligne{i + 1}": {
            nom_groupe: [eleve() for _ in range(nombre_etudiants)]
            for nom_groupe, nombre_etudiants in config['nombres_etudiants'].items()
        }
    }
    for i in range(config['nombres_lignes'])
]

for ligne in classe:
    for rang, groupes in ligne.items():
        print(f"\n{rang} :\n")
        for nom_groupe, etudiants in groupes.items():
            print(f"  {nom_groupe} : {etudiants}")
