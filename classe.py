import csv
import random

# Lecture du CSV contenant les noms/ prénoms
students = []
with open('data/noms_m1.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:
        students.append({'firstname': row[0], 'lastname': row[1]})


print(students) # debug

# melange de liste des etudiants 
random.shuffle(students)


#test affichage de tous les prénoms
for student in students:
    print(student['lastname'])