# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:32:39 2018

@author: chirag.gokani
"""

def trigrams(var):
    ls = []
    leng = len(var)
    for x in range(leng):
        wrd=var[x:x+3]
        if len(wrd) < 3:
            break
        ls.append(wrd)
    return ls


def rev_trigrams(lst1):
    ls=[]
    i=1
    if len(lst1) > 3:
        for x in lst1:
            ls.append(lst1[i][2])
            i=i+1
            if i==len(lst1):
                break
        p=str(lst1[0])
        q=''.join(ls)
        r=p+q
        return r
    else:
        return str(lst1[0])