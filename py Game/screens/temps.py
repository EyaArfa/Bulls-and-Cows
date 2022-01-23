import tkinter
from functions import *
class temps:
    def __init__(self, parent,min,sec):
        # variable storing time
        self.canva=parent
        self.seconds =min
        self.minutes=sec
        # label displaying time
        self.label = tkinter.Label(parent, text="{0:2d}:{0:2d}".format(self.minutes,self.seconds), font="Arial 30",bg="#A7DFEE")
        self.label.pack()
        parent.create_window(40,35,anchor="center",window=self.label)
        # start the timer
        self.label.after(1000, self.refresh_label)

    def refresh_label(self):
        """ refresh the content of the label every second """
        # increment the time
        time=self.minutes*60+self.seconds
        if(time==0):
            done("LOST","TIME'S UP")
        print(time)
        time -= 1
        print(time)
        min,sec=divmod(time,60)
        self.seconds=sec
        self.minutes=min
        print(min,sec)
        remaining="{:02d}:{:02d}".format(min,sec)
        # display the new time
        self.label.configure(text=remaining)
        # request tkinter to call self.refresh after 1s (the delay is given in ms)
        self.label.after(1000, self.refresh_label)

      
