from tkinter import messagebox
import levels

def done(root,title,msg):
    response=messagebox.askquestion(title,msg)
    print(response)
    if response==messagebox.YES:
        root.destroy()
        levels() 
    else:
        root.destroy()