# EDM5240-devoir2
#coding : utf-8

#Par Myriam Eddahia

#On importe notre fichier et on demande de l'ouvrir pour avoir accès aux données.

import csv

subventions = "grants.csv"

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
	n+=1

	if ligne[17] == "FCP - Aide aux éditeurs de périodiques":
		annee = ligne[0]
		print(n,ligne)
		#Pour isoler l'année au cours de laquelle la subvention a été octroyée.
		print("La subvention a été octoyée en " + annee[3:7] + ".")

	elif ligne[17] == "FCP - Innovation commerciale":
		annee = ligne[0]
		print(n,ligne)
		#Pour isoler l'année au cours de laquelle la subvention a été octroyée.
		print("La subvention a été octoyée en " + annee[3:7] + ".")

	elif ligne[17] == "Initiatives collectives":
		annee = ligne[0]
		print(n,ligne)
		#Pour isoler l'année au cours de laquelle la subvention a été octroyée.
		print("La subvention a été octoyée en " + annee[3:7] + ".")

#Il faut trouver le nom des subventions
#On cherche les subventions octroyées par le Fonds du Canada pour les périodiques (les transactions de trois subventions).
#On filtre ensuite la liste des fonds pour ne retenir que ceux qui nous intéresse.
