def nombre_de_mots(phrase):
    counter = 0
    for c in phrase:
        if c == " ":
            counter += 1

    if phrase[-1] == ".":
        counter += 1
    return counter


print(nombre_de_mots('Il y a un seul espace entre les mots.'))
