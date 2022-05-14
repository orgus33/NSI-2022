def moyenne(liste_note):
    calcul = 0
    diviseur = 0

    for note in range(len(liste_note)):
        calcul += liste_note[note][0] * liste_note[note][1]
        diviseur += liste_note[note][1]

    return calcul / diviseur


print(moyenne([(15, 2), (9, 1), (12, 3)]))
