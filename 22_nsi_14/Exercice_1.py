def correspond(mot, mot_a_trous):

    for i in range(len(mot)-1):
        if mot_a_trous[i] != mot[i] and mot_a_trous[i] != "*":
            return False

    return True


print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))
