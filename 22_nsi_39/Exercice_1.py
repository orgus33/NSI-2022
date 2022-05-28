def moyenne(liste):
    total = 0
    for number in liste:
        total += number
    return total / len(liste)


print(moyenne([10, 20, 30, 40, 60, 110]))
