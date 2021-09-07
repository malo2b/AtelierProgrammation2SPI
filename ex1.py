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

print(message_imc(17))