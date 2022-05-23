def max_dico(dico):
    max = 0
    for value in dico:
        if dico[value] > max:
            max = dico[value]
            name = value
    return (name, max)


print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))
