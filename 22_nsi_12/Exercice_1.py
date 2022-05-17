def moyenne(tab):

    moyenne = 0

    if tab == []:
        return "erreur"
    else:
        for el in tab:
            moyenne += el

    return moyenne/len(tab)


print(moyenne([]))
