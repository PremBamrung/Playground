#on utilise la tibrairie time pour pouvoir faire un benchmark
import time
from decimal import Decimal,getcontext
#from numba import jit
#from progress.bar import ChargingBar
print("getcontext().prec= ",getcontext().prec)

#n=int(input("Juste qu'à combien ? "))
n=(3)

#fonction qui calcule le nième nombre de la suite de fibonacci
#suffix = '%(percent)d%% [%(elapsed_td)s / %(eta)d / %(eta_td)s]'
#bar = ChargingBar('Processing',max=n )
#@jit(nopython=True)
#getcontext().prec = 15


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ ," took " )
        print( (end-start) , " ms")
        return result
    return wrapper

#@time_it    
def Fibo(n) :
    a,b,c=1,1,1
    if (n==1) :
        return(a)
    elif (n==2) :
        return(b)
    else :
        while (c<n-2) :
            a,b,c=b,a+b,c+1
            
            #bar.next()
        #bar.finish()
        return(a+b)





#Affiche la nième valeur de la suite
print("Le nième (",n,") nombre de la suite par itération est : ")   #+str(Fibo(n)))
#démarre le timer
start=Decimal(time.time()) 
result=Fibo(n)
#arrête le timer
end=Decimal(time.time())
print(result)



#affiche le temps de calcul par itération
print("Temps de calcul par itération est de : ")
print(str(end-start)+" s")

#affiche le ratio n/(n-1) pour calculer phi le nombre d'or
ratio=Decimal(result)/Decimal(Fibo(n-1))
print("Le ratio est de : ")
print(str(ratio))

#affiche la différence entre le phi et le ratio calculé 
similitude=Decimal(ratio)/Decimal((1+5**0.5)/2)
print("La similitude avec phi est de :")
print(str(similitude))


#valeur exacte de phi
#print(float((1+5**0.5)/2))

# valeur approché de phi avec un grand nombre de chiffres
phi=1.618033988749894848204586834365638117720309179805762862135448622705260462189024497072072041 

#formule de binet permet de calculer le nième sans récursion ni itération

def binet(n):
    a=Decimal(1)
    b=Decimal(5)
    c=Decimal(0.5)
    d=Decimal(2)
    n=Decimal(n)

    r=a/b**c*(((b**c+a)/d)**n-((-b**c+a)/d)**n)
    return r



#affiche le nième nombre de la suite avec la formule de binet
print("Le nième nombre de la suite avec la formuel de Binet est : ")#+str(binet(n)))
#commence un second timer  
start2= Decimal(time.time())
result_binet=binet(n)
#arrête le second timer
end2=Decimal(time.time())
print(result_binet)

#affiche le temps de calcul pour la formule de binet
print("Temps de calcul avec la formule de Binet est de :")
print(str(end2-start2)+" s")


# Python Fibonacci series Program using For Loop

# Fibonacci series will start at 0 and travel upto below number
#Number = int(input("Please Enter the Range Number: "))
Number=n
# Initializing First and Second Values of a Series

           
# Find & Displaying Fibonacci series
@time_it
def fibo_for(Number):
    First_Value = 0
    Second_Value = 1
    for Num in range(1, Number+1):
            if(Num <= 1):
                        Next = Num
            else:
                        Next = First_Value + Second_Value
                        First_Value = Second_Value
                        Second_Value = Next
    return(Next)

print("For loop")
print(fibo_for(Number))


@time_it
def fibo_while(Number):
    i = 1
    First_Value = 0
    Second_Value = 1
    while(i < Number+1):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           i = i + 1
    return(Next)

print("While loop")

print(fibo_while(n))


# Recursive Function Beginning
@time_it
def fibo_recur(Number):
    if(Number < 2):
        return Number
    else: 
        resultat=(fibo_recur(Number - 2)+ fibo_recur(Number - 1))
    return(resultat)

print("Recursive")
print(fibo_recur(n))
