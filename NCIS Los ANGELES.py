def liste_eleve(fichier):
    liste = []
    with open(fichier) as file:
        for line in file:
            liste.append(line.strip().split())
    return liste

def nom_matricule(liste):
    dico = {}
    for eleve in liste:
        if len(eleve) <= 4:
            dico[eleve[3] + ' ' + eleve[2]] = int(eleve[1])
        elif eleve[4][0] in '0123456789':
            dico[eleve[3] +' '+ eleve[2]] = int(eleve[1])
        else:
            dico[eleve[4] + ' ' + eleve[2] + ' ' + eleve[3]] = int(eleve[1])
    return dico

def matricule_nom(liste):
    dico = {}
    for eleve in liste:
        if len(eleve) <= 4:
            dico[int(eleve[1])] = eleve[3] + ' ' + eleve[2]
        elif eleve[4][0] in '0123456789':
            dico[int(eleve[1])] = eleve[3] + ' ' + eleve[2]
        else:
            dico[int(eleve[1])] = eleve[4] + ' ' + eleve[2] + ' ' + eleve[3]
    return dico

def trouver_nom(dico, matricule):
    return dico[matricule]

def trouver_matricule(dico, nom):
    return dico[nom]

def points_meca(liste):
    dico = {}
    for eleve in liste:
        dico[int(eleve[1][2:])] = float(eleve[-1])
    return dico

def points_chimie(fichier):
    liste = []
    dico = {}
    with open(fichier) as file:
        for line in file:
            liste.append(line.strip().split())
    for eleve in liste:
        dico[int(eleve[0])] = float(eleve[-1])
    return dico

def points_physique(fichier):
    liste = []
    dico = {}
    with open(fichier) as file:
        for line in file:
            liste.append(line.strip().split())
    for eleve in liste:
        if len(eleve) == 3:
            dico[int(eleve[0])] = float(eleve[-1])
    return dico

def points_analyse(fichier):
    with open(fichier) as file:
        liste = file.read().strip().split()
    i = 0
    dico = {}
    while i+2 < (len(liste)):
        if len(liste[i]) == 9:
            j = i
            while len(liste[j+1]) != 9 and len(liste) > j+3:
                j += 1
            dico[int(liste[i][2:])] = liste[j]
        i = j+1
        j = 0
    for key, value in dico.items():
        if 'N' not in value:
            dico[key] = float(value)
    return dico

def points_eleves(dico_matricule_nom, dico_meca, dico_chimie, dico_physique, dico_analyse):
    dico = {}
    for matricule, eleve in dico_matricule_nom.items():
        dico[eleve] = []
    for matricule in dico_meca:
        if matricule in dico_meca:
            dico[dico_matricule_nom[matricule]].append('méca:  ' + str(dico_meca[matricule]))
    for matricule in dico_physique:
        if matricule in dico_physique and matricule in dico_matricule_nom:
            dico[dico_matricule_nom[matricule]].append('physique:  ' + str(dico_physique[matricule]))
    for matricule in dico_chimie:
        if matricule in dico_chimie and matricule in dico_matricule_nom:
            dico[dico_matricule_nom[matricule]].append('chimie:  ' + str(dico_chimie[matricule]))
    for matricule in dico_analyse:
        if matricule in dico_analyse and matricule in dico_matricule_nom:
            dico[dico_matricule_nom[matricule]].append('analyse:  ' + str(dico_analyse[matricule]))
    for key, value in dico.items():
        n = len(value)
        total = 0
        for i in range(n):
            if 'NDP' not in value[i]:
                total += float(value[i][-5:])
        dico[key].append('moyenne:  ' + str(total/n)[:4])
    return dico

def au_dessus_moyenne(dico):
    liste = []
    for key, value in dico.items():
        moyenne = float(value[-1][-5:])
        if  moyenne >= 10:
            liste.append([key, moyenne])
    return liste

def tout_reussi(dico):
    liste = []
    for key, value in dico.items():
        n = len(value)
        reussi = 0
        for i in range(n-1):
            if 'NDP' not in value[i]:
                if float(value[i][-5:]) >= 10:
                    reussi += 1
        if reussi == 4:
            liste.append([key, value])
    return liste

liste = liste_eleve('méca.txt')
dico_nom_matricule = nom_matricule(liste)
dico_matricule_nom = matricule_nom(liste)
dico_meca = points_meca(liste)
dico_chimie = points_chimie('chimie.txt')
dico_physique = points_physique('physique.txt')
dico_analyse = points_analyse('analyse.txt')
dico_eleve = points_eleves(dico_matricule_nom, dico_meca, dico_chimie, dico_physique, dico_analyse)



#liste des eleves ayant réussi ces 4 cours
#print(tout_reussi(dico_eleve))
#print(len(tout_reussi(dico_eleve)))

#trouver l'élève via le matricule. Entrée : les 6 chiffres du matricules
#print(trouver_nom(dico_matricule_nom,))

#Entrée : 'Prénom NOM'
nom_eleve = 'Alexandre LE MERCIER'

#trouver le matricule d'un élève. Entrée : 'Prénom NOM'
print(trouver_matricule(dico_nom_matricule, nom_eleve ))

#cotes d'un élève. Entrée : 'Prénom NOM'
print('Cotes de', nom_eleve,':', dico_eleve[nom_eleve])



