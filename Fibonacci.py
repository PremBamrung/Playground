#on utilise la tibrairie time pour pouvoir faire un benchmark
import time

#fonction qui calcule le nième nombre de la suite de fibonacci
def Fibo(n) :
    a,b,c=1,1,1
    if (n==1) :
        return(a)
    elif (n==2) :
        return(b)
    else :
        while (c<n-2) :
            a,b,c=b,a+b,c+1
        return(a+b)

#n=int(input("Juste qu'à combien ? "))
n=67



#Pour afficher chaque nombre jusqu'à n
#Requiert beaucoup plus de temps, le temps d'affichage est plus long que le temps de calcul
#i=1
#while (i<n+1):
#  print(Fibo(i))
#  i+=1



#Affiche la nième valeur de la suite
print("Le nième nombre de la suite par itération est : ")   #+str(Fibo(n)))
#démarre le timer
start=time.time()
print(Fibo(n))
#arrête le timer
end=time.time()



#affiche le temps de calcul par itération
print("Temps de calcul par itération est de : ")
print(str(end-start)+" s")

#affiche le ratio n/(n-1) pour calculer phi le nombre d'or
ratio=float(Fibo(n))/float(Fibo(n-1))
print("Le ration est de : ")
print(str(ratio))

#affiche la différence entre le phi et le ratio calculé 
similitude=float(ratio)/float((1+5**0.5)/2)
print("La similitude avec phi est de :")
print(str(similitude))


#valeur exacte de phi
#print(float((1+5**0.5)/2))

# valeur approché de phi avec un grand nombre de chiffres
phi=1.618033988749894848204586834365638117720309179805762862135448622705260462189024497072072041 

#formule de binet permet de calculer le nième sans récursion ni itération

def binet(n):
  r=1/5**0.5*(((5**0.5+1)/2)**n-((-5**0.5+1)/2)**n)
  return r



#affiche le nième nombre de la suite avec la formule de binet
print("Le nième nombre de la suite avec la formuel de Binet est : ")#+str(binet(n)))
#commence un second timer  
start2= time.time()
print(binet(n))
#arrête le second timer
end2=time.time()

#affiche le temps de calcul pour la formule de binet
print("Temps de calcul avec la formule de Binet est de :")
print(str(end2-start2)+" s")