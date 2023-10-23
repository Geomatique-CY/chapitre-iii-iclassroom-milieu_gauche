import csv,random

nombres_lignes, nombres_groupes_par_ligne,nombres_etudiants = 3, 3, {"groupe gauche": 3, "groupe milieu": 2, "groupe droit": 3}

with open('data/noms_m1.csv', 'r', encoding='utf-8') as csvfile: students = [row[1] for row in csv.reader(csvfile, delimiter=';')]

random.shuffle(students)
eleve = lambda: students.pop() if students else "Personne"

classe = [{f"ligne{i+1}": {nom: [eleve() for _ in range(nombres)] for nom, nombres in nombres_etudiants.items()}}for i in range(nombres_lignes)]

[print(f"\n{rang} :\n" + '\n'.join([f"  {nom_groupe} : {etudiants}" for nom_groupe, etudiants in groupes.items()])) for ligne in classe for rang, groupes in ligne.items()]