
from tkinter import *

root = Tk()
root.title("経路")
root.resizable(0,0)


grid_length = 30

root_frame = Frame(root, relief='groove', borderwidth=5, bg='LightGray')

game_frame = Frame(root_frame, relief='sunken', borderwidth=3, bg='LightGray')
root_frame.pack()

game_frame.pack(pady=5, padx=5)


####マス目の作成####
def left_click(event):
    if event.widget["bg"] == "black":
        event.widget.configure(relief='raised', borderwidth=3, bg="LightGray")
    elif event.widget["bg"] == "LightGray":
        event.widget.configure(relief='raised', borderwidth=3, bg="black")
    print(event.widget.num)


i = 0
frame_list = []
for y in range(20):
    for x in range(40):
        frame = Frame(game_frame, width=grid_length, height=grid_length, bd=3, relief='raised', bg='LightGray')
        frame.bind("<1>", left_click)
        frame.num = i
        frame_list.append(frame)
        frame.grid(row=y, column=x)
        i += 1

root.mainloop()