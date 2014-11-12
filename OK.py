# coding=utf-8
__author__ = 'Earvin Kayonga'

import os
from random import randrange
from math import ceil


def printable(nb, max=10):
    i = 0
    print 'La table de multiplication de ', nb, 'avec ', max, 'iterations'
    print('Debut de la Table')
    while i < max:
        print i + 1, "*", nb, "=", (i + 1) * nb
        i += 1
    print('Fin de la Table')



def gain(mise, nombre, tirage):#Fonction qui calcule les gains du joueur

    print('Attention, Rien ne va plus!!')
    print "Le Tirage: ", tirage
    i = 0
    while i < 10:
        print('--------------------------------------------')
        i = i + 1


    if tirage == nombre:
        print "Bravo Vous avez gagné ", mise * 3 , " dollars"
        return
    elif Couleur(tirage) == Couleur(mise):
        print "Bravo Vous avez gagné ", mise + (mise * 50/100), " dollars"
        return


    print('Bon, Vous avez perdus')
    print('Revenez nous voir')


def Couleur(a):#Fonction pour déterminer la couleur d'un nombre
    if a% 2 == 0:
        return 1
    else:
        return 0



def Roulette():
    i = 1
    while i != 0:
        try:
            mise = input(' Veuillez miser une somme  ')
        except:
            print('Une somme en dollar est attendu!')
        try: #Gros soucis dans la boucle. A changer
            nombre = input(' Veuillez miser un NOMBRE entre 0 et 49  ')
        except:
            print('Un  nombre entre 0 et 49 est attendu!')
        if nombre > 0:
            if nombre < 49:
                i = i - 1
    # Fin de la Mise
    print('Allez c est parti alors!')
    print('Vous avez misé :')
    print mise, " dollars sur le numero " , nombre


    gain(mise,nombre,randrange(0, 49))





Roulette()
