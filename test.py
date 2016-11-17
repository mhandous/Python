#!/usr/bin/python3
# import de la lyb sys

import sys

print (sys.version_info)
print (sys.version)

print (sys.platform)

print ("Hello")
print ('Hello')
print ("C'est")
print ("""   texte

            a la suite""")
print ("C'est le test dans C:\\user")
strAdresse = "Spam"
print(strAdresse)

# définition des variable de la liste de a
print ("--->définition des variable de la liste de a")
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# affichage des 4 premier
print (a[:4])
#affichage des 2 du milieu
print (a[3:-3])
# affichage du 4 dernier
print (a[+4:])

i = 5
mykey = "dog"
fois = 20
# % sont les valeur entre (i, mykey, fois) d ex %d pour les decimal, s ex s%
print ('la valeur %d et le mot \'%s\' apparaissent %d fois.' % (i, mykey, fois))

print('la valeur {} et le mot \'{}\' appraissent {} fois'.format(i, mykey, fois))

#test conditionnel
print ("--->Test Conditionnel")
valeur = "dog"
# si la valeur et egale a cat
if valeur == "cat" :
    print ("ok")
# et si
elif valeur == "dog" :
    print ("dog ok")
# sinon
else:
    print ("inconnu")

# Test conditionnel 2
print ("--->Test conditionnel 2")
valeur = "toto"
valeur2 = "titi"
# Si la valeur est egale a toto et valeur2 egale a titi alors imprime a l'ecran OK
if valeur == "toto" and valeur2 == "titi" :
    print ("OK pour les valeurs")

# Boucle
print ("boucle")
seq = [1,2,3,4]
a,b,c,d = seq
print (a)
# pour tous les carracters qui sont dans spam on imprime letter
for letter in "Spam" :
    print ("current letter", letter)
# on fait une boucle sur une liste fruit et la variable et fruits et la liste
fruits = ['banane', 'pomme', 'mangue']
for fruit in fruits :
    print ("mon fruit", fruit)
# on fait une boucle de 1 a 10 et si dans la boucle passe 6 on arrete la boucle avec la commande break
for num in range (1,10) :
    print (num)
    if num == 5 :
        continue
    if num == 7 :
        break

# while True est une valeur qui est toujours vrais / var = var +1 on rajoute 1 dans l'exemple si dessous on decremente pour la fin de la boucle
print ("---> Fin de boucle conditionnel par de-incrementation")
var = 10
while True :
    var -=1
    if (var ==6) :
        continue
    print (var)
    if (var == 0) :
        break

print ("End Loop")

# Compreention list paste la liste en faisant un boucle inversé
print ("---> Compreention")
a = [1,2,3,4,5,6,7,8,9,10]
#elevation au carre
squares = [x**2 for x in a]
print (squares)
ange


