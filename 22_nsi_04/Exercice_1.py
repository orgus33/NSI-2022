def recherche(tab):
    liste = []
    
    for i in range(0, len(tab)-1):
        if (1+tab[i]) == tab[i+1]:
            liste.append((tab[i], tab[i+1]))

    return liste


print(recherche([5, 1, 2, 3, 8, -5, -4, 7]))
