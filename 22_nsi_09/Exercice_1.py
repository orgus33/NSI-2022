def calcul(n):
    liste = [n]

    while n != 1:
        if liste[-1] % 2 == 0:
            n = n//2
            liste.append(n)
        else:
            n = (3*n) + 1
            liste.append(n)

    return liste


print(calcul(7))
