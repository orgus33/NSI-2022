def verifie(tab):
    number = tab[0]
    for n in tab:
        if n < number:
            return False
    return True


print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([5]))
