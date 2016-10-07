#!/usr/bin/env python 

import sys

for ligne in sys.stdin: 
ligne = ligne.strip()

cles = ligne.split()

for cle in cles:

valeur = 1

print( "%s\t%d" % (cle,valeur) )
