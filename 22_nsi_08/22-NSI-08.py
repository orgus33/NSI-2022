def insere(a, tab):
    l = list(tab)  # l contient les mêmes éléments que tab
    l.append(a)
    i = len(tab) - 1
    while a < l[i] and i >= 0:
        l[i+1] = tab[i]
        l[i] = a
        i = i - 1
    return l


print(insere(1, [2, 3, 4]))
