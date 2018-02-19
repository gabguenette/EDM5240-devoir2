#coding: utf-8

import csv

fichier = "grants.csv"

f1 = open(fichier)
lignes= csv.reader(f1)
next(lignes)

n=0
#objectif=0
#valeur=0

for ligne in lignes:
	n += 1

	#if ligne[17] == "FCP -Innovation commerciale":
		#print(n,ligne)
	#if ligne[17] == "FCP - Aide aux éditeurs de périodiques":
		#print(n,ligne)
	#if ligne[17] == "Initiatives collectives":
		#print(n,ligne)
	if ligne[17] == "FCP -Innovation commerciale":
		print(n,ligne,ligne[13])
	elif ligne[17] == "FCP - Aide aux éditeurs de périodiques":
		print(n,ligne,ligne[13])
	elif ligne[17] == "Initiatives collectives":
		print(n,ligne,ligne[13])




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
