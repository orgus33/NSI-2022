def moyenne(tab):
    ''' 
        moyenne(list) -> float 
        Entrée : un tableau non vide d'entiers 
        Sortie : nombre de type float  
        Correspondant à la moyenne des valeurs présentes dans le 
        tableau 
    '''
    total = 0
    for n in tab:
        total += n
    if len(tab) > 1:
        return total / len(tab)
    else:
        return total
    


assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5
