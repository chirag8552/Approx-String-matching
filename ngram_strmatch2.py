# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:41:31 2018

@author: chirag.gokani
"""

from ngram_trigram import trigrams
from ngram_trigram import rev_trigrams
from dbaccess import ls4,ls3,start1,start2
#from ngram_fileread import ls4
#from ngramtemp import dict1
import sys
from collections import OrderedDict
import time

def loop_cnt(num,per):
    number=(per*(num))/100
    approx=int(round(number))
    return approx

def percen(num1,num2):
    percn=int((num1/num2)*100)
    return percn

inp1=(sys.argv[1:])
inp2=' '.join(str(x) for x in inp1).lower()
print(inp2)
inp=trigrams(inp2)
per=80
#inp=trigrams('PATH')
#per=int(50)
l_inp=len(inp)
print(inp)
print(l_inp)
print(loop_cnt(l_inp,per))
cnt_loop=loop_cnt(l_inp,per)
end2=time.time()
print("Switch : " + str(end2-start2))
print("===================================================")
start=time.time()
ls5=[]
ls7=[]

i=0
for x in ls4:
    cnt=0
    for y in ls4[i]:
        for a in inp:
            if y==a:
                cnt=cnt+1
#                print(cnt)
            if cnt >= cnt_loop:
#                print(str(x) + "     " +str(cnt))
                ls5.append(x)
                ls7.append(i)
                cnt=0
                break
    i=i+1
    
#calculate percentage    
print("===================================================")
dict1=dict()
i=0
abc=0
for x in ls5:
    cnt=0
    j=0
    q=ls3[ls7[i]]
    for y in ls5[i]:
        for a in inp:
            if y==a:
                cnt=cnt+1
            if cnt >=cnt_loop and cnt <= l_inp:
                p=rev_trigrams(ls5[i])
#                ls6.append(p)
                dict1[q] = cnt
#                print(str(p)+"     " +str(cnt)+"     " +str(j))
        j=j+1
    i=i+1
    abc=abc+1

i=0
for x in dict1.values():
#    print(x)
    q=percen(x,l_inp)
    p=list(dict1.keys())[list(dict1.values()).index(x)]
    dict1[p]=q
    i=i+1
i=1
for x in dict1.items():
    print(str(i)+" --- > "+str(x))
    i=i+1
print("===================================================")

end=time.time()
end1=time.time()
print("String Matching time : " + str(end-start))
print("Exec code time : " + str(end1-start1))