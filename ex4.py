from ex2 import anneeBissextile
import datetime as date
 
def dateEstValide(jour:int,mois:int,annee:int) -> bool:
    """
    Inputs:
        int:jour, mois, annee # Correspondant a une date de naissance
    Outputs:
        bool: Si date valide True sinon False
    """
    
    # CONSTANTES #
    DAY_OF_MONTH = [
        None,31,28,31,30,31,30,31,31,30,31,30,31 # Tableau contenant le nombre de jour dans le mois 
    ]                                            # correspondant a l'index
    
    # Variables #
    estValide = False
    estBissextile = anneeBissextile(annee)

    if estBissextile:
        DAY_OF_MONTH[2] = 29
        
    if int(annee):
        if mois >=1 and mois <= 12:
            if jour >=1 and jour <= DAY_OF_MONTH[mois]:
                if (date.date.today() > date.date(annee,mois,jour)):
                    estValide = True
                    
    return estValide
    
    
def saisieDateNaissance() -> date:
    """
    Fonction de saisie date de naissance
    Output:
        date:dateNaissance 
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
            
    return date.date(yyyy,mm,jj)

def age(dateNaissance:date) -> int:
    """
    Inputs: date:dateNaissance
    Output: int: Age
    """
    
    dateAjourdhui = date.date.today()
    age = dateAjourdhui - dateNaissance
    return int(age.days/365.25)
    
def estMajeur(dateNaissance:date) -> bool:
    """
    Inputs:
        date:dateNaissance
    Output: bool True si majeur, False sinon
    """
    
    AGE_MAJORITE = 18
    DATEDAUJOURDHUI = date.date.today()
    estMajeure = False
    age = DATEDAUJOURDHUI.year - dateNaissance.year
    if(age>=AGE_MAJORITE):
        estMajeure = True
    return estMajeure    

def testAcces() -> None:
    """
    Procédure pour démarer un test d'accès
    """
    dateNaissance = saisieDateNaissance()
    print ("Bonjour vous avez {} ans".format(age(dateNaissance)))
    if estMajeur(dateNaissance):
        print("Accès autorisé")
    else:    
        print("Accès interdit")
    
testAcces()