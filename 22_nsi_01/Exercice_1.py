def recherche(caractere, mot):
    counter = 0
    for lettre in mot:
        if lettre == caractere:
            counter += 1
    return counter


print(recherche('a', "mississippi"))
