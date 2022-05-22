def renverse(mot):
    inverse_mot = ""

    for l in mot:
        inverse_mot = l + inverse_mot

    return inverse_mot


print(renverse("informatique"))
