from tkinter import *

#backend

class User:
    def __init__(self,name,surname):
        self.__name = name
        self.__surname = surname

    def getInfo(self):
        result = self.__name + self.__surname
        return result

def Click():
    print("Hello")


#frontend
root = Tk()
root.geometry("500x500")
root.title("Pencere")
btn = Button(text="Click me!",command=Click)

root.mainloop()