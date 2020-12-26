# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:09:13 2020

@author: axeln
"""

from trilistemot import listemot

def cararep (mot):
    mot.strip()
    rep=[]
    for i in range (0,len(mot)):
        rep.append("_")
    let=mot[0]
    for i in range (0,len(mot)):
          if mot[i]==let:
               rep[i]=let
    return rep,let
    



class mot:
    def __init__(self):
        self.mot=listemot()
        self.motst=self.mot.strip()
        self.reponse,self.premlettre=cararep(self.mot)

    def mproposer(self,lettre):
        for i in range (0,len(self.reponse)):
            if self.motst[i] == lettre:
                self.reponse[i]=lettre
                