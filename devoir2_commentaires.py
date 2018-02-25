# EDM5240-devoir2
#coding : utf-8

### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###

#Par Myriam Eddahia

#On importe notre fichier et on demande de l'ouvrir pour avoir accès aux données.

import csv

### Je modifie simplement le nom du fichier pour faire rouler ton code sur mon ordi

subventions = "../grants.csv"

f1 = open(subventions)
programmes = csv.reader(f1)
next(programmes)

#Voici les trois programmes qui s'inscrivent dans le Fonds du Canada pour les périodiques : Aide aux éditeurs de périodiques, Innovation commerciale et Initiatives collectives.

#for ligne in programmes:
	#print(ligne[17])

#17 étant la position dans laquelle nous trouverons le nom du fond octroyé.
n=0

for ligne in programmes:
	#Pour chaque ligne dans l'ensemble des données de subventions, cibler les programmes qui bénéficient du Fonds du Canada pour les périodiques. 

### Ton compteur compte toutes les lignes.
### Si tu souhaites compter uniquement les subventions du Fonds qu'on recherche,
### il faut mettre ce compteur dans chacun de tes «if» ou «elif» ci-dessous

	# n+=1

	if ligne[17] == "FCP - Aide aux éditeurs de périodiques":
		annee = ligne[0]
		n += 1
		print(n,ligne)
		#Pour isoler l'année au cours de laquelle la subvention a été octroyée.

		### Bien, sauf que la date de la subvention se trouve dans l'élément ligne[13]
		### Il faut donc, pour obtenir l'année, faire «ligne[13][:4]»

		print("La subvention a été octoyée en " + annee[3:7] + ".")

	elif ligne[17] == "FCP - Innovation commerciale":
		annee = ligne[0]
		n += 1
		print(n,ligne)
		#Pour isoler l'année au cours de laquelle la subvention a été octroyée.
		print("La subvention a été octoyée en " + annee[3:7] + ".")

	elif ligne[17] == "Initiatives collectives":
		annee = ligne[0]
		n += 1
		print(n,ligne)
		#Pour isoler l'année au cours de laquelle la subvention a été octroyée.
		print("La subvention a été octoyée en " + annee[3:7] + ".")

#Il faut trouver le nom des subventions
#On cherche les subventions octroyées par le Fonds du Canada pour les périodiques (les transactions de trois subventions).
#On filtre ensuite la liste des fonds pour ne retenir que ceux qui nous intéresse.

### Ton code est bien, mais il n'identifie pas certaines subventions.
### Il permet de trouver 2310 subventions.
### Pour être certain de tout trouver, il fallait une condition plus simple, mais double, avec un «or»:
### «if "Fonds du Canada pour les périodiques" in ligne[17] or "FCP -" in ligne[17]:»
### On en identifie alors 4608.