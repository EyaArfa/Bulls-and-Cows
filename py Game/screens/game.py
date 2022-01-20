# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 21:29:59 2022

@author: EYA
"""
from random  import randint
def count(ch,x):
    if(ch==x):
        return (4,0)
    else:
        nt=0
        nv=0
        for i in x:
            if (i in ch) :
                pos=ch.index(i)
                if(pos==x.index(i)):
                    nt+=1
                else:
                    nv+=1
        return(nt,nv)

cs=randint(1000, 9999)
x=str(input("i'm thinking of 4 digit number guess it"))
ch=str(cs)
essai=1
while(essai<6):
        if(count(ch,x)==(4,0)):
           print("you won!") 
           break
        else:
           l=count(ch,x)
           print('{}T,{}V'.format(l[0], l[1]))
           x=str(input("try again "))
           essai+=1
print(cs)

        


