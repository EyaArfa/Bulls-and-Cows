import tkinter
from PIL import Image,ImageTk
from pygame import mixer
from game import play
def easy(music,levelwin):
    levelwin.destroy()
    play(music,min=0,sec=0)
def med(music,levelwin):
    levelwin.destroy()
    play(music,min=2,sec=0)
def hard(music,levelwin):
    levelwin.destroy()
    play(music,min=1,sec=0)
def levels(music):
    root=tkinter.Tk()
    if(music):
        mixer.init()
        mixer.music.load('py Game\music\\bensound-summer_mp3_music.mp3')
        mixer.music.play()
    root.geometry('500x500') 
    root.title('vache&taureau')

    root.iconphoto(False,tkinter.PhotoImage(file='py Game\images\icon.png'))
    #create canvas
    canva1=tkinter.Canvas(width=500,height=500)
    canva1.pack(fill = "both", expand = True)
    #display image
    back=tkinter.PhotoImage(master=canva1,file=r'py Game\images\Sans titre.png')
    canva1.create_image(0,0,image=back, anchor = "nw")
    
     # # Read  Image1
    image1 = (Image.open(r'py Game\images\easy.png'))
    # Resize the image using resize() method
    resize_image = image1.resize((100, 100))
    imgeasy=ImageTk.PhotoImage(resize_image)
    btneasy= tkinter.Button(canva1,image=imgeasy,borderwidth=0,command=lambda:easy(music,root))
    btneasy_window=canva1.create_window(100,250,anchor="center",window=btneasy)

    image2 = (Image.open(r'py Game\images\med.png'))
    # Resize the image using resize() method
    resize_image = image2.resize((100, 100))
    imgmed = ImageTk.PhotoImage(resize_image)
    btnmed= tkinter.Button(canva1,image=imgmed,borderwidth=0,command=lambda:med(music,root))
    btnmed_window=canva1.create_window(250,250,anchor="center",window=btnmed)

    image3 = (Image.open(r'py Game\images\hard.png'))
    # Resize the image using resize() method
    resize_image = image3.resize((100, 100))
    imghard = ImageTk.PhotoImage(resize_image)
    btnhard= tkinter.Button(canva1,image=imghard,borderwidth=0,command=lambda:hard(music,root))
    btnhard_window=canva1.create_window(400,250,anchor="center",window=btnhard)


    root.mainloop()
# levels(False)