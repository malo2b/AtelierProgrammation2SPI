import random

def message_imc(imc:float) -> str:
    """
    Fonction qui a partir de la valeur d'IMC passé en paramètre
    interprete le resultat
    """
    
    # CONSTANTES #
    PALIER_IMC = [16.5,18.5,25,30,35,40,99]
    INTERPRETATION_IMC = [
        "dénutrition ou famine",
        "maigreur",
        "corpulence normale",
        "surpoids",
        "obésité modérée",
        "obésité sévère",
        "obésité morbide "
    ]
    
    # variables #
    interpretation = ""
    index = 0
    
    while index < len(PALIER_IMC) and interpretation == "":
        if PALIER_IMC[index] > imc:
            interpretation = INTERPRETATION_IMC[index]
        index+=1
        
    return interpretation

def test(nbrTest:int):
    """
    Fonction qui permet de tester la fonction message_imc a partir de nombre aléatoires
    """
    
    for i in range(nbrTest):
        imcToTest = random.randint(10,50)
        print("Verifier correspondance entre {} et {}".format(imcToTest, message_imc(imcToTest)))
    
# test(10)

while True:
    try:
        imc = int(input("Veuillez saisir votre IMC : "))  
        if (imc < 99 and imc > 10):
            break   
        else:
            print("Veuillez saisir une IMC Valide")
    except ValueError:
        print("Veuillez faire une saisie valide !")
        
print(message_imc(imc))