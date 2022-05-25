def RechercheMin(tab):
    ind_min = 0

    for i in range(1, len(tab)):
        if tab[i] < tab[ind_min]:
            ind_min = i
    return ind_min


print(RechercheMin([5, 3, 2, 2, 4]))
