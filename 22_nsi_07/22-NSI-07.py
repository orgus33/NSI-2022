def tri_bulles(T):
    n = len(T)
    for i in range(len(T)-1, 0, -1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T


print(tri_bulles([3, 8, 1, 7, 6, 4, 9, 0]))
