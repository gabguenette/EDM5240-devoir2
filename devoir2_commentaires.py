### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###

#coding: utf-8

import csv

### Je modifie simplement le nom du fichier pour faire rouler ton code sur mon ordi

fichier = "../grants.csv"

f1 = open(fichier)
lignes= csv.reader(f1)
next(lignes)

n=0
#objectif=0
#valeur=0

for ligne in lignes:
### C'est bien d'avoir pensé inclure un compteur, mais il compte l'ensemble des subventions contenues dans le fichier «grants.csv»
### Je vais le mettre en commentaire
###	n += 1

	#if ligne[17] == "FCP -Innovation commerciale":
		#print(n,ligne)
	#if ligne[17] == "FCP - Aide aux éditeurs de périodiques":
		#print(n,ligne)
	#if ligne[17] == "Initiatives collectives":
		#print(n,ligne)
	if ligne[17] == "FCP -Innovation commerciale":
		n += 1
		print(n,ligne,ligne[13])
	elif ligne[17] == "FCP - Aide aux éditeurs de périodiques":
		n += 1
		print(n,ligne,ligne[13])
	elif ligne[17] == "Initiatives collectives":
		n += 1
		print(n,ligne,ligne[13])

### Très intéressantes lignes commentées, ci-dessous, qui me permettent vraiment de comprendre ta démarche

	#print(n,ligne)
	#inv = (ligne[-1])
	#inv = (ligne[-2])
	#inv = (ligne[-3])
	#inv = (ligne[-4])
	#inv = (ligne[-5])
	#inv = (ligne[17])

	#print (inv)


#for l in lignes:
	#n += 1
	#print (n,l)

#if ligne[17]=="Fonds du Canada pour les périodiques: Innovation commerciale - Imprimés":
	#print (ligne)

#if objectif == "Fonds du Canada pour les périodiques: Initiatives collectives":
	#print (objectif)

#for ligne in lignes:
	#try:
		#print (ligne[17]("Fonds du Canada pour les périodiques: Innovation commerciale - Imprimés"))
	#except:
		#print ("NON")


### Intéressante méthode, avec un «if» et deux «elif»
### Encore plus simple: un seul «if» grâce auquel on teste deux conditions séparées par un «or»:
### «if "Fonds du Canada pour les périodiques" in ligne[17] or "FCP -" in ligne[17]:»
### Cela permet d'aller chercher plus de subventions: 4608, ce qui correspond davantage à ce qu'on cherche
### Car tes «if» et «elif» ne fonctionnent que si toute la ligne[17] correspond à l'expression recherchée,
### ce qui fait que ton code ne trouve que 2350 subventions.

### En outre, je demandais d'afficher l'année
### La ligne[13] est la date complète à partir de laquelle il fallait extraire l'année