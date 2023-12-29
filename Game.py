import random
from tkinter import *
from copy import deepcopy


class Game:
    def __init__(self):
        self.width = 1080
        self.height = 720
        self.root = Tk()
        self.root.title("Anglais")
        menubar = Menu(self.root, relief=SUNKEN)
        filemenu = Menu(menubar, tearoff=0)
        L = ["Francais -> Anglais", "Anglais -> Français"]
        for machin in L:
            filemenu.add_checkbutton(label=machin, font=('Arial', 16))

        menubar.add_cascade(label="Sens", menu=filemenu)
        self.root.config(menu=menubar)
        self.label = Label(self.root, text="Init", font=('Arial', 20))
        self.label.pack()
        self.entry = Entry(self.root, font=('Arial', 20), justify=CENTER)
        self.entry.pack()
        self.submit = Button(self.root, font=('Arial', 20), command=self.check_answer, text="Submit")
        self.submit.pack()
        self.label2 = Label(self.root, text="", font=('Arial', 20))
        self.label2.pack()
        self.dictionary = {}
        with open('words.txt', 'r', encoding="utf-8") as f:
            for line in f:
                a, b = line.split(":")
                self.dictionary[a] = b
        self.working_dictionary = deepcopy(self.dictionary)
        self.pick_word()
        self.root.bind('<Return>', self.check_answer)

    def pick_word(self):
        if len(self.working_dictionary) == 0:
            self.working_dictionary = deepcopy(self.dictionary)
        self.key = random.choice(list(self.working_dictionary))
        self.working_dictionary.pop(self.key)
        self.value = self.dictionary[self.key][:-1]
        self.label.config(text=self.key)
        self.entry.delete(0, END)

    def check_answer(self, event=None):
        if self.entry.get() == self.value:
            self.pick_word()
            self.label2.configure(text="Correct", fg="green")
        else:
            self.label2.config(text=self.key+":"+self.value, fg="red")
            self.pick_word()

    def main(self):
        self.root.mainloop()

game = Game()
game.main()
