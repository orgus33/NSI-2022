def maxi(tab):
    max = tab[0]
    for i in range(1, len(tab)-1):
        if tab[i] > max:
            max = tab[i]
            ind = i
    return (max, ind)


print(maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
