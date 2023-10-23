import csv,random
with open('data/noms_m1.csv', 'r', encoding='utf-8') as csvfile: students = [row[1] for row in csv.reader(csvfile, delimiter=';')] 

nb_rangees, nb_groupes_rangee, nb_etudiants = 3, 3, {"Groupe de gauche": 3, "Groupe du milieu": 2, "Groupe de droite": 3} 
eleve = lambda: students.pop((random.randrange(len(students)))) if students else "Personne" 
classe = [{f"Rangée {i+1}": {nom: [eleve() for _ in range(nombres)] for nom, nombres in nb_etudiants.items()}}for i in range(nb_rangees)]

[print(f"\n{nom_rang} :\n" + '\n'.join([f" {nom_groupe} : {', '.join(etudiants)}" for nom_groupe, etudiants in groupes.items()])) for rang in classe for nom_rang, groupes in rang.items()]


# C'est pas une lecture de repos

# Variables et dataprocessing
# 2 - Création de la liste de prénoms "students" depuis le csv placé dans le dossier data
# 4 - Configuration, on peut changer les valeurs de toutes les variables pour customiser la disposition de la classe et le code s'adaptera 
# 5 - Définition de la fonction eleve() qui permet de prélever un prénom de la liste avec pop(), de façon aléatoire avec random.randrange(), si on épuise la liste, on inscrit "Personne"
# 6 - Création de la liste de dictionnaires imbriqués qui représente la classe lol
#      - Chaque élément de la liste est un dictionnaire qui représente une rangée de la salle de classe, et les clés de ce dictionnaire sont les noms des rangées
#      - À l'intérieur de chaque dictionnaire de rangée, on a un autre dictionnaire où les clés représentent les différents groupes de ladite rangée. Les valeurs de ces clés sont les listes de noms d'étudiants de chaque groupe
#      - Chaque élément imbriqué est rempli avec des boucles "for" qui s'adaptent et réutilisent les éléments que j'ai définis dans les lignes 4 et 5

# Affichage
# 8 - Lecture de liste de dictionnaires imbriqués
#      - Avec " for rang in classe ", on itère chaque rangée de la salle et on stocke toutes les données d'une rangée dans "rang"
#
#         - Avec " for nom_rang, groupes in rang.items() " :
#           On itère sur les éléments (paires clé-valeur) du dictionnaire "rang"
#           "nom_rang" est la clé (le nom de la rangée), et "groupes" est la valeur (le dictionnaire de groupes)
#
#         - "f"\n{nom_rang} :\n" récupère ce nom de rangée pour chaque input d'entête de rangée 
#                   
#             - " \n'.join([f" {nom_groupe} : {', '.join(etudiants)} " for nom_groupe, etudiants in groupes.items()]) "
#               C'est l'endroit où chaque groupe et sa liste d'étudiants sont formatés et concaténés ("".join") avec un retour à la ligne ("\n") entre chaque groupe ("groupes.item")
#               Je rappelle que "groupes" est le dictionnaire qui contient le nom du groupe et la liste des prénoms des étudiants de ce même groupe
#               Dans ces dictionnaires, "nom_groupe" est la clé et "etudiants" est la valeur (une liste de prénoms)
#               {', '.join(etudiants)} permet de print la liste de cette façon : "Erwan, Clémence, Chloé", au lieu de "['Erwan', 'Clémence', 'Chloé']"