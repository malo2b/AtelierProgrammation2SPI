from ex2 import anneeBissextile
import datetime as date

def date_est_valide(jour:int,mois:int,annee:int) -> bool:
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

    if anneeBissextile(annee):
        DAY_OF_MONTH[2] = 29

    return mois >=1 and mois <= 12 and jour >=1 and jour <= DAY_OF_MONTH[mois] and date.date.today() > date.date(annee,mois,jour)


def saisie_date_naissance() -> date:
    """
    Fonction de saisie date de naissance
    Output:
        date:date_naissance
    """

    # Saisie utilisateur #

    while True:
        try:
            jj = int(input("Veuillez saisir votre jour de naissance :  "))
            mm = int(input("Veuillez saisir votre mois de naissance :  "))
            yyyy = int(input("Veuillez saisir votre année de naissance :  "))
            if date_est_valide(jj,mm,yyyy):
                break
            else:
                print("Veuillez saisir une date de naissance valide !")
        except ValueError:
            print("Veuillez saisir une date de naissance valide !")

    return date.date(yyyy,mm,jj)

def age(date_naissance:date) -> int:
    """
    Inputs: date:date_naissance
    Output: int: Age
    """

    date_ajourdhui = date.date.today()
    calcul_age = date_ajourdhui - date_naissance
    return int(calcul_age.days/365.25)

def est_majeur(date_naissance:date) -> bool:
    """
    Inputs:
        date:date_naissance
    Output: bool True si majeur, False sinon
    """

    AGE_MAJORITE = 18
    DATEDAUJOURDHUI = date.date.today()
    est_majeure = False
    calcul_age = DATEDAUJOURDHUI.year - date_naissance.year
    if calcul_age>=AGE_MAJORITE:
        est_majeure = True
    return est_majeure

def test_acces() -> None:
    """
    Procédure pour démarer un test d'accès
    """
    date_naissance = saisie_date_naissance()
    print ("Bonjour vous avez {} ans".format(age(date_naissance)))
    if est_majeur(date_naissance):
        print("Accès autorisé")
    else:
        print("Accès interdit")

test_acces()
