def convertir(T):
    """ 
    T est un tableau d'entiers, dont les éléments sont 0 ou 1 et 
    représentant un entier écrit en binaire. Renvoie l'écriture 
    décimale de l'entier positif dont la représentation binaire 
    est donnée par le tableau T 
    """
    multiplication = len(T)-1

    result = 0
    for n in T:
        result += 2 ** multiplication * n
        multiplication = multiplication - 1
    return result


print(convertir([1, 0, 1, 0, 0, 1, 1]))
print(convertir([1, 0, 0, 0, 0, 0, 1, 0]))
