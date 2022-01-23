import tkinter


def high():
    f = open(r"py Game\cache\score.txt")
    l=f.readlines()
    # creates a Tk() object
    master = tkinter.Tk()
    master.mainloop()
high()