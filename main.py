from tkinter import *
import random as ra
r = Tk()
r.title("Color Randomizer Game")
r.geometry("300x300")
r.config(bg="white")
lbl = Label(r,font=("Roman",10),bg="white")
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)
#Logic-
class Game():
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ["RED","YELLOW","ORANGE","GREEN","BLUE","PURPLE","BROWN","BLACK"]
        self.random_number_for_text = ra.randint(0,7)
        self.colors = ["red","yellow","orange","green","blue","purple","brown","black"]
        self.random_number_for_colors = ra.randint(0,7)
        self.bg = ["red","yellow","orange","green","blue","purple","brown","black"]
        self.random_number_for_bg = ra.randint(0,7)
        lbl['text'] = self.text[self.random_number_for_text]
        lbl["fg"] = self.colors[self.random_number_for_colors]
        g = self.bg[self.random_number_for_bg]
        lbl['bg'] = str(g)
        r.config(bg=str(g))
obj = Game()
btn = Button(r,text="Start",command=obj.updateGame,bg="white",fg="blue",relief=FLAT,padx=10,pady=1,font=("Arial",15))
btn.place(relx=0.5,rely=0.8,anchor=CENTER)
r.mainloop()