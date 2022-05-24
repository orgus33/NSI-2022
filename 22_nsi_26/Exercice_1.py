def RechercheMin(tab):
    min = 0
    for i in range(1, len(tab)):
        if tab[i] < tab[min]:
            min = i
    return min
    

print(RechercheMin([5, 3, 2, 2, 4]))