from math import sqrt 
import random

def discriminant(a:float,b:float,c:float) -> float:
    """fonction permettant de retourner le discriminant pour une equation sous la forme ax2+bx+c"""
    return b*b-(4*a*c)

def racine_unique(a:float,b:float) -> float:
    """
    fonction de calcul d'une racine unique pour un polynome de degré 2
    """
    return -b / 2 * a

def racineDouble(a,b,delta,num) -> float:
    """
    fonction permettant de calculer les solutions d'une equations du second ordre 
    """
    resultat = 0.0
    if(num==1):
        resultat = (-b+sqrt(delta))/(2*a)
    else:
        resultat = (-b-sqrt(delta))/(2*a)
    return resultat
    
    
def str_equation(a,b,c) -> str:
    """formate le format d'affichage pour l'equation """
    return "{}x2 + {}x + {}".format(a,b,c)
    
    
def solution_equation(a,b,c) -> str:
    """
    fontion qui appel les fonctions pour determiner l'equation
    et retourne une chaine de caractère formatée avec le resultat
    """
    solution = ""
    
    delta = discriminant(a,b,c)
    
    if (delta < 0):
        solution = "Solution de l'équation {}=0 Pas de racine réelle".format(str_equation(a,b,c))
    elif (delta == 0):
        solution = "Solution de l'équation {}=0 Racine unique : x = {}".format(str_equation(a,b,c),racine_unique(a,b))
    else:
        solution = "Solution de l'équation {}=0 \n Deux racines \n x1= {} \n x2= {}".format(str_equation(a,b,c),round(racineDouble(a,b,delta,1),2),round(racineDouble(a,b,delta,2),2))
    
    return solution
    
def equation(a:float,b:float,c:float) -> None:
    """
    Procédure d'appel a la résolution de l'equation
    """
    print(solution_equation(a,b,c))
     
    
def test_equation(nbrTests:int) -> None:
    """
    Procédure de test de l'equation
    """
    for i in range(nbrTests):
        a = random.randint(-10,+10)
        b = random.randint(-10,+10)
        c = random.randint(-10,+10)
        print("Pour a = {} b = {} c = {} : ".format(a,b,c))
        equation(a,b,c)
        print("\n\n")
        
test_equation(3)