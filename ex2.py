import random


def anneeBissextile(annee:int):
    """
    Inputs: int:annee
    Outputs: bool:True if bissextile else false
    """
    res = False
    if (annee % 4 == 0 and (annee % 100 != 0)) or annee % 400 == 0:
        res = True
    return res

def test_est_bissextile(nbrTest:int) -> None:
    for i in range(nbrTest):
        anneeRandom = random.randint(-1000,2050)
        print("L'année {} est bissextile ? : {}".format(anneeRandom,anneeBissextile(anneeRandom)))

# test_est_bissextile(10)