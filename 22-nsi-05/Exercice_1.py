def rechercheMinMax(tab):
    if tab == []:
        dico = {"min": None, "max": None}
    else:
        dico = {"min": tab[0], "max": tab[0]}
        for i in range(len(tab) - 1):
            if tab[i] < dico["min"]:
                dico["min"] = tab[i]
            elif tab[i] > dico["max"]:
                dico["max"] = tab[i]
    return dico


print(rechercheMinMax([]))
