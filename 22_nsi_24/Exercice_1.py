def maxliste(tab):
    max = tab[0]
    for i in range(1, len(tab)-1):
        if tab[i] > max:
            max = tab[i]
    return max


print(maxliste([-27, 24, -3, 15]))
