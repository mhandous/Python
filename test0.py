# on a 2 variables  temps et distance
# calcul de la vitesse
print("--->calcul de la vitesse<---")
temps = 6.896
distance = 19.7

vitesse = distance/temps
# affichage formatte
print ("La vitesse est - {:.2f} mettre par seconde".format(vitesse))
#{} permet d'inclure la varialbe vitesse qui doit etre declarer en fin de ligne par format(vitesse) format
# permet de reperer les balises
# nomeclature ex. print(msg.format(vitesse))

# en utilisant la fonction range
# afficher les entier de 0 a 3
# de 4 a 7
for i in range(0,4):
    print (i)

for i in range (0,10):
    if i > 3:
        print ("---", i)
    if i == 7:
        break

# avec une boucle afficher les caracteres de la chaine suivante
msg="C'est la formation DevOps"
for c in msg:
    print (c)


# sur la liste suivante faire les action suivantes
liste = [ 17,38,10,25,72]
# trier et aficher la liste
liste.sort()
print (liste)
#ajouter l'element 12 et afficher la liste
liste.append(12)
print (liste)
#afficher l'indice de l'element 17
print (liste.index(17))
#elevezl'element 38 et afficher la liste
liste.remove(38)
print(liste)
#afficher la sous liste du 3eme element jusqu'a la fin de la liste
print(liste[2:])
