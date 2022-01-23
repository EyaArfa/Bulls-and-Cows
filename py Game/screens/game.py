# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 21:29:59 2022

@author: EYA
"""
from asyncio import create_task
from operator import truediv
from pydoc import describe
from random  import randint
from tkinter import ANCHOR, CENTER, Button, Canvas, Frame, Grid, Label, PhotoImage, messagebox
from window import window
import pygame
import sys
import tkinter.font
from PIL import Image,ImageTk
number=""
trial=0
cs=randint(1000, 9999)
ch=str(cs)
print(ch)
# ch=''
def error():
    messagebox.showerror("error","ENTER 4 DIGIT NUMBER")
def add(value,answer,canva1):
    global number
    if(len(number)<4):
        number+=value
        canva1.itemconfig(answer,text=number)
    print(number)
def clear(answer,canva1):
    global number
    number=number[0:len(number)-1] 
    canva1.itemconfig(answer,text=number) 
    print(number) 

def bullandcow():
    
    #create object
    root=tkinter.Tk()
    #define a title for the window
    root.title('vache&taureau')
    #adjust size
    root.geometry('500x500')
    #disable window resizing
    root.resizable(False,False)
    #define image as icon for the window
    root.iconphoto(False,PhotoImage(file='py Game\images\icon.png'))
    #create canvas
    canva1=Canvas(root,width=500,height=500)
    canva1.pack(fill = "both", expand = True)
    #display image
    bg=PhotoImage(file='py Game\images\Sans titre.png')
    canva1.create_image( 0, 0, image = bg, anchor = "nw")
    
    
    
    # # Create an object of type Font from tkinter.
    Desired_font = tkinter.font.Font( family = "Comic Sans MS", 
                                size = 50, 
                                 weight = "bold")
    answer=canva1.create_text(260,140,text='',font=Desired_font,fill="#F1E755")
    # # Read  Image1
    image1 = (Image.open(r"py Game\images\num1.png"))
    # Resize the image using resize() method
    resize_image = image1.resize((50, 50))
    img_btn1 = ImageTk.PhotoImage(resize_image)
    btn1= Button(root,image=img_btn1,borderwidth=0,command=lambda:add("1",answer,canva1))
    btn1_window=canva1.create_window(200,200,anchor="center",window=btn1)

    # #btn1.grid(row=1,column=0,padx=3,pady=5)
    
    # Read  Image2
    image2 = (Image.open(r"py Game\images\num2.png"))
    # Resize the image using resize() method
    resize_image = image2.resize((50, 50))
    img_btn2 = ImageTk.PhotoImage(resize_image)
    btn2= Button(canva1,image=img_btn2,borderwidth=0,command=lambda:add("2",answer,canva1))
    btn2_window=canva1.create_window(260,200,anchor="center",window=btn2)

    
    # Read  Image3
    image3 = (Image.open(r"py Game\images\num3.png"))
    # Resize the image using resize() method
    resize_image = image3.resize((50, 50))
    img_btn3 = ImageTk.PhotoImage(resize_image)
    btn3= Button(canva1,image=img_btn3,borderwidth=0,command=lambda:add("3",answer,canva1))
    btn3_window=canva1.create_window(320,200,anchor="center",window=btn3)
   

    # Read  Image4
    image4 = (Image.open(r"py Game\images\num4.png"))
    # Resize the image using resize() method
    resize_image = image4.resize((50, 50))
    img_btn4 = ImageTk.PhotoImage(resize_image)
    btn4= Button(canva1,image=img_btn4,borderwidth=0,command=lambda:add("4",answer,canva1))
    btn1_window=canva1.create_window(200,260,anchor="center",window=btn4)
    

     # Read  Image5
    image5 = (Image.open(r"py Game\images\num5.png"))
    # Resize the image using resize() method
    resize_image = image5.resize((50, 50))
    img_btn5 = ImageTk.PhotoImage(resize_image)
    btn5= Button(canva1,image=img_btn5,borderwidth=0,command=lambda:add("5",answer,canva1))
    btn5_window=canva1.create_window(260,260,anchor="center",window=btn5)


    #  # Read  Image6
    image6 = (Image.open(r"py Game\images\num6.png"))
    # Resize the image using resize() method
    resize_image = image6.resize((50, 50))
    img_btn6 = ImageTk.PhotoImage(resize_image)
    btn6= Button(canva1,image=img_btn6,borderwidth=0,command=lambda:add("6",answer,canva1))
    btn6_window=canva1.create_window(320,260,anchor="center",window=btn6)
   

     # Read  Image7
    image7 = (Image.open(r"py Game\images\num7.png"))
    # Resize the image using resize() method
    resize_image = image7.resize((50, 50))
    img_btn7 = ImageTk.PhotoImage(resize_image)
    btn7= Button(canva1,image=img_btn7,borderwidth=0,command=lambda:add("7",answer,canva1))
    btn7_window=canva1.create_window(200,320,anchor="center",window=btn7)
    #  # Read  Image8
    image8 = (Image.open(r"py Game\images\num8.png"))
    # Resize the image using resize() method
    resize_image = image8.resize((50, 50))
    img_btn8 = ImageTk.PhotoImage(resize_image)
    btn8= Button(canva1,image=img_btn8,borderwidth=0,command=lambda:add("8",answer,canva1))
    btn8_window=canva1.create_window(260,320,anchor="center",window=btn8)
    #  # Read  Image9
    image9 = (Image.open(r"py Game\images\num9.png"))
    # Resize the image using resize() method
    resize_image = image9.resize((50, 50))
    img_btn9 = ImageTk.PhotoImage(resize_image)
    btn9= Button(canva1,image=img_btn9,borderwidth=0,command=lambda:add("9",answer,canva1))
    btn9_window=canva1.create_window(320,320,anchor="center",window=btn9)
    # btn9.grid(row=3,column=2,padx=3,pady=5)
    #  # Read  delete image
    imagedel = (Image.open(r"py Game\images\0.png"))
    # Resize the image using resize() method
    resize_image = imagedel.resize((50, 50))
    img_btn0 = ImageTk.PhotoImage(resize_image)
    btn0= Button(canva1,image=img_btn0,borderwidth=0,command=lambda:add("0",answer,canva1))
    btn0_window=canva1.create_window(200,380,anchor="center",window=btn0)
    #  # Read  delete image
    imagedel = (Image.open(r"py Game\images\del.png"))
    # Resize the image using resize() method
    resize_image = imagedel.resize((50, 50))
    img_btndel = ImageTk.PhotoImage(resize_image)
    btndel= Button(canva1,image=img_btndel,borderwidth=0,command=lambda:clear(answer,canva1))
    btndel_window=canva1.create_window(260,380,anchor="center",window=btndel)
    custom=tkinter.font.Font( family = "Comic Sans MS", 
                                size = 20, 
                                 weight = "bold")
    nc=canva1.create_text(300,30,text='',font=custom,fill="white")
    nb=canva1.create_text(230,30,text='',font=custom,fill="white")
    # # Read  check image
    imagecheck = (Image.open(r"py Game\images\check.png"))
    # Resize the image using resize() method
    resize_image = imagecheck.resize((50, 50))
    img_btncheck = ImageTk.PhotoImage(resize_image)
    btncheck= Button(canva1,image=img_btncheck,borderwidth=0,command=lambda:count(ch,number,canva1,nc,nb,answer) if(len(number)==4)else error() )
    btncheck_window=canva1.create_window(320,380,anchor="center",window=btncheck)
    
        


    root.mainloop()
def play():
    global ch
    cs=randint(1000, 9999)
    ch=str(cs)
    essai=5
    bullandcow()
def show_result(nt,nv,canva,nc,nb):
    
    bull=PhotoImage(file=r'py Game\images\bull.png')
    widgetbull= Label(canva, image=bull)
    widgetbull.image=bull
    widgetbull.pack()
    canva.create_window(200, 30, window=widgetbull)
    


    cow=PhotoImage(file='py Game\images\cow-icon-hi.png')
    widgetcow = Label(canva, image=cow)
    widgetcow.image=cow
    widgetcow.pack()
    canva.create_window(270, 30, window=widgetcow)
    canva.itemconfig(nc,text=str(nv))
    canva.itemconfig(nb,text=str(nt))





   


    
def count(ch,x,canva,nc,nb,answer):
    global number
    global trial
    trial+=1
    if(ch==x):
        show_result(4,0,canva,nc,nb)             
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
        show_result(nt,nv,canva,nc,nb)
        number=''
        canva.itemconfig(answer,text=number)

        print(nt,nv)
bullandcow()
""" 
while(essai<6):
        if(count(ch,x)==(4,0)):
           print("you won!") 
           break
        else:
           l=count(ch,x)
           print('{}T,{}V'.format(l[0], l[1]))
           x=str(input("try again "))
           essai+=1 """

        


