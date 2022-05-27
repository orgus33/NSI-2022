def recherche(tab, n):
    indice = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            indice = i

    return indice


print(recherche([5, 3], 1))
print(recherche([2, 4], 2))
print(recherche([2, 3, 5, 2, 4], 2))
