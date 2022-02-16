from tkinter import *
import tkinter.messagebox as tmsg


def click():
    global i
    i +=1
    if i%2==0:
        turn = 'O'
        lb_move.config(text="X's Move")
    else:
        turn = 'X'
        lb_move.config(text="O's move")

    val = value.get()
    print(val)
    if val == "Top-Left":
        if turn == 'X':
            can_wid.create_line(0,0,133,133,width=5)
            can_wid.create_line(133,0,0,133,width=5)
        else:
            can_wid.create_oval(0,0,133,133,width=5)
    if val == "Top-Middle":
        if turn == 'X':
            can_wid.create_line(133,0,267,133,width=5)
            can_wid.create_line(267,0,133,133,width=5)
        else:
            can_wid.create_oval(133,0,267,133,width=5)
    if val == "Top-Right":
        if turn == 'X':
            can_wid.create_line(267,0,400,133,width=5)
            can_wid.create_line(400,0,267,133,width=5)
        else:
            can_wid.create_oval(267,0,400,133,width=5)
    if val == "Middle-Left":
        if turn == 'X':
            can_wid.create_line(0,133,133,267,width=5)
            can_wid.create_line(133,133,0,267,width=5)
        else:
            can_wid.create_oval(0,133,133,267,width=5)
    if val == "Middle":
        if turn == 'X':
            can_wid.create_line(133,133,267,267,width=5)
            can_wid.create_line(133,267,267,133,width=5)
        else:
            can_wid.create_oval(133,133,267,267,width=5)
    if val == "Middle-Right":
        if turn == 'X':
            can_wid.create_line(267,133,400,267,width=5)
            can_wid.create_line(400,133,267,267,width=5)
        else:
            can_wid.create_oval(267,133,400,267,width=5)
    if val == "Bottom-Left":
        if turn == 'X':
            can_wid.create_line(0,267,133,400,width=5)
            can_wid.create_line(133,267,0,400,width=5)
        else:
            can_wid.create_oval(0,267,133,400,width=5)
    if val == "Bottom-Middle":
        if turn == 'X':
            can_wid.create_line(133,267,267,400,width=5)
            can_wid.create_line(267,267,133,400,width=5)
        else:
            can_wid.create_oval(133,267,267,400,width=5)

    if val == "Bottom-Right":
        if turn == 'X':
            can_wid.create_line(267,267,400,400,width=5)
            can_wid.create_line(400,267,267,400,width=5)
        else:
            can_wid.create_oval(267,267,400,400,width=5)


def done():
    tmsg.showinfo("Hey There!", "Thanks for playing")
    exit()


i=0
root = Tk()
root.title("TicTacToe Game")
root.geometry("600x750")
root.minsize(600,750)
root.maxsize(600,750)
root.configure(bg="light grey")

can_width = 400
can_height = 400

lb = Label(text="Tic Tac Toe", font="Comicsansms 30 bold",bg="Light Grey")
lb.grid(row=0,column=0,padx=20, pady=10)
lb_move = Label(text="X's Move", font="Comicsansms 15 bold",bg="Light Grey")
lb_move.grid(row=1,column=0,pady=5)

choice = [
    "Top-Left",
    "Top-Middle",
    "Top-Right",
    "Middle-Left",
    "Middle",
    "Middle-Right",
    "Bottom-Left",
    "Bottom-Middle",
    "Bottom-Right"
]

value = StringVar()
value.set("Choose Your Move")
drop = OptionMenu(root, value, *choice)
drop.grid(row=2,column=0)

fr = Frame(root, bg="Light Grey")
fr.grid(row=3,column=0)
b = Button(fr, text="Confirm", command=click)
b.grid(row=3, column=0,pady=10)

can_wid = Canvas(root,width=can_width, height=can_height)
can_wid.grid(row=4,padx=100,pady=15)
can_wid.create_line(133,0,133,400,width="5")        # First vertical line
can_wid.create_line(267,0,267,400,width="5")        # Second vertical line
can_wid.create_line(0,133,400,133,width="5")        # First horizontal line
can_wid.create_line(0,267,400,267,width="5")        # Second horizontal line

fr = Frame(root, bg="Light Grey")
fr.grid(row=6)
b = Button(fr,text="Done",command=done, width=20, height=2, bg="white", relief=RAISED)
b.grid(row=6,pady=5)

root.mainloop()