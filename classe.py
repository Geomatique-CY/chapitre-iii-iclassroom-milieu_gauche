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
if 'lastname ' in students :
    students.remove('lastname ')
n=1

def groupe3(n, groupe) :
    for u in range(3) : 
        groupe += students[n]['lastname']+ ' '
        n+=1
    return(groupe)

def groupe2(n, groupe) : 
    for u in range(2) : 
        groupe += students[n]['lastname']+ ' '
        n+=1
    return(groupe)
for i in range (3) :
    g1=''
    g1 = groupe3(n, g1)
    n+=3

    g2 = ''
    g2 = groupe2(n, g2)
    print(g1 + '        ' + g2)
