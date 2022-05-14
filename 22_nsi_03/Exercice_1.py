def delta(liste):
    encoding = [liste[0]]
    
    for index in range(len(liste)-1):
        encoding.append(liste[index+1] - liste[index])
        
    return encoding


print(delta([42]))
