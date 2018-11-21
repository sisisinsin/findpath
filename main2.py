
from tkinter import *


root = Tk()
root.title("経路")
root.resizable(0, 0)


grid_length = 30
y_length = 20
x_length = 40
is_start = True
is_target = True


start_positon_x = None
start_positon_y = None
target_postion_x = None
target_postion_y = None

root_frame = Frame(root, relief='groove', borderwidth=5, bg='LightGray')

game_frame = Frame(root_frame, relief='sunken', borderwidth=3, bg='LightGray')
root_frame.pack()

game_frame.pack(pady=5, padx=5)

def left_click(event):
    global is_start
    global is_target
    global start_positon_x
    global start_positon_y
    global target_postion_x
    global target_postion_y
    global start_node

    if is_start == False and event.widget["bg"] == "white":
        event.widget.configure(relief='raised', borderwidth=3, bg="green")
        start_positon_x = event.widget.x
        start_positon_y = event.widget.y
        event.widget.wall = False
        is_start = True
    elif is_target == False and event.widget["bg"] == "white":
        event.widget.configure(relief='raised', borderwidth=3, bg="red")
        target_postion_x = event.widget.x
        target_postion_y = event.widget.y
        is_target = True
    else:
        if event.widget["bg"] == "black":
            event.widget.configure(relief='raised', borderwidth=3, bg="white")
            event.widget.wall = False
            #event.widget.bind("<1>", stop)
        elif event.widget["bg"] == "white":
            event.widget.configure(relief='raised', borderwidth=3, bg="black")
            event.widget.wall = True
        elif is_target == True and event.widget["bg"] == "green":
            is_start = False
            event.widget.configure(relief='raised', borderwidth=3, bg="white")
            event.widget.wall = False
        elif is_start == True and event.widget["bg"] == "red":
            is_target = False
            event.widget.configure(relief='raised', borderwidth=3, bg="white")
            event.widget.wall = False

    #print(event.widget.x)
    #print(event.widget.y)
    

def get_cost(event):
    print(start_positon_x)
    print(start_positon_y)

i = 0
frame_list = []
for y in range(y_length):
    for x in range(x_length):
        frame = Frame(game_frame, width=grid_length, height=grid_length, bd=3, relief='raised', bg="white")
        if y == y_length / 2 and x == x_length / 2 - 5:
            label = Label(frame, relief="raised", text="0", bg="green")
            start_positon_x = x
            start_positon_y = y

        elif y == y_length / 2 and x == x_length / 2 + 5:
            label = Label(frame, relief="raised", text="0", bg="red")
            target_postion_x = x
            target_postion_y = y
        else:
            label = Label(frame, relief="raised", text="0", bg="white")
        label.place(width=28, height=28)
        label.x = x
        label.y = y
        label.wall = False
        label.bind("<1>", left_click)
        i += 1
        frame_list.append(frame)
        frame.grid(row=y, column=x)


calc_frame = Frame(root_frame, borderwidth=3, bg='LightGray')
calc_frame.pack()
calc_button = Button(calc_frame, text="計算")
calc_button.pack()
calc_button.bind("<1>", get_cost)

def stop(event):
    pass



root.mainloop()