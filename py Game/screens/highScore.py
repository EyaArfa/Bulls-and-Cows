

from tkinter import *
from tkinter.ttk import *
def high():
    f = open("py Game\cache\score.txt")
    l=f.readlines()
    # creates a Tk() object
    master = Tk()
    master.eval('tk::PlaceWindow %s center' % master.winfo_pathname(master.winfo_id()))
    master.geometry("300x200")
    master.title('Highest scores')
    label = Label(master,
            text ='Players:')
    label.pack(pady = 10)
    for line in l:
        label = Label(master,
        text =line.rstrip("\n"))
        label.pack(pady = 0)

    btn = Button(master,
    text ="Return",
        command = master.destroy)
    btn.pack(pady = 10)

    mainloop()
    f.close()