#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:12:37 2020

@author: axel.nael
"""
from trilistemot import listemot
from fctPendu import pendu
from random import randint
score=open('ScorePendu','a')
scorer=open('ScorePendu','r')
scorestr=scorer.read()
listescore=scorestr.split('\n')
highscore=0
for i in range (0,len(listescore)-1):
    if int(listescore[i][0])>=highscore:
        highscore=int(listescore[i][0])
limot=listemot()
cont=1

while cont==1:
    valeurmot=randint(0,len(limot))
    vie,mot=pendu(limot[valeurmot])
    ligne=str(vie)+","+str(mot)+"\n"
    score.write(str(ligne))
    if vie<highscore:
        print("vous n'avez pas battu votre record.")
        print "votre record est de",highscore,"vies."
    elif vie==highscore:
        print ("Vous avez égalé votre record!")
    elif vie>highscore:
        print ("Félicitation! Vous avez battu votre record personnel!!!")
    cont=int(input("Voulez vous rejouer? 1=Oui 0=Non"))
    while cont!=1 and cont!=0:
        print "Erreur, merci de ne retrer que 1 ou 0"
        cont=int(input("Voulez vous rejouer? 1=Oui 0=Non"))
score.close
score=open('ScorePendu','a')
score.close
scorer.close