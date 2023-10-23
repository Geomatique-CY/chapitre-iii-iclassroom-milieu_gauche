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


# Methode pour avoir tous les prénoms
for x in students:
    print(x['lastname'])

# méthode pour avoir un prénom en particulier
print(students[1]['lastname'])

variable = len (students)
print(variable)
