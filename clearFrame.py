from tkinter import *

root = Tk()
a = Button(text=str(1))
a.place(x=0, y=0)

root.update()
widget_x, widget_y = a.winfo_rootx(), a.winfo_rooty()
print(widget_x, widget_y)

root.mainloop()