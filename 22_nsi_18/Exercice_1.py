def mini(releve, date):
    mini_moy = releve[0]
    mini_index = None
    for i in range(1, len(releve)):
        if mini_moy > releve[i]:
            mini_moy = releve[i]
            mini_index = i
    return mini_moy, date[mini_index]


t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

print(mini(t_moy, annees))
