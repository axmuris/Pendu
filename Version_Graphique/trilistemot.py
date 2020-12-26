#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:29:19 2020

@author: axel.nael
"""
from random import randint

def listemot():
    fich=open ('ListemotPendu','r')
    liste=fich.read()
    liste=list(liste.split(','))
    liste[-1]=liste[-1][0:-1]
    listef=sorted(liste,key=len)
    mot=listef[randint(0,len(listef)-1)]
    return(mot)

