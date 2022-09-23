from tkinter import *
from tkinter import messagebox

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.resizable(width=False, height=False)
        self.player_1 = True
        self.row1 = []
        self.row2 = []
        self.row3 = []
        self.col1 = []
        self.col2 = []
        self.col3 = []
        self.dig1 = []
        self.dig2 = []
        self.running = True
        self.count = 0
        self.widget()

    def widget(self):
        self.one = Button(self.master, text="", width=25, height=10, command=lambda: self.mark(self.one))
        self.one.grid(row=0, column=0)

        self.two = Button(self.master, text="", width=25, height=10, command=lambda: self.mark(self.two))
        self.two.grid(row=0, column=1)

        self.three = Button(self.master, text="", width=25, height=10, command=lambda: self.mark(self.three))
        self.three.grid(row=0, column=3)

        self.four = Button(self.master, text="", width=25, height=10, command=lambda: self.mark(self.four))
        self.four.grid(row=1, column=0)

        self.five = Button(self.master, text="", width=25, height=10, command=lambda: self.mark(self.five))
        self.five.grid(row=1, column=1)

        self.six = Button(self.master, text="", width=25, height=10, command=lambda: self.mark(self.six))
        self.six.grid(row=1, column=3)

        self.seven = Button(self.master, text="", width=25, height=10, command=lambda: self.mark(self.seven))
        self.seven.grid(row=3, column=0)

        self.eight = Button(self.master, text="", width=25, height=10, command=lambda: self.mark(self.eight))
        self.eight.grid(row=3, column=1)

        self.nine = Button(self.master, text="", width=25, height=10, command=lambda: self.mark(self.nine))
        self.nine.grid(row=3, column=3)

    def mark(self, b):
        if self.player_1 and b["text"] == "":
            b["text"] = "X"
            self.player_1 = False
            self.count += 1
            b.config(bg="#EE8CAD")
        elif not self.player_1 and b["text"] == "":
            b["text"] = "O"
            self.player_1 = True
            self.count += 1
            b.config(bg="#84BDE0")
        else:
            messagebox.showerror("Tic Tac Toe", "This box is not empty. Pick another box.")

        if b == self.one or b == self.two or b == self.three:
            self.row1.append(b["text"])
        elif b == self.four or b == self.five or b == self.six:
            self.row2.append(b["text"])
        elif b == self.seven or b == self.eight or b == self.nine:
            self.row3.append(b["text"])

        if b == self.one or b == self.four or b == self.seven:
            self.col1.append(b["text"])
        elif b == self.two or b == self.five or b == self.eight:
            self.col2.append(b["text"])
        elif b == self.three or b == self.six or b == self.nine:
            self.col3.append(b["text"])

        if b == self.one or b == self.five or b == self.nine:
            self.dig1.append(b["text"])
        elif b == self.three or b == self.five or b == self.seven:
            self.dig2.append(b["text"])

        self.winner()

        if self.count == 9:
            messagebox.showinfo("Tic Tac Toe", "It is a Tie")
            self.running = False
            self.restart()

        self.restart()

    def winner(self):
        all = [self.row1, self.row2, self.row3, self.col1, self.col2, self.col3, self.dig1, self.dig2]

        for line in all:
            if len(line) == 3:
                if line.count(line[0]) == len(line):
                    if self.player_1 == True:
                        messagebox.showinfo("Tic Tac Toe", "Player 2 Won")
                    else:
                        messagebox.showinfo("Tic Tac Toe", "Player 1 Won")
                    self.running = False

    def restart(self):
        if self.running == False:
            self.player_1 = True
            self.row1 = []
            self.row2 = []
            self.row3 = []
            self.col1 = []
            self.col2 = []
            self.col3 = []
            self.dig1 = []
            self.dig2 = []
            self.running = True
            self.count = 0
            self.widget()




root = Tk()
my_gui = GUI(root)
root.mainloop()

