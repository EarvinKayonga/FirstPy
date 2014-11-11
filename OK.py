__author__ = 'Earvin'

import os
from random import randrange
from math import ceil

def printable(nb, max = 10):
    i = 0
    print 'La table de multiplication de ', nb, 'avec ', max , 'iterations'
    print('Debut de la Table')
    while i < max:
         print i + 1, "*", nb, "=", (i + 1) * nb
         i += 1
    print('Fin de la Table')

printable(7)
