import matplotlib.pyplot as plt
import numpy as np

def charger(filename, sep=','):
    liste_donnees = []
    with open(filename, 'r', encoding='utf-8') as mon_csvfile:
        les_entetes = mon_csvfile.readline().strip().split(sep)
        for ligne in mon_csvfile:
            d_donnees = {}
            l_donnees = ligne.strip().split(sep)
            for index, donnee in enumerate(l_donnees):
                d_donnees[les_entetes[index]] = donnee
            liste_donnees.append(d_donnees)
    return liste_donnees

def sauvegarder(filename, l_donnees, sep=','):
    with open(filename, 'w', encoding='utf-8') as file_out:
        l_entetes = [str(e) for e in l_donnees[0]]
        entetes = sep.join(l_entetes)
        file_out.write(entetes + '\n')
        for donnees in l_donnees:
            ligne = sep.join([str(donnees[cle]) for cle in l_entetes])
            file_out.write(ligne + '\n')

def affichage(l_donnees):
    x = []
    y1 = []
    y2 = []
    l_entetes = [str(e) for e in l_donnees[0]]
    for donnee in l_donnees :
        lst = [float(donnee[cle]) for cle in l_entetes]
        xi, y1i, y2i = lst[0], lst[1], lst[2]
        x.append(xi)
        y1.append(y1i)
        y2.append(y2i)
    print(len(x))
    print(y2)
    plt.plot(x, y1, label="Mouvement horizontal")
    plt.plot(x, y2, label="Mouvement vertical", linewidth='2')
    plt.legend()
    plt.xlabel("seconds (dépend de la vidéo envoyée mais on trouve ça facile dans les données)")
    plt.ylabel("pixels (osef Debeir ça passe)")
    plt.show() "sexe"

liste = charger("data.csv")
print(liste)
affichage(liste)
