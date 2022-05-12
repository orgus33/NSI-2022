def pascal(n):

    C = [[1]]

    for k in range(1, n+1):

        Ck = [1]

        for i in range(1, k):
            print("k = ", k, "i = ", i)
            Ck.append(C[len(C)-1][i-1] + C[len(C)-1][i])

        Ck.append(1)

        C.append(Ck)
    return C

# C : tableau abec la liste des nombres du triangles
# n >= 0 :
# Ck : contient la k-ième ligne du tableau


print(pascal(5))
