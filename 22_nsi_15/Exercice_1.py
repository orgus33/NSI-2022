def nb_repetitions(elt, tab):
    counter = 0
    for el in tab:
        if el == elt:
            counter += 1
    return counter


print(nb_repetitions(12, [1, '! ', 7, 21, 36, 44]))
