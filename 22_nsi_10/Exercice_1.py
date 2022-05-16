def occurence_lettres(phrases):
    dic = {}
    for l in phrases:
        if l in dic:
            dic[l] += 1
            
        else:
            dic[l] = 1
            
    return dic


print(occurence_lettres("Hello world!"))
