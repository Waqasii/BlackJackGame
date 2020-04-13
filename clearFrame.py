from tkinter import *

def say_hi():
    print("hello ~ !")

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)
root.title("tkinter frame")

label= Label(root,text="Label",justify=LEFT)
label.place(x=15,y=10)

hi_there = Button(root,text="say hiiiiiiii~",command=say_hi)
hi_there.place(x=23,y=15)

print(hi_there.winfo_rootx())
print(root.coors(hi_there))

root.mainloop()