def recherche(elt, tab):
    indices = []
    for i in range(len(tab)):
        if tab[i] == elt:
            indices.append(i)
    return indices


print(recherche(3, [3, 2, 1, 3, 2, 1]))
print(recherche(4, [1, 2, 3]))
