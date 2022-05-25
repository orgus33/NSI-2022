def trouver_intrus(tab, g, d):
    '''
    Renvoie la valeur de l'intrus situé entre les indices g et d 
    dans la liste tab où 
	tab vérifie les conditions de l'exercice,
    	g et d sont des multiples de 3.
    '''
    if g == d:
        return tab[g]
    
    else:
        nombre_de_triplets = (d - g)// 3
        indice = g + 3 * (nombre_de_triplets // 2)
        
        if tab[indice] != tab[indice + 1]:
            return trouver_intrus(tab, g, indice)
        else:
            return trouver_intrus(tab, indice+3, d)

print(trouver_intrus([3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 
8, 5, 5, 5], 0, 21))