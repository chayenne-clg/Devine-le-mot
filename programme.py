import random

#Liste de mots à deviner
liste_mots = ['ordinateur', 'python', 'code', 'binaire', 'jeux','lentille','fonction','boucle','variable']

#Séléction aléatoire d'un mot
mot = random.choice(liste_mots)

#Cache les lettres du mot pour avoir quelque chose de la forme _ _ _ _ _
mot_devine = ['_'] * len(mot)

#On a droit à 10 tentatives pour deviner le mot
tentatives = 10

#Tant qu'in reste des tentatives, le jeu continue
while tentatives > 0:
    print('\nMot actuel : ' + ' '.join(mot_devine))
    lettre = input('Propose une lettre : ').lower()

#Si la lettre choisie est dans le mot on la remplace dans le mot à deviné
    if lettre in mot:
        for i in range(len(mot)):
            if mot[i] == lettre:
                mot_devine[i] = lettre
        print('Bonne réponse !')

#Sinon on perd une tentative
    else:
        tentatives -= 1
        print('Mauvaise réponse ! Tentatives restantes : ' + str(tentatives))

#S'il ne reste plus de lettres masquées alors la partie est gagnée
    if '_' not in mot_devine:
        print('\nBravo ! Tu as trouvé le mot : ' + mot)
        break

#S'il ne reste plus de tentatives et s'il reste des lettres masquées la partie esr perdue
    if tentatives == 0 and '_' in mot_devine:
        print('\nTu n’as plus de tentatives ! Le mot était : ' + mot)
