def moyenne(tab):
    total = 0

    for number in tab:
        total += number
    return total / len(tab)


print(moyenne([1.0, 2.0, 4.0]))
