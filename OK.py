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


# printable(7)


def inputmise():
    i = 1
    while i != 0:
        try:
            mise = input(' Veuillez miser une somme  ')
        except:
            print('Une somme en dollar est attendu!')
        try:
            nombre = input(' Veuillez miser un NOMBRE entre 0 et 49  ')
        except:
            print('Un  nombre entre 0 et 49 est attendu!')
        if nombre > 0:
            if nombre < 49:
                i = i - 1

    print('Allez c est parti alors!')
    print('Vous avez misé :')
    print mise, " dollars sur le numero " , nombre





inputmise()