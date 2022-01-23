# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
def about():
    # creates a Tk() object
    master = Tk()
    master.eval('tk::PlaceWindow %s center' % master.winfo_pathname(master.winfo_id()))
    master.geometry("450x250")
    master.title('How to play?')
    label = Label(master,
        text ="*A player will create a secret code, usually a 4-digit number.\nThis number must not have any repeated digits.\n*Another player makes a guess (4 digit number) to decipher the secret number.\nAfter making a guess, 2 clues will be provided: the cows and the bulls.\n*The bulls indicate the number of correct digits in the right position\nand the cows indicate the number of correct digits in the wrong position.\nFor example, if the secret code is 1234 and the guessed number is 1246 then we have\n2 BULLS(for the correct matches of numbers 1 and 2) and\n1 COW (for the match of number 4 in the wrong position)\n*The player continues to guess until the secret code is cracked.\nThe player who guesses in the minimum number of tries wins.")
    label.pack(pady = 10)

    btn = Button(master,
    text ="Return",
        command = master.destroy)
    btn.pack(pady = 10)

    mainloop()