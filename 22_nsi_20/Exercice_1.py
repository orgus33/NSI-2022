def xor(tab1, tab2):
    tab = []
    for i in range(len(tab1)):
        if tab1[i] + tab2[i] == 1:
            tab.append(1)
        else:
            tab.append(0)
    return tab


a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]


print(xor(a, b))
print(xor(c, d))


# Ou :


def xor(a, b):
    resultat = []
    for i in range(len(a)):
        if a[i] == b[i]:
            resultat.append(0)
        else:
            resultat.append(1)
    return resultat
