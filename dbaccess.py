# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:44:00 2018

@author: chirag.gokani
"""
from ngram_trigram import trigrams
import cx_Oracle
import time
start1=time.time()
start=time.time()
try: 
    con = cx_Oracle.connect('chiragdb_814/banana12@158.234.207.63:1521/hot11perf')
    print(con.version)
    curs = con.cursor()
    end=time.time()
    start3=time.time()
    print("Database Connection time : "+ str(end-start))
    curs.execute('select SDN_NAME from HS_SDN_APP')
#    fl=open("data","w")
    ls4=[]
    ls3=[]
    for a in curs:
        p=str(a[0]).lower()
        ls3.append(str(a[0]))
        q=trigrams(p)
        ls4.append(q)
    end3=time.time()
    print("database to list : "+ str(end3-start3))
#        fl.write(str(q)+"\n")
    start2=time.time()
#    con.close
#    fl.close()
except Exception as e:
    print(e)
    
    

#fh=open("data","r")
#
#for x in fh:
#    ls.append(x)
    
#fl1=open("data1","w")
#
#for x in ls3:
##    p=trigrams(x)
##    ls4.append(p)
#    fl1.write(str(x)+"\n")
#fl1.close()


