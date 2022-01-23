import os
from tkinter import Button, Canvas, Image, PhotoImage
import tkinter
from PIL import Image,ImageTk
import ctypes
master = tkinter.Tk()
user32 = ctypes.windll.user32
width1, height1 = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
def easy(music):
    master.destroy()
    play(music,min=0,sec=0)
def med(music):
    master.destroy()
    play(music,min=2,sec=0)
def hard(music):
    master.destroy()
    play(music,min=1,sec=0)
from game import play

def levels(music):
    width=(width1//3)*2
    height=(height1//3)*2
    x=(width1//2)-(width//2)
    y=height1-height
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (x,y)
    os.environ['SDL_VIDEO_CENTERED'] = '0'
    # creates a Tk() object
    master.resizable(False,False)
    master.geometry('500x500') 
    master.title('vache&taureau')
    # master.iconphoto(False,PhotoImage(file='py Game\images\icon.png'))
    #create canvas
    canva1=Canvas(master,width=width,height=height)
    canva1.pack(fill = "both", expand = True)
    #display image
    # back=PhotoImage(file=r'"C:\Users\EYA\Documents\Ing\FIA1\ParadigmeDeProgrammation\TP\MyPyGame-main\MyPyGame\py Game\images\bulls-and-cows-android.jpg"')
    # canva1.create_image(0,0,image=back, anchor = "nw")
    
    # # Read  Image1
    image1 = (Image.open(r"py Game\images\easy.png"))
    # Resize the image using resize() method
    resize_image = image1.resize((100, 100))
    imgeasy = ImageTk.PhotoImage(resize_image)
    btneasy= Button(master,image=imgeasy,borderwidth=0,command=lambda:easy(music))
    btneasy_window=canva1.create_window(width//10,height//2.5,anchor="center",window=btneasy)

    image2 = (Image.open(r"py Game\images\med.png"))
    # Resize the image using resize() method
    resize_image = image2.resize((100, 100))
    imgmed = ImageTk.PhotoImage(resize_image)
    btnmed= Button(master,image=imgmed,borderwidth=0,command=lambda:med(music))
    btnmed_window=canva1.create_window(width//10+150,height//2.5,anchor="center",window=btnmed)

    image3 = (Image.open(r"py Game\images\hard.png"))
    # Resize the image using resize() method
    resize_image = image3.resize((100, 100))
    imghard = ImageTk.PhotoImage(resize_image)
    btnhard= Button(master,image=imghard,borderwidth=0,command=lambda:hard(music))
    btnhard_window=canva1.create_window(width//10+300,height//2.5,anchor="center",window=btnhard)
    master.mainloop()   
# levels(True)
