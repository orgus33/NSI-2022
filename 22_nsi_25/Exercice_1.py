def selection_enclos(table_animaux, num_enclos):
    table = []
    for i in range(len(table_animaux)):
        if table_animaux[i]['enclos'] == num_enclos:
            table.append(table_animaux[i])
    return table

animaux = [ {'nom':'Medor',  'espece':'chien', 'age':5, 'enclos':2}, 
            {'nom':'Titine', 'espece':'chat',  'age':2, 'enclos':5}, 
            {'nom':'Tom',    'espece':'chat',  'age':7, 'enclos':4}, 
            {'nom':'Belle',  'espece':'chien', 'age':6, 'enclos':3}, 
            {'nom':'Mirza',  'espece':'chat',  'age':6, 'enclos':5}]

print(selection_enclos(animaux, 7))