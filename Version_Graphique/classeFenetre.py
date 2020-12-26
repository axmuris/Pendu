# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:50:44 2020

@author: axeln
"""
from tkinter import Tk, Label, Canvas, PhotoImage, Button, Entry, StringVar, NORMAL,DISABLED

class fenetre():
    def __init__(self,jeux):
        self.fen=Tk()
        self.can=Canvas(self.fen,height=500,width=1000,backgroun='lightgreen')
        self.label=StringVar()
        self.instruc=Label(self.fen, textvariable=self.label)
        self.reponse=StringVar()
        self.rep=Label(self.fen,textvariable=self.reponse)
        self.lettre=StringVar()
        self.prop=Entry(self.fen, textvariable=self.lettre) 
        self.liste= StringVar()
        self.listeprop=Label(self.fen, textvariable=self.liste)
        self.propose=Button(self.fen, text="proposer", state=DISABLED, command = lambda:jeux.proposer(self.lettre.get()))
        self.rejouer=Button(self.fen, text="rejouer", command=lambda:jeux.insertcoin())
        self.fen.bind('<Return>',lambda x:jeux.proposer(self.lettre.get()))
        self.can2=Canvas(self.fen,height=350,width=300)
        self.bonhomme=PhotoImage(master=self.fen, file='bonhomme1.gif')
        self.image=self.can2.create_image(150,150,image = self.bonhomme)

        
        self.quit=Button(self.fen,text="Quitter",command = self.fen.destroy)
        self.vie=StringVar()
        self.live=Label(self.fen, textvariable=self.vie)

    def affiche(self):
        self.fen.title("Pendu")
        
        self.can.grid(row = 1, column = 1, rowspan= 6, columnspan=2)
        self.rep.grid(row = 1, column = 1)
        self.prop.grid(row = 2, column = 1) 
        self.propose.grid(row = 3, column = 1)
        self.instruc.grid(row = 4 , column = 1)
        self.listeprop.grid(row = 5, column = 1)
        
        self.live.grid(row = 1, column = 2)
        self.can2.grid(row = 2, column = 2, rowspan = 2)
        self.rejouer.grid(row = 5 , column = 2)
        self.quit.grid(row = 6, column = 2)
        self.fen.mainloop()

    def activationpropose(self):
        if (self.propose['state'] == NORMAL):
            self.propose['state'] = DISABLED
        else:
            self.propose['state'] = NORMAL

    def bohnommechgt(self,vie):
        if vie==7:
            self.bonhomme['file']='bonhomme1.gif'
        elif vie==6:
            self.bonhomme['file']='bonhomme2.gif'
        elif vie==5:
            self.bonhomme['file']='bonhomme3.gif'
        elif vie==4:
            self.bonhomme['file']='bonhomme4.gif'
        elif vie==3:
            self.bonhomme['file']='bonhomme5.gif'
        elif vie==2:
            self.bonhomme['file']='bonhomme6.gif'
        elif vie==1:
            self.bonhomme['file']='bonhomme7.gif'
        elif vie==0:
            self.bonhomme['file']='bonhomme8.gif'

        
        

