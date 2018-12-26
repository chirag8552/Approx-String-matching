# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:37:04 2018

@author: chirag.gokani
"""
from collections import OrderedDict
from ngram_trigram import trigrams
#import os

fl = open("2.000000000002","r")
ls1=[]
for line in fl:
    ls1.append(line.split(' '))
fl.close()

ls2=[]
i=0
j=1
for line in ls1:
    ls2.append(ls1[i][j])
    i=i+1

ls3=list(OrderedDict.fromkeys(ls2))
ls4=[]
i=0
for x in ls3:
    ls4.append(trigrams(ls3[i]))
    i=i+1

