def recherche(tab, n):
    ind_debut = 0
    ind_fin = len(tab)-1

    while ind_fin > ind_debut:
        ind_millieu = (ind_debut + ind_fin) // 2

        if tab[ind_millieu] == n:
            return ind_millieu

        elif tab[ind_millieu] > n:
            ind_fin = ind_millieu - 1

        else:
            ind_debut = ind_millieu + 1
    return -1


print(recherche([2, 3, 4, 6, 7], 5))
