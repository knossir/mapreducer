#!/usr/bin/env python

import sys

lst_cle = None
ts_cle = None  
running_total = 0

for input_ligne in sys.stdin:
input_ligne = input_ligne.strip();

ts_cle,valeur = input_ligne.split("\t",1)

valeur=int(valeur)


if lst_cle== ts_cle:
running_total += valeur
else:

if lst_cle:


print( "%s\t%d" % (lst_cle, running_total) )
running_total = valeur
lst_cle = ts_cle

if lst_cle == ts_cle:
print( "%s\t%d" % (lst_cle,running_total))
