def conv_bin(n):
    liste = [n % 2]
    n = n // 2

    while n != 0:
        liste.append(n % 2)

        n = n//2

    liste.reverse()

    return (liste, len(liste))


print(conv_bin(5))
