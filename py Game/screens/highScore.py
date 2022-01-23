
import tkinter
def high():
    f = open(r"py Game\cache\score.txt")
    l=f.readlines()
    # creates a Tk() object
    master = tkinter.Tk()
    # master.eval('tk::PlaceWindow %s center' % master.winfo_pathname(master.winfo_id()))
    master.geometry("300x200")
    master.title('Highest scores')
    label = tkinter.Label(master,
            text ='Players:')
    label.pack(pady = 10)
    for line in l:
        label = tkinter.Label(master,
        text =line.rstrip("\n"))
        label.pack(pady = 0)

    btn = tkinter.Button(master,
    text ="Return",
        command = master.destroy)
    btn.pack(pady = 10)

    master.mainloop()
    f.close()
