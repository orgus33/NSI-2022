def recherche(elt, tab):
    indice = -1
    index = 0

    while indice == -1:
        if tab[index] == elt:
            indice = index
        index += 1

    return indice


print(recherche(50, [10, 8, 7, 52, 50, 8, 8, 8, 9, 2, 4, 3, 1, 50, 1]))


# Autre option
def recherche(elt, tab):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return -1
