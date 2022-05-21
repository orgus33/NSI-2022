def multiplication(n1, n2):
    result = 0
    if n1 < 0:
        n1 = n1 * -1
        for i in range(n1):
            result -= n2
    else:
        for i in range(n1):
            result += n2
    return result


print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))

# ou


def multiplication(a, b):
    produit = 0
    for i in range(abs(a)):
        produit += abs(b)
    if (a > 0 and b < 0) or (a < 0 and b > 0):
        return -produit
    else:
        return produit
