def recherche(a, t):
    counter = 0
    for i in range(len(t)):
        if t[i] == a:
            counter += 1
    return counter


print(recherche(5, [-2, 3, 4, 8]))

print(recherche(5, [-2, 3, 1, 5, 3, 7, 4]))

print(recherche(5, [-2, 5, 3, 5, 4, 5]))
