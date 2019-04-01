# coding: utf-8

import time 
from random import randint
print("Bonjour, je suis TARS.")
#time.sleep(2)
print("Jouons à un petit jeu.")
#time.sleep(2)
print("Chacun de nous deux va choisir un entier entre 1 et 10.")
#time.sleep(2)
print("Chaque chiffre sera additionné avec le précédent.")
#time.sleep(2)
print("Le premier de nous deux qui fait arriver la somme à 100 aura gagné.")
#time.sleep(2)
print("Facile non ? ")
#time.sleep(2)


réponse =input("Es-tu prêt ? O/N     ")



def jeu():
	somme =1
	ordinateur=1
	if réponse.lower()=="o":
		while somme < 100:		
			print("                                  ORDINATEUR : "+ str(ordinateur))
			print("                 TOTAL : "+str(somme))
			joueur=int(input("Nombre du Joueur : "))		
			if joueur<1 or joueur >10:
				print("Il faut choisir entre 1 et 10 !")
			somme +=joueur
			if somme==100:
				print("Bravo tu as gagné !")
			print("                 TOTAL : "+ str(somme))
			ordinateur = 11 -joueur
			#print("Je choisis le chiffre : "+ str(ordinateur))
			somme += ordinateur
			if somme ==100:
				print("Je choisis : "+str(ordinateur)) 
				print("                 TOTAL : "+ str(somme))
				print("Tu as perdu!")
				trouvé=input("As-tu trouver pourquoi ? O/N     ")
				if trouvé.lower()=="o":
					print("Bravo petit malin!")
					time.sleep(3)
					print("Passons au niveau suivant...")
					#load lvl2
				else:				
					retry=input("Veux-tu rejouer ? O/N     ")
					if retry.lower()=="o":
						return jeu()
					else:
						print("Merci d'avoir joué, au revoir")
						for x in range(1,6):
							print("Fermeture du programme dans "+str(6-x)+" secondes")
							time.sleep(1)
						print("Tchou!")					
						quit()
	else:
		print("Au revoir.")
		for x in range(1,4):
			print("Fermeture du programme dans "+str(4-x)+" secondes")
			time.sleep(1)
		print("Tchou!")
		quit()
jeu()

def jeu2():
	somme =1	
	while somme < 100:		
			
			joueur=int(input("Joueur ? "))		
			if joueur<1 or joueur >10:
				print("Il faut choisir entre 1 et 10 !")
			somme +=joueur
			print("                 TOTAL : "+ str(somme))
			if somme==100:
				print("Bravo tu as gagné !")
			#if somme>(56)
			ordinateur=randint(1,10)
			print("                                  ORDINATEUR : "+ str(ordinateur))
			somme += ordinateur
			print("                 TOTAL : "+str(somme))

			if somme ==100:
				print("Je choisis : "+str(ordinateur)) 
				print("                 TOTAL : "+ str(somme))
				print("Tu as perdu!")
				trouvé=input("As-tu trouver pourquoi ? O/N     ")
				if trouvé.lower()=="o":
					print("Bravo petit malin!")
					time.sleep(3)
					print("Passons au niveau suivant...")
					#load lvl2
				else:				
					retry=input("Veux-tu rejouer ? O/N     ")
					if retry.lower()=="o":
						return jeu()
					else:
						print("Merci d'avoir joué, au revoir")
						for x in range(1,6):
							print("Fermeture du programme dans "+str(6-x)+" secondes")
							time.sleep(1)
						print("Tchou!")					
						quit()

#jeu2()