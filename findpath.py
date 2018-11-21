from tkinter import *

root = Tk()
root.title("経路")
root.resizable(0, 0)

grid_length = 30
y_length = 20
x_length = 40
not_go = 10000
mode = 1
is_start = True
is_target = True

start_position_x = None
start_position_y = None
target_position_x = None
target_position_y = None

f_cost = []  # コスト
old_f_cost = []  # コスト
g_cost = []  # コスト
h_cost = []
labels = []  # ラベルの座標
walls = []  # 壁があるか
parent = []

for i in range(y_length):
    f_cost.append([not_go for i in range(x_length)])
    old_f_cost.append([not_go for i in range(x_length)])
    g_cost.append([not_go for i in range(x_length)])
    h_cost.append([not_go for i in range(x_length)])
    labels.append([None for i in range(x_length)])
    walls.append([None for i in range(x_length)])
    parent.append(([None for i in range(x_length)]))

# print(nodes)

root_frame = Frame(root, relief='groove', borderwidth=5, bg='LightGray')

game_frame = Frame(root_frame, relief='sunken', borderwidth=3, bg='LightGray')
root_frame.pack()

game_frame.pack(pady=5, padx=5)


def left_click(event):
    global is_start
    global is_target
    global start_position_x
    global start_position_y
    global target_position_x
    global target_position_y
    global start_node

    if is_start == False and event.widget["bg"] == "white":
        event.widget.configure(relief='raised', borderwidth=3, bg="green")
        start_position_x = event.widget.x
        start_position_y = event.widget.y
        event.widget.wall = False
        walls[event.widget.y][event.widget.x] = False
        is_start = True
    elif is_target == False and event.widget["bg"] == "white":
        event.widget.configure(relief='raised', borderwidth=3, bg="red")
        target_position_x = event.widget.x
        target_position_y = event.widget.y
        event.widget.wall = False
        walls[event.widget.y][event.widget.x] = False
        is_target = True
    else:
        if event.widget["bg"] == "black":
            event.widget.configure(relief='raised', borderwidth=3, bg="white")
            walls[event.widget.y][event.widget.x] = False
            event.widget.wall = False
            # event.widget.bind("<1>", stop)
        elif event.widget["bg"] == "white" or event.widget["bg"] == "LightGray" or event.widget["bg"] == "steelblue":
            event.widget.configure(relief='raised', borderwidth=3, bg="black")
            walls[event.widget.y][event.widget.x] = True
            event.widget.wall = True
        elif is_target == True and event.widget["bg"] == "green":
            is_start = False
            event.widget.configure(relief='raised', borderwidth=3, bg="white")
            walls[event.widget.y][event.widget.x] = False
            event.widget.wall = False
        elif is_start == True and event.widget["bg"] == "red":
            is_target = False
            event.widget.configure(relief='raised', borderwidth=3, bg="white")
            walls[event.widget.y][event.widget.x] = False
            event.widget.wall = False

    # print(event.widget.x)
    # print(event.widget.y)


def clear_cost(event):
    for y in range(y_length):
        for x in range(x_length):
            old_f_cost[y][x] = f_cost[y][x]


def get_cost(event):
    for y in range(y_length):
        for x in range(x_length):
            f_cost[y][x] = not_go
            g_cost[y][x] = not_go
            h_cost[y][x] = not_go
            parent[y][x] = None
            if labels[y][x]["bg"] == "steelblue" or labels[y][x]["bg"] == "LightGray":
                labels[y][x].configure(bg="white")


    start_x = start_position_x
    start_y = start_position_y
    target_x = target_position_x
    target_y = target_position_y
    open_list = []
    close_list = []
    f_cost[start_y][start_x] = 0
    g_cost[start_y][start_x] = 0

    open_list.append(labels[start_y][start_x])

    global mode
    mode = v.get()

    while start_x != target_position_x or start_y != target_position_y:
        # 左上
        if not start_y - 1 < 0 and not start_x - 1 < 0:
            if walls[start_y - 1][start_x - 1] == False and (walls[start_y - 1][start_x] == False or walls[start_y][start_x - 1] == False):
                tmp_f_cost = f_cost[start_y - 1][start_x - 1]
                tmp_g_cost = g_cost[start_y - 1][start_x - 1]
                g_cost[start_y - 1][start_x - 1] = g_cost[start_y][start_x] + calc_distance(start_x, start_y,
                                                                                            start_x - 1, start_y - 1)

                h_cost[start_y - 1][start_x - 1] = calc_distance(target_x, target_y, start_x - 1, start_y - 1)

                if tmp_g_cost < g_cost[start_y - 1][start_x - 1]:
                    g_cost[start_y - 1][start_x - 1] = tmp_g_cost

                f_cost[start_y - 1][start_x - 1] = g_cost[start_y - 1][start_x - 1] + h_cost[start_y - 1][start_x - 1]

                if tmp_f_cost <= f_cost[start_y - 1][start_x - 1]:
                    f_cost[start_y - 1][start_x - 1] = tmp_f_cost
                else:
                    open_list.append(labels[start_y - 1][start_x - 1])
                    parent[start_y - 1][start_x - 1] = labels[start_y][start_x]
        # 上
        if not start_y - 1 < 0:
            if walls[start_y - 1][start_x] == False:
                tmp_f_cost = f_cost[start_y - 1][start_x]
                tmp_g_cost = g_cost[start_y - 1][start_x]
                g_cost[start_y - 1][start_x] = g_cost[start_y][start_x] + calc_distance(start_x, start_y, start_x,
                                                                                        start_y - 1)

                h_cost[start_y - 1][start_x] = calc_distance(target_x, target_y, start_x, start_y - 1)

                if tmp_g_cost < g_cost[start_y - 1][start_x]:
                    g_cost[start_y - 1][start_x] = tmp_g_cost

                f_cost[start_y - 1][start_x] = g_cost[start_y - 1][start_x] + h_cost[start_y - 1][start_x]
                if tmp_f_cost <= f_cost[start_y - 1][start_x]:
                    f_cost[start_y - 1][start_x] = tmp_f_cost
                else:
                    open_list.append(labels[start_y - 1][start_x])
                    parent[start_y - 1][start_x] = labels[start_y][start_x]
        # 右上
        if not start_y - 1 < 0 and not start_x + 1 >= x_length:
            if walls[start_y - 1][start_x + 1] == False and (walls[start_y - 1][start_x] == False or walls[start_y][start_x + 1] == False):
                tmp_f_cost = f_cost[start_y - 1][start_x + 1]
                tmp_g_cost = g_cost[start_y - 1][start_x + 1]
                g_cost[start_y - 1][start_x + 1] = g_cost[start_y][start_x] + calc_distance(start_x, start_y,
                                                                                            start_x + 1, start_y - 1)

                h_cost[start_y - 1][start_x + 1] = calc_distance(target_x, target_y, start_x + 1, start_y - 1)

                if tmp_g_cost < g_cost[start_y - 1][start_x + 1]:
                    g_cost[start_y - 1][start_x + 1] = tmp_g_cost

                f_cost[start_y - 1][start_x + 1] = g_cost[start_y - 1][start_x + 1] + h_cost[start_y - 1][start_x + 1]
                if tmp_f_cost <= f_cost[start_y - 1][start_x + 1]:
                    f_cost[start_y - 1][start_x + 1] = tmp_f_cost
                else:
                    open_list.append(labels[start_y - 1][start_x + 1])
                    parent[start_y - 1][start_x + 1] = labels[start_y][start_x]
        # 左
        if not start_x - 1 < 0:
            if walls[start_y][start_x - 1] == False:
                tmp_f_cost = f_cost[start_y][start_x - 1]
                tmp_g_cost = g_cost[start_y][start_x - 1]
                g_cost[start_y][start_x - 1] = g_cost[start_y][start_x] + calc_distance(start_x, start_y, start_x - 1,
                                                                                        start_y)

                h_cost[start_y][start_x - 1] = calc_distance(target_x, target_y, start_x - 1, start_y)

                if tmp_g_cost < g_cost[start_y][start_x - 1]:
                    g_cost[start_y][start_x - 1] = tmp_g_cost

                f_cost[start_y][start_x - 1] = g_cost[start_y][start_x - 1] + h_cost[start_y][start_x - 1]
                if tmp_f_cost <= f_cost[start_y][start_x - 1]:
                    f_cost[start_y][start_x - 1] = tmp_f_cost
                else:
                    open_list.append(labels[start_y][start_x - 1])
                    parent[start_y][start_x - 1] = labels[start_y][start_x]
        # 右
        if not start_x + 1 >= x_length:
            if walls[start_y][start_x + 1] == False:
                tmp_f_cost = f_cost[start_y][start_x + 1]
                tmp_g_cost = g_cost[start_y][start_x + 1]
                g_cost[start_y][start_x + 1] = g_cost[start_y][start_x] + calc_distance(start_x, start_y, start_x + 1,
                                                                                        start_y)

                h_cost[start_y][start_x + 1] = calc_distance(target_x, target_y, start_x + 1, start_y)

                if tmp_g_cost < g_cost[start_y][start_x + 1]:
                    g_cost[start_y][start_x + 1] = tmp_g_cost

                f_cost[start_y][start_x + 1] = g_cost[start_y][start_x + 1] + h_cost[start_y][start_x + 1]
                if tmp_f_cost <= f_cost[start_y][start_x + 1]:
                    f_cost[start_y][start_x + 1] = tmp_f_cost
                else:
                    open_list.append(labels[start_y][start_x + 1])
                    parent[start_y][start_x + 1] = labels[start_y][start_x]
        # 左下
        if not start_y + 1 >= y_length and not start_x - 1 < 0:
            if walls[start_y + 1][start_x - 1] == False and (walls[start_y + 1][start_x] == False or walls[start_y][start_x - 1] == False):
                tmp_f_cost = f_cost[start_y + 1][start_x - 1]
                tmp_g_cost = g_cost[start_y + 1][start_x - 1]
                g_cost[start_y + 1][start_x - 1] = g_cost[start_y][start_x] + calc_distance(start_x, start_y,
                                                                                            start_x - 1, start_y + 1)

                h_cost[start_y + 1][start_x - 1] = calc_distance(target_x, target_y, start_x - 1, start_y + 1)

                if tmp_g_cost < g_cost[start_y + 1][start_x - 1]:
                    g_cost[start_y + 1][start_x - 1] = tmp_g_cost

                f_cost[start_y + 1][start_x - 1] = g_cost[start_y + 1][start_x - 1] + h_cost[start_y + 1][start_x - 1]
                if tmp_f_cost <= f_cost[start_y + 1][start_x - 1]:
                    f_cost[start_y + 1][start_x - 1] = tmp_f_cost
                else:
                    open_list.append(labels[start_y + 1][start_x - 1])
                    parent[start_y + 1][start_x - 1] = labels[start_y][start_x]
        # 下
        if not start_y + 1 >= y_length:
            if walls[start_y + 1][start_x] == False:
                tmp_f_cost = f_cost[start_y + 1][start_x]
                tmp_g_cost = g_cost[start_y + 1][start_x]
                g_cost[start_y + 1][start_x] = g_cost[start_y][start_x] + calc_distance(start_x, start_y, start_x,
                                                                                        start_y + 1)

                h_cost[start_y + 1][start_x] = calc_distance(target_x, target_y, start_x, start_y + 1)

                if tmp_g_cost < g_cost[start_y + 1][start_x]:
                    g_cost[start_y + 1][start_x] = tmp_g_cost

                f_cost[start_y + 1][start_x] = g_cost[start_y + 1][start_x] + h_cost[start_y + 1][start_x]
                if tmp_f_cost <= f_cost[start_y + 1][start_x]:
                    f_cost[start_y + 1][start_x] = tmp_f_cost
                else:
                    open_list.append(labels[start_y + 1][start_x])
                    parent[start_y + 1][start_x] = labels[start_y][start_x]
        # 右下
        if not start_y + 1 >= y_length and not start_x + 1 >= x_length:
            if walls[start_y + 1][start_x + 1] == False and (walls[start_y + 1][start_x] == False or walls[start_y][start_x + 1] == False):
                tmp_f_cost = f_cost[start_y + 1][start_x + 1]
                tmp_g_cost = g_cost[start_y + 1][start_x + 1]
                g_cost[start_y + 1][start_x + 1] = g_cost[start_y][start_x] + calc_distance(start_x, start_y,
                                                                                            start_x + 1, start_y + 1)

                h_cost[start_y + 1][start_x + 1] = calc_distance(target_x, target_y, start_x + 1, start_y + 1)

                if tmp_g_cost < g_cost[start_y + 1][start_x + 1]:
                    g_cost[start_y + 1][start_x + 1] = tmp_g_cost

                f_cost[start_y + 1][start_x + 1] = g_cost[start_y + 1][start_x + 1] + h_cost[start_y + 1][start_x + 1]
                if tmp_f_cost <= f_cost[start_y + 1][start_x + 1]:
                    f_cost[start_y + 1][start_x + 1] = tmp_f_cost
                else:
                    open_list.append(labels[start_y + 1][start_x + 1])
                    parent[start_y + 1][start_x + 1] = labels[start_y][start_x]

        start_x = open_list[0].x
        start_y = open_list[0].y

        for i, label in enumerate(open_list):
            label = open_list[i]
            if label not in close_list:
                if f_cost[label.y][label.x] < f_cost[start_y][start_x] or (f_cost[label.y][label.x] == f_cost[start_y][start_x] and h_cost[label.y][label.x] < h_cost[start_y][start_x]):
                    start_x = label.x
                    start_y = label.y

        if (len(open_list) != 0):
            open_list.remove(labels[start_y][start_x])
            close_list.append(labels[start_y][start_x])

    get_path(target_position_x, target_position_y)

    for y in range(y_length):
        for x in range(x_length):
            labels[y][x].configure(text=f_cost[y][x])

            # 仮色つけ
            if f_cost[y][x] != not_go and labels[y][x]["bg"] == "white":
                labels[y][x].configure(bg="LightGray")

            """
            if f_cost[y][x] != old_f_cost[y][x] and labels[y][x].wall == False and labels[y][x]["bg"] == "white":
                labels[y][x].configure(text=f_cost[y][x], bg="LightGray")
            else:
                if labels[y][x]["bg"] == "LightGray":
                    labels[y][x].configure(text=f_cost[y][x], bg ="white")
                else:
                    labels[y][x].configure(text=f_cost[y][x])
                old_f_cost[y][x] = f_cost[y][x]
            """


def get_path(t_x, t_y):
    count = 0
    while t_x != start_position_x or t_y != start_position_y:
        next = parent[t_y][t_x]
        t_x = next.x
        t_y = next.y
        if next != labels[start_position_y][start_position_x]:
            next.configure(bg="steelblue")
            count += 1

    path_label.configure(text=count)

def calc_distance(a_x, a_y, b_x, b_y):
    cost_x = abs(a_x - b_x)
    cost_y = abs(a_y - b_y)
    if mode == 1:
        if cost_x > cost_y:
            return 14 * cost_y + 10 * (cost_x - cost_y)
        else:
            return 14 * cost_x + 10 * (cost_y - cost_x)
    elif mode == 2:
        return cost_x + cost_y
    elif mode == 3:
        return cost_x * cost_x + cost_y * cost_y

def f_cost_view(event):
    for y in range(y_length):
        for x in range(x_length):
            labels[y][x].configure(text=f_cost[y][x])

def g_cost_view(event):
    for y in range(y_length):
        for x in range(x_length):
            labels[y][x].configure(text=g_cost[y][x])

def h_cost_view(event):
    for y in range(y_length):
        for x in range(x_length):
            labels[y][x].configure(text=h_cost[y][x])

frame_list = []
for y in range(y_length):
    for x in range(x_length):
        frame = Frame(game_frame, width=grid_length, height=grid_length, bd=3, relief='raised', bg="white")
        if y == y_length / 2 and x == x_length / 2 - 5:
            label = Label(frame, relief="raised", text=f_cost[y][x], bg="green")
            start_position_x = x
            start_position_y = y

        elif y == y_length / 2 and x == x_length / 2 + 5:
            label = Label(frame, relief="raised", text=f_cost[y][x], bg="red")
            target_position_x = x
            target_position_y = y
        else:
            label = Label(frame, relief="raised", text=f_cost[y][x], bg="white")
        label.place(width=32, height=32)
        label.x = x
        label.y = y
        label.wall = False
        walls[y][x] = False
        labels[y][x] = label
        label.bind("<1>", left_click)
        frame_list.append(frame)
        frame.grid(row=y, column=x)

calc_frame = Frame(root_frame, borderwidth=3, bg='LightGray')
calc_frame.pack()
calc_button = Button(calc_frame, text="計算")
calc_button.grid(row=1, column=1)
calc_button.bind("<1>", get_cost)
clear_button = Button(calc_frame, text="クリア")
clear_button.grid(row=1, column=2)
clear_button.bind("<1>", clear_cost)
f_button = Button(calc_frame, text="fコスト")
f_button.grid(row=1, column=3)
f_button.bind("<1>", f_cost_view)
g_button = Button(calc_frame, text="gコスト")
g_button.grid(row=1, column=4)
g_button.bind("<1>", g_cost_view)
h_button = Button(calc_frame, text="hコスト")
h_button.grid(row=1, column=5)
h_button.bind("<1>", h_cost_view)
path_label = Label(calc_frame, text="00", bg="white")
path_label.grid(row=1, column=6)
v = IntVar()
v.set(1)

radio1 = Radiobutton(calc_frame, text="Di", variable=v, value=1, bg="LightGray")
radio1.grid(row=2, column=1)

radio2 = Radiobutton(calc_frame, text="Ma", variable=v, value=2, bg="LightGray")
radio2.grid(row=2, column=2)

radio3 = Radiobutton(calc_frame, text="U", variable=v, value=3, bg="LightGray")
radio3.grid(row=2, column=3)

root.mainloop()
