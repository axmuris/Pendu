# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:13:13 2020

@author: axeln
"""


from classeFenetre import fenetre
from classemot import mot
from classeprops import propos


class jeux:
    def __init__(self):
        self.disp=fenetre(self)
        self.listeprop=propos()
        
    def insertcoin(self):
        self.mot=mot()
        self.listeprop.listepro=[]
        self.listeprop.listepro.append(self.mot.premlettre)
        self.vies =7
        self.disp.vie.set("Vies restantes:" + str(self.vies))
        self.disp.bonhomme['file']='bonhomme1.gif'
        self.disp.liste.set("Lettres déjà proposées:" + str(self.listeprop.listepro))
        self.disp.lettre.set("")
        self.disp.label.set("Bonjour et bienvenue à ce jeux du Pendu. Veuillez entrer une lettre et appuyer sur \"proposer\" pour commencer.")
        self.disp.reponse.set(self.mot.reponse)
        self.disp.activationpropose()
        self.disp.affiche()
    
    def proposer(self,lettre):
        if self.disp.lettre.get() =="":
            self.disp.label.set("Vous n'avez pas entré de lettre, merci d'entrer une lettre minuscule.")
        elif self.disp.lettre.get() in self.listeprop.listepro:
            self.disp.label.set("Vous avez déjà entré cette lettre, merci d'en entrer une autre.")
        elif (self.disp.lettre.get() in self.mot.motst) and (self.disp.lettre.get not in self.listeprop.listepro):    
            self.listeprop.ajout(lettre)
            self.mot.mproposer(lettre)
            self.disp.reponse.set(self.mot.reponse)
            self.disp.label.set("Bravo, vous avez trouvé une lettre!")
            if "_" not in self.mot.reponse:
                self.disp.activationpropose()
                self.disp.label.set("Bravo, vous vez trouvé le mot. \n Il vous restait "+str(self.vies)+" vies. \n Voulez-vous rejouer?")
        elif self.disp.lettre.get() not in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
            self.disp.label.set("La proposition n'est paas acceptée, merci de ne rentrer qu'une lettre seule en minuscule (les accents ne sont pas autorisés).")
        else:
            self.disp.label.set("Malheureusement cette lettre ne faisait pas partit du mot, vous perdez donc une vie...")
            self.vies=self.vies-1
            self.disp.bohnommechgt(self.vies)
            self.disp.vie.set("Vies restantes:" + str(self.vies))
            self.listeprop.ajout(lettre)
            if self.vies == 0:
                self.disp.label.set("Vous n'avez plus de vie, malheureusement vous avez perdu.\n Le mot était "+self.mot.mot+".\n Voulez vous rejouer?")
                self.disp.activationpropose()
        self.disp.liste.set("Lettres déjà proposées:" + str(self.listeprop.listepro))
        self.disp.lettre.set("")
    
        
        
game=jeux()
game.insertcoin()
