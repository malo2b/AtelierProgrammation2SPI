from ex2 import anneeBissextile
from datetime import date
 
def dateEstValide(jour:int,mois:int,annee:int):
    """
    Verifie si la date entrez par l'utilisateur est valide
    """
    estValide = False
    estBissextile = anneeBissextile()
    if(jour>=1 and jour <= 31):
        if(mois>=1 and mois<=12):
            if(annee>0):
                estValide = True
    return estValide
    
    
def saisieDateNaissance():
    """
    Fonction de saisie date de naissance
    """
    
    # Saisie utilisateur #
    
    while True:
        try:
            jj = int(input("Veuillez saisir votre jour de naissance :  "))
            mm = int(input("Veuillez saisir votre mois de naissance :  "))  
            yyyy = int(input("Veuillez saisir votre année de naissance :  "))  
            if dateEstValide(jj,mm,yyyy):
                break   
            else:
                print("Veuillez saisir une date de naissance valide !")
        except ValueError:
            print("Veuillez saisir une date de naissance valide !")
            
    return datetime.date(yyyy,mm,jj)

    

def age(dateNaissance):
    date.today
    
# def estMajeure(dateNaissance):

# def testAcces():
    