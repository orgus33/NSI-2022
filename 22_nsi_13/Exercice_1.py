def rendu(somme_a_rendre):
    cinq_euros = 0
    deux_euros = 0
    un_euros = 0

    while somme_a_rendre != 0:

        if somme_a_rendre >= 5:
            cinq_euros += 1
            somme_a_rendre -= 5

        elif somme_a_rendre >= 2:
            deux_euros += 1
            somme_a_rendre -= 2

        elif somme_a_rendre == 1:
            un_euros += 1
            somme_a_rendre -= 1

    return [cinq_euros, deux_euros, un_euros]


print(rendu(89))
