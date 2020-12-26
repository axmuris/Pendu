#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:01:23 2020

@author: axel.nael
"""
def pendu(dmot):
    abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Lmot=list(dmot.strip())
    life=8
    answer=[]
    print "La première lettre du mot vous est donné:" 
    listeprop=[Lmot[0],]
    for i in range (0,len(Lmot)):
        answer.append("_")
    for i in range (0,len(Lmot)):
                if (Lmot[i]==Lmot[0]):
                    answer[i]=Lmot[0]
    print "Mot:",answer[:]
    while (life!=0) and (('_' in answer)==True ):
        print "Lettres déjà testées:",listeprop[:]
        print("Quelle lettre voulez vous essayer?")
        proposition = raw_input("Lettre :")
        while (proposition in listeprop)==True:
            print ("Vous avez déjà essayer cette lettre, merci d'en rentrer une autre.")
            print "Lettres déjà testées:",listeprop[:]
            proposition=raw_input("Lettre:")
        while ((proposition in abc) == False):
            print ("Erreur, merci de rentrer une unique lettre valide (le jeu n'accepte pas les caractère spéciaux et les accents.)")
            proposition=raw_input("Lettre:")
        if proposition in Lmot:
            for i in range (0,len(Lmot)):
                if (Lmot[i]==proposition):
                    answer[i]=proposition
            print("Bravo, vous avez trouvez une lettre")
        else:
            print"Malheureusement la lettre",proposition[:],"n'est pas dans le mot, vous perdez une vie."
            life=life-1
        listeprop.append(proposition)
        print "Mot:",answer[:]
        print "Vie restantes:", life
        
    if life==0:
       print ("Vous n'avez plus de vies, vous avez perdu.")
       print "le mot que vous cherchiez était", dmot,"."
    else:
       print "Félicitation, vous avez trouvé le mot",dmot,"."
       print "Il vous restait",life, "vies."
    return(life,dmot)

