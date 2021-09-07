def message_imc(imc:float):
    """
    Fonction qui a partir de la valeur d'IMC passé en paramètre
    interprete le resultat
    """
    
    # CONSTANTES #
    PALIER_IMC = [16.5,18.5,25,30,35,40]
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
    
    for index, seuilImc in PALIER_IMC:
        if imc < seuilImc:
            interpretation = INTERPRETATION_IMC[index]
