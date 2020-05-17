from tkinter import *
from tkinter import messagebox as mb, messagebox

from math import *

main_root = Tk(className="Birb")
frm_param = Frame(main_root)


def oval_generate(a, b, shift_x, shift_y):
    temp = list()
    t = 0

    while (t <= 360):
        x = a * cos((t * pi) / 180)
        y = b * sin((t * pi) / 180)
        temp.append([birb_center[0] + (x - shift_x), (birb_center[1] + (y - shift_y))])
        t += 0.1

    return temp


# Service parameters
canvas_screen = [1280, 960]
user_center = [0, 960]
birb_center = [canvas_screen[0] // 2, canvas_screen[1] // 2]    # Center coordinate
ent_width = 10              # Width for all entries
birb_width = 3              # Width for birb
body_a = 120                # Oval rad by x
body_b = 65                 # Oval rad by y
head_r = 40                 # Circle rad

# Coordinates for birb
body = oval_generate(body_a, body_b, 0, 0)
head = oval_generate(head_r, head_r, 85, 90)

beak = [[birb_center[0] - 175, birb_center[1] - 85], 
        [birb_center[0] - 110, birb_center[1] - 120], 
        [birb_center[0] - 110, birb_center[1] - 120], 
        [birb_center[0] - 110, birb_center[1] - 85], 
        [birb_center[0] - 110, birb_center[1] - 85], 
        [birb_center[0] - 175, birb_center[1] - 85]]

tail = [[birb_center[0] + 95, birb_center[1] - 20], 
        [birb_center[0] + 175, birb_center[1] - 25], 
        [birb_center[0] + 175, birb_center[1] - 25], 
        [birb_center[0] + 102, birb_center[1] + 13], 
        [birb_center[0] + 102, birb_center[1] + 13], 
        [birb_center[0] + 95, birb_center[1] - 20]]

wing = [[birb_center[0] + 30, birb_center[1] + 10], 
        [birb_center[0] + 80, birb_center[1] + 10],
        [birb_center[0] + 80, birb_center[1] + 10], 
        [birb_center[0] + 120, birb_center[1] + 100],
        [birb_center[0] + 120, birb_center[1] + 100], 
        [birb_center[0] + 30, birb_center[1] + 10]]

paws = [[birb_center[0] - 35, birb_center[1] + 60], 
        [birb_center[0] - 70, birb_center[1] + 130], 
        [birb_center[0] + 10, birb_center[1] + 65], 
        [birb_center[0] + 50, birb_center[1] + 130]]

birb_coords = [beak, head, body, wing, tail, paws]
undo = [[]] * len(birb_coords)

reset = list()

for i in range(len(birb_coords)):
    reset.append([])
    for j in range(len(birb_coords[i])):
        reset[i].append([])
        reset[i][j].append(birb_coords[i][j][0])
        reset[i][j].append(birb_coords[i][j][1])

reset_center = [0] * 2
undo_center = list()
reset_center[0] = birb_center[0]
reset_center[1] = birb_center[1]


def caching():
    global undo
    global undo_center

    undo_center.clear()
    undo.clear()

    undo_center.append(birb_center[0])
    undo_center.append(birb_center[1])

    for i in range(len(birb_coords)):
        undo.append([])
        for j in range(len(birb_coords[i])):
            undo[i].append([])
            undo[i][j].append(birb_coords[i][j][0])
            undo[i][j].append(birb_coords[i][j][1])



def scale_figure(figure, c_x, c_y):
    for i in range(len(figure)):
        tmp_x = figure[i][0]
        tmp_y = figure[i][1]
        figure[i][0] = (tmp_x - user_center[0]) * c_x + user_center[0]
        figure[i][1] = (tmp_y - user_center[1]) * c_y + user_center[1]

    return figure


def move_figure(figure, x, y):
    for i in range(len(figure)):
        figure[i][0] += x
        figure[i][1] += y

    return figure


def rotate_figure(figure, angle):
    for i in range(len(figure)):
        tmp_x = figure[i][0] - user_center[0]
        tmp_y = figure[i][1] - user_center[1]
        figure[i][0] = tmp_x * cos(angle) - tmp_y * sin(angle) + user_center[0]
        figure[i][1] = tmp_x * sin(angle) + tmp_y * cos(angle) + user_center[1]

    return figure



def scaling():
    global birb_coords
    global birb_center

    caching()

    try:
        coeff_x = float(ent_scale_x.get())
        coeff_y = float(ent_scale_y.get())
    except:
        messagebox.showerror("Error", "Введены некорректные коеф-нты для масштабирования")
        return

    for i in range(len(birb_coords)):
        birb_coords[i] = scale_figure(birb_coords[i], coeff_x, coeff_y)

    #tmp_x = birb_center[0]
    #tmp_y = birb_center[1]
    #birb_center[0] = (tmp_x - user_center[0]) * coeff_x + user_center[0]
    #birb_center[1] = (tmp_y - user_center[1]) * coeff_y + user_center[1]

    cnv_wall.delete(ALL)
    draw_birb()


def moving():
    global birb_center

    try:
        step_x = float(ent_step_x.get())
        step_y = -float(ent_step_y.get())
    except:
        messagebox.showerror("Error", "Введены некорректные смещения.")
        return

    caching()

    for i in range(len(birb_coords)):
        birb_coords[i] = move_figure(birb_coords[i], step_x, step_y)

    #birb_center[0] += step_x
    #birb_center[1] += step_y

    cnv_wall.delete(ALL)
    draw_birb()


def rotating(side):
    global birb_coords
    global birb_center

    caching()

    try:
        angle = ((float(ent_angle.get()) * pi) / 180) * side
    except:
        messagebox.showerror("Error", "Введен некорректный угол поворота")
        return
    
    for i in range(len(birb_coords)):
        birb_coords[i] = rotate_figure(birb_coords[i], angle)

    
    #tmp_x = birb_center[0] - user_center[0]
    #tmp_y = birb_center[1] - user_center[1]

    #birb_center[0] = tmp_x * cos(angle) - tmp_y * sin(angle) + user_center[0]
    #birb_center[1] = tmp_x * sin(angle) + tmp_y * cos(angle) + user_center[1]

    cnv_wall.delete(ALL)
    draw_birb()



def move_up():
    step_x = 0

    try:
        step_y = float(ent_step_y.get()) * -1
    except:
        messagebox.showerror("Error", "Введено некорректное смещение по Y.")
        return

    moving(step_x, step_y)


def move_down():
    step_x = 0

    try:
        step_y = float(ent_step_y.get())
    except:
        messagebox.showerror("Error", "Введено некорректное смещение по Y.")
        return

    #moving(step_x, step_y)


def move_right():
    try:
        step_x = float(ent_step_x.get())
    except:
        messagebox.showerror("Error", "Введено некорректное смещение по X.")
        return

    step_y = 0
    moving(step_x, step_y)


def move_left():
    try:
        step_x = float(ent_step_x.get()) * -1
    except:
        messagebox.showerror("Error", "Введено некорректное смещение по X.")
        return

    step_y = 0
    #moving(step_x, step_y)



def rotate_rigth():
    side = 1
    rotating(side)


def rotate_left():
    side = -1
    rotating(side)



def update_center():
    global user_center

    try:
        new_x = float(ent_center_x.get())
        new_y = canvas_screen[1] - float(ent_center_y.get())
    except:
        messagebox.showerror("Error", "Введены некорректные координаты для центра")
        return

    user_center[0] = new_x
    user_center[1] = new_y
    cnv_wall.delete(ALL)
    draw_birb()


def go_undo():
    global birb_coords
    global birb_center

    birb_center[0] = undo_center[0]
    birb_center[1] = undo_center[1]

    for i in range(len(birb_coords)):
        for j in range(len(birb_coords[i])):
            birb_coords[i][j][0] = undo[i][j][0]
            birb_coords[i][j][1] = undo[i][j][1]
    
    cnv_wall.delete(ALL)
    draw_birb()


def go_reset():
    global birb_coords
    global birb_center

    birb_center[0] = reset_center[0]
    birb_center[1] = reset_center[1]

    for i in range(len(birb_coords)):
        for j in range(len(birb_coords[i])):
            birb_coords[i][j][0] = reset[i][j][0]
            birb_coords[i][j][1] = reset[i][j][1]
    
    cnv_wall.delete(ALL)
    draw_birb()


# Center__________________________________________________
frm_center = LabelFrame(frm_param, text="Координты центра")

lbl_center_x = Label(frm_center, text="По X: ")
ent_center_x = Entry(frm_center, width=ent_width)
ent_center_x.insert(0, '0')

lbl_center_y = Label(frm_center, text="По Y: ")
ent_center_y = Entry(frm_center, width=ent_width)
ent_center_y.insert(0, '0')

btn_center = Button(frm_center, text="Задать", command=update_center)

lbl_center_x.grid(row=0, column=0, sticky="WESN", padx=5)
ent_center_x.grid(row=0, column=1, sticky="WESN", padx=5)
lbl_center_y.grid(row=1, column=0, sticky="WESN", padx=5)
ent_center_y.grid(row=1, column=1, sticky="WESN", padx=5)
btn_center.grid(row=2, column=0, columnspan=2, sticky="WESN", padx=5)

frm_center.grid(row=0, column=0, sticky='WESN')

# Move_____________________________________________
frm_move = LabelFrame(frm_param, text="Перемещение")
frm_step = Frame(frm_move)
frm_btn_move = Frame(frm_move)

lbl_step_x = Label(frm_step, text="Шаг по X:")
ent_step_x = Entry(frm_step, width=ent_width)
ent_step_x.insert(0, '0')

lbl_step_y = Label(frm_step, text="Шаг по Y:")
ent_step_y = Entry(frm_step, width=ent_width)
ent_step_y.insert(0, '0')

lbl_step_x.grid(row=0, column=0, sticky="WESN", padx=5)
ent_step_x.grid(row=0, column=1, sticky="WESN", padx=5)

lbl_step_y.grid(row=1, column=0, sticky="WESN", padx=5)
ent_step_y.grid(row=1, column=1, sticky="WESN", padx=5)

#Buttons
btn_move = Button(frm_btn_move, text="Переместить", command=moving)
btn_move.pack()
'''
txt_move = "▲◄►▼"
fun_move = [move_up, move_left, move_right, move_down]
btn_move = [0] * len(txt_move)

for i in range(len(txt_move)):
    btn_move[i] = Button(frm_btn_move, text=txt_move[i], command=fun_move[i])

btn_move[0].grid(row=0, column=1, sticky='WESN')
btn_move[1].grid(row=1, column=0, sticky='WESN')

btn_useless = Button(frm_btn_move, state=DISABLED)
btn_useless.grid(row=1, column=1, sticky='WESN')

btn_move[2].grid(row=1, column=2, sticky='WESN')
btn_move[3].grid(row=2, column=1, sticky='WESN')
'''
frm_step.grid(row=0, column=0, sticky='WESN')
frm_btn_move.grid(row=1, column=0, padx=10, pady=10)
frm_move.grid(row=1, column=0, sticky='WESN')


# Scale_________________________________________________
frm_scale = LabelFrame(frm_param, text="Масштабирование")

lbl_scale_x = Label(frm_scale, text="По X: ")
ent_scale_x = Entry(frm_scale, width=ent_width)
ent_scale_x.insert(0, '1')

lbl_scale_y = Label(frm_scale, text="По Y: ")
ent_scale_y = Entry(frm_scale, width=ent_width)
ent_scale_y.insert(0, '1')

btn_scale = Button(frm_scale, text="Масштабировать", command=scaling)

lbl_scale_x.grid(row=0, column=0, padx=5)
ent_scale_x.grid(row=0, column=1, padx=5)
lbl_scale_y.grid(row=1, column=0, padx=5)
ent_scale_y.grid(row=1, column=1, padx=5)

btn_scale.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='WESN')

frm_scale.grid(row=2, column=0, sticky='WESN')


# Rotation_____________________________________
frm_rot  = LabelFrame(frm_param, text="Поворот")
frm_angle = Frame(frm_rot)
frm_btn_rot = Frame(frm_rot)

lbl_angle = Label(frm_angle, text="Угол: ")
ent_angle = Entry(frm_angle, width=ent_width)
ent_angle.insert(0, '0')

lbl_angle.grid(row=0, column=0, padx=5)
ent_angle.grid(row=0, column=1, padx=5)

btn_rot_left = Button(frm_btn_rot, text="<", command=rotate_left)
btn_rot_rigth = Button(frm_btn_rot, text=">", command=rotate_rigth)

btn_rot_left.grid(row=0, column=0, sticky='WESN')
btn_rot_rigth.grid(row=0, column=1, sticky='WESN')

frm_angle.grid(row=0, column=0, sticky='WESN')
frm_btn_rot.grid(row=1, column=0, padx=10, pady=10)
frm_rot.grid(row=3, column=0, sticky='WESN')

btn_back = Button(frm_param, text="Вернуть", command=go_undo)
btn_back.grid(row=4, column=0, sticky='WESN', padx=10, pady=10)

btn_reset = Button(frm_param, text="Сброс", command=go_reset)
btn_reset.grid(row=5, column=0, sticky='WESN', padx=10, pady=10)

# Draw_____________________________________________
frm_draw = LabelFrame(main_root, text="Изображение")

cnv_wall = Canvas(frm_draw, width=canvas_screen[0], height=canvas_screen[1], bg="white")

cnv_wall.pack()

frm_draw.grid(row=0, column=1, sticky='WESN')
frm_param.grid(row=0, column=0, sticky='WESN')
    


def draw_birb():
    cnv_wall.create_oval(user_center[0], user_center[1], 
                        user_center[0], user_center[1], 
                        width=6, outline="red")
    #cnv_wall.create_oval(birb_center[0], birb_center[1], 
    #                    birb_center[0], birb_center[1], 
    #                    width=8, outline="blue")
    # Beak
    for i in range(len(beak) - 1):
        cnv_wall.create_line(beak[i][0], beak[i][1], beak[i + 1][0], beak[i + 1][1],
                            width=birb_width + 1)

    # Head
    for i in range(len(head)):
        cnv_wall.create_oval(head[i][0], head[i][1], head[i][0], head[i][1], 
                            width=birb_width)
    
    # Body
    for i in range(len(body)):
        cnv_wall.create_oval(body[i][0], body[i][1], body[i][0], body[i][1], 
                            width=birb_width)

    # Tail
    for i in range(len(tail) - 1):
        cnv_wall.create_line(tail[i][0], tail[i][1], tail[i + 1][0], tail[i + 1][1],
                            width=birb_width + 1)

    # Wing
    for i in range(len(tail) - 1):
        cnv_wall.create_line(wing[i][0], wing[i][1], wing[i + 1][0], wing[i + 1][1],
                            width=birb_width + 1)

    # Paws
    cnv_wall.create_line(paws[0][0], paws[0][1], paws[1][0], paws[1][1], 
                        width=birb_width + 1)
    cnv_wall.create_line(paws[2][0], paws[2][1], paws[3][0], paws[3][1], 
                        width=birb_width + 1)


def main():
    draw_birb()


main()

main_root.mainloop()