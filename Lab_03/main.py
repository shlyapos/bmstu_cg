from tkinter import Tk, LabelFrame, Frame, Label, Button, Entry, IntVar, Canvas, Radiobutton, Menu, ALL
from tkinter import messagebox as mb, messagebox

from math import cos, sin, pi, fabs
from time import monotonic

root = Tk(className="Рисование прямых")

''' ### Service constants ### '''
cnv_size = [500, 500]
ent_width = 10
padx_const = 5
pady_const = 5

# For method radiobuttons picker 
# In paint 
meth_paint = IntVar()
meth_paint.set(0)
# In analys
meth_analyse = IntVar()
meth_analyse.set(0)

meth_bg_analyse = IntVar()
meth_bg_analyse.set(0)

# For color radiobuttons picker
# In paint
color_paint = IntVar()
color_paint.set(0)
# In analys
color_analyse = IntVar()
color_analyse.set(0)

# Methods name
method_name = ["Цифрового дифференциального анализатора",
               "Брезенхема (для действительных чисел)",
               "Брезенхема (для целых чисел)",
               "Брезенхема (с устранением ступенчатости)",
               "Ву",
               "Встроенная функция"]

# Colors for methods
colors      = ["#000",
               "#00f",
               "#0f0",
               "#f00"]
colors_name = ["Чёрный",
               "Синий",
               "Зелёный",
               "Красный"]
pixel_width = 2
I = 192

frm_paint = LabelFrame(root, text="Рисование отрезков")
frm_analyse = LabelFrame(root, text="Анализ методов")


def set_16th_numb(tmp):
    if tmp < 10:
        return str(tmp)
    
    if tmp == 10:
        return "a"
    if tmp == 11:
        return "b"
    elif tmp == 12:
        return "c"
    elif tmp == 13:
        return "d"
    elif tmp == 14:
        return "e"
    elif tmp == 15:
        return "f"


def convert_number(numb):
    numb_16 = ""

    tmp = numb // 16
    numb_16 += set_16th_numb(tmp)

    tmp = numb % 16
    numb_16 += set_16th_numb(tmp)
    
    return numb_16


def draw_pixel(x, y, color, wall):
    wall.create_oval(x, y, x, y, fill=color)


def draw_pixel_i(x, y, std_color, i, wall):
    if i > 255:
        i = 255

    i = int(i)
    
    if i < 0:
        i *= -1
        
    color = "#"
    sh = str(convert_number(i))

    if (std_color[1] == 'f'):
        color += "ff" + sh + sh
    elif (std_color[2] == 'f'):
        color += sh + "ff" + sh
    elif (std_color[3] == 'f'):
        color += sh + sh + "ff"
    else:
        color += sh + sh + sh

    wall.create_oval(x, y, x, y, fill=color, outline=color)



def rounding(num):
    int_num = int(num + (0.5 if num > 0 else -0.5))
    return int_num


def fpart(num):
    return num - int(num)


def ipart(num):
    return num - fpart(num)


def sign(num):
    if (num > 0):
        return 1
    elif (num < 0):
        return -1
    else:
        return 0


def method_picker(ind):
    if (ind == 0):
        return draw_cda_line
    elif (ind == 1):
        return draw_bresenham_float_line
    elif (ind == 2):
        return draw_bresenham_int_line
    elif (ind == 3):
        return draw_bresenham_step_remove_line
    elif (ind == 4):
        return draw_vu_line
    else:
        return draw_standart_line


def useless_func():
    pass


def rotate_point(xs, ys, xe, ye, angle):
    a = (angle * pi / 180)

    x = xs + (xe - xs) * cos(a) - (ye - ys) * sin(a)
    y = ys + (ye - ys) * cos(a) + (xe - xs) * sin(a)

    return x, y


'''#### _Methods_ ####'''
def draw_cda_line(xs, ys, xe, ye, color, wall):
    if (xs == xe) and (ys == ye):
        draw_pixel(xs, ys, color, wall)
    else:
        if abs(xe - xs) > abs(ye - ys):
            l = abs(xe - xs)
        else:
            l = abs(ye - ys)

        dx = (xe - xs) / l
        dy = (ye - ys) / l
        x = xs
        y = ys
        i = 1

        while (i < dx + l):
            draw_pixel(round(x), round(y), color, wall)
            x += dx
            y += dy
            i += 1


def draw_bresenham_float_line(xs, ys, xe, ye, color, wall):
    if (xs == xe) and (ys == ye):
        draw_pixel(xs, ys, color, wall)
    else:
        dx = xe - xs
        dy = ye - ys
        # sign() возвращает знак числа
        sx = sign(dx)
        sy = sign(dy)
        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            fl = 0
        else:
            fl = 1
            dx, dy = dy, dx
        # Модуль тангенса угла наклона
        m = dy / dx
        # Начальное значение ошибки
        f = m - 0.5

        x = xs
        y = ys
        i = 1
        
        while i < dx + 1:
            draw_pixel(x, y, color, wall)
            # Вычисление координат и ошибки для следю пиксела
            if f >= 0:
                if fl == 1:
                    x += sx
                else:
                    y += sy
                # Корректировка ошибки
                f -= 1
            if f < 0:
                if fl == 1:
                    y += sy
                else:
                    x += sx
            # Вычисление ошибки
            f += m
            i += 1


def draw_bresenham_int_line(xs, ys, xe, ye, color, wall):
    if (xs == xe) and (ys == ye):
        draw_pixel(xs, ys, color, wall)
    else:
        dx = xe - xs
        dy = ye - ys
        # sign() возвращает знак числа
        sx = sign(dx)
        sy = sign(dy)
        dx = abs(dx)
        dy = abs(dy)
        x = xs
        y = ys

        fl = 0

        if dy > dx:
            dx, dy = dy, dx
            fl = 1

        # Инициализация начального значения ошибки
        f = 2 * dy - dx
        i = 1

        while i <= dx:
            draw_pixel(x, y, color, wall)
            # Вычисление координат и ошибки для следующего пиксела
            if f >= 0:
                if fl == 0:
                    y += sy
                else:
                    x += sx
                # Корректировка ошибки
                f -= 2 * dx
            if fl == 0:
                x += sx
            else:
                y += sy
            # Вычисление ошибки
            f += 2 * dy
            i += 1


def draw_bresenham_step_remove_line(xs, ys, xe, ye, color, wall):
    if (xs == xe) and (ys == ye):
        draw_pixel(xs, ys, color, wall)
        return

    # Количество уровней интенсивности
    I = 255

    dx = xe - xs
    dy = ye - ys
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        fl = 0
    else:
        fl = 1
        dx, dy = dy, dx
    # Вычисление модуля тангенса угла наклона отрезка
    m = dy / dx
    # Вычисление начального значения ошибки
    f = I / 2
    x = xs
    y = ys
    # Вычисление скорректированного значения тангенса угла наклона и
    # коэффициента w
    m *= I
    w = I - m
    i = 0

    draw_pixel_i(x, y, color, rounding(f), wall)

    while i < dx:
        if f <= w:
            if fl == 0:
                x += sx
            if fl == 1:
                 y += sy
            f += m
        else:
            x += sx
            y += sy
            f -= w
        draw_pixel_i(x, y, color, rounding(f), wall)
        i += 1


def draw_vu_line(xs, ys, xe, ye, color, wall):
    if (xs == xe) and (ys == ye):
        draw_pixel(xs, ys, color, wall)
        return
    
    st = abs(ye - ys) > abs(xe - xs)

    if st:
        xs, ys = ys, xs
        xe, ye = ye, xe
    
    if xs > xe:
        xs, xe = xe, xs
        ys, ye = ye, ys
    
    x0 = round(xs)
    y0 = round(ys)
    x1 = round(xe)
    y1 = round(ye)

    dx = xe - xs
    dy = ye - ys

    # Высвечивание начала и конца отрезка
    draw_pixel(x0, y0, color, wall)
    draw_pixel(x1, y1, color, wall)

    gradient = dy / dx
    y = y0 + gradient

    # На каждом шаге ведётся расчёт для 2-х ближайших к прямой пикселов,
    # которые закрашиваются с разной интенсивностью, в зависимости от расстояния
    for x in range(x0 + 1, x1):
        if st:
            draw_pixel_i(int(y), x, color, 1 - (y - int(y)) * I, wall)
            draw_pixel_i(int(y + 1), x, color, (y - int(y)) * I, wall)
        else:
            draw_pixel_i(x, int(y), color, 1 - (y - int(y)) * I, wall)
            draw_pixel_i(x, int(y + 1), color, (y - int(y)) * I, wall)
        y += gradient


def draw_standart_line(xs, ys, xe, ye, color, wall):
    wall.create_line(xs, ys, xe, ye, width=pixel_width, fill=color)



def paint_draw_line():
    color = colors[color_paint.get()]

    try:
        xs = float(ent_paint_start_x.get())
        ys = cnv_size[1] - float(ent_paint_start_y.get())
    except:
        messagebox.showerror("Ошибка", "Поля ввода начала отрезка пусты или содержат некорректные символы")
        return

    try:
        xe = float(ent_paint_end_x.get())
        ye = cnv_size[1] - float(ent_paint_end_y.get())
    except:
        messagebox.showerror("Ошибка", "Поля ввода конца отрезка пусты или содержат некорректные символы")
        return    

    if (meth_paint.get() == 0):
        draw_cda_line(xs, ys, xe, ye, color, cnv_paint_wall)
    elif (meth_paint.get() == 1):
        draw_bresenham_float_line(xs, ys, xe, ye, color, cnv_paint_wall)
    elif (meth_paint.get() == 2):
        draw_bresenham_int_line(xs, ys, xe, ye, color, cnv_paint_wall)
    elif (meth_paint.get() == 3):
        draw_bresenham_step_remove_line(xs, ys, xe, ye, color, cnv_paint_wall)
    elif (meth_paint.get() == 4):
        draw_vu_line(xs, ys, xe, ye, color, cnv_paint_wall)
    elif (meth_paint.get() == 5):
        draw_standart_line(xs, ys, xe, ye, color, cnv_paint_wall)
    else:
        messagebox.showerror("Ошибка", "Неизвестная ошибка выбора метода, попробуйте ещё раз")
        return


def paint_draw_clear():
    cnv_paint_wall.delete(ALL)



def analyse_draw_line():
    color_main = colors[color_analyse.get()]
    color_bg = "white"

    xs = cnv_size[0] // 2
    ys = cnv_size[1] // 2
    xe = xs + cnv_size[0] - 300
    ye = ys

    try:
        angle = float(ent_analyse_angle.get())
    except:
        messagebox.showerror("Ошибка", "Поле ввода угла пусто или содержит некорректные символы")
        return
    
    k = 360 // angle

    func_method_main = method_picker(meth_analyse.get())
    func_method_bg = method_picker(meth_bg_analyse.get())

    while k > -1:
        func_method_main(xs, ys, xe, ye, color_main, cnv_analyse_wall)

        if (meth_bg_analyse.get() != 6):
            func_method_bg(xs, ys, xe, ye, color_bg, cnv_analyse_wall)

        xe, ye = rotate_point(xs, ys, xe, ye, angle)
        k -= 1


def analyse_draw_clear():
    cnv_analyse_wall.delete(ALL)



def destruct_all():
    frm_paint.pack_forget()
    frm_analyse.pack_forget()


def construct_paint():
    destruct_all()
    frm_paint.pack()


def construct_analyse():
    destruct_all()
    frm_analyse.pack()


''' ### Paint ### '''
# _Frames_
frm_paint_param = LabelFrame(frm_paint, text="Опции")
frm_paint_color = LabelFrame(frm_paint, text="Цвета")
frm_paint_draw = LabelFrame(frm_paint, text="Изображение")


# _Canvas_
lbl_cnv_paint_left_up = Label(frm_paint_draw, text="(0; " + str(cnv_size[1]) + ")")
lbl_cnv_paint_rigth_up = Label(frm_paint_draw, text="(" + str(cnv_size[0]) + "; " + str(cnv_size[1]) + ")")
lbl_cnv_paint_rigth_down = Label(frm_paint_draw, text="(" + str(cnv_size[0]) + "; 0)")
lbl_cnv_paint_left_down = Label(frm_paint_draw, text="(0; 0)")

lbl_cnv_paint_left_up.grid(row=0, column=0, sticky="WESN")
lbl_cnv_paint_rigth_up.grid(row=0, column=2, sticky="WESN")

cnv_paint_wall = Canvas(frm_paint_draw, height=cnv_size[0], width=cnv_size[1], bg="white")
cnv_paint_wall.grid(row=1, column=1, sticky="WESN")

lbl_cnv_paint_left_down.grid(row=2, column=0, sticky="WESN")
lbl_cnv_paint_rigth_down.grid(row=2, column=2, sticky="WESN")


# _Start_ 
frm_paint_start = LabelFrame(frm_paint_param, text="Начало отрезка")

lbl_paint_start_x = Label(frm_paint_start, text="X: ")
lbl_paint_start_x.grid(row=0, column=0, padx=padx_const, sticky="WESN")

ent_paint_start_x = Entry(frm_paint_start, width=ent_width)
ent_paint_start_x.grid(row=0, column=1, padx=padx_const, sticky="WESN")

lbl_paint_start_y = Label(frm_paint_start, text="Y: ")
lbl_paint_start_y.grid(row=1, column=0, padx=padx_const, sticky="WESN")

ent_paint_start_y = Entry(frm_paint_start, width=ent_width)
ent_paint_start_y.grid(row=1, column=1, padx=padx_const, sticky="WESN")

frm_paint_start.pack()


# _End_
frm_paint_end = LabelFrame(frm_paint_param, text="Конец отрезка")

lbl_paint_end_x = Label(frm_paint_end, text="X: ")
lbl_paint_end_x.grid(row=0, column=0, padx=padx_const, sticky="WESN")

ent_paint_end_x = Entry(frm_paint_end, width=ent_width)
ent_paint_end_x.grid(row=0, column=1, padx=padx_const, sticky="WESN")

lbl_paint_end_y = Label(frm_paint_end, text="Y: ")
lbl_paint_end_y.grid(row=1, column=0, padx=padx_const, sticky="WESN")

ent_paint_end_y = Entry(frm_paint_end, width=ent_width)
ent_paint_end_y.grid(row=1, column=1, padx=padx_const, sticky="WESN")

frm_paint_end.pack()


# _Methods_
frm_paint_methods = LabelFrame(frm_paint_param, text="Методы")
rbtn_method = [0] * len(method_name)

for i in range(len(method_name)):
    rbtn_method[i] = Radiobutton(frm_paint_methods, text=method_name[i], variable=meth_paint, value=i)
    rbtn_method[i].grid(row=i, column=0, sticky="W")

frm_paint_methods.pack()


# _Buttons_
frm_paint_button = Frame(frm_paint_param)

btn_paint_draw = Button(frm_paint_button, text="Нарисовать", command=paint_draw_line)
btn_paint_draw.grid(row=0, column=0, pady=1, sticky="WESN")

btn_paint_clear = Button(frm_paint_button, text="Очистить", command=paint_draw_clear)
btn_paint_clear.grid(row=1, column=0, pady=1, sticky="WESN")

frm_paint_button.pack()


# _Colors_
rbtn_paint_color = [0] * len(colors)

for i in range(len(colors)):
    rbtn_paint_color = Radiobutton(frm_paint_color, text=colors_name[i], variable=color_paint, value=i)
    rbtn_paint_color.grid(row=0, column=i, padx=3, sticky="WESN")

frm_paint_param.grid(row=0, rowspan=2, column=0, padx=1, pady=1, sticky="WESN")
frm_paint_color.grid(row=0, column=1, padx=1, pady=1, sticky="WESN")
frm_paint_draw.grid(row=1, column=1, padx=1, pady=1, sticky="WESN")



''' ### Analyse ### '''
# _Frames_
frm_analyse_param = LabelFrame(frm_analyse, text="Параметры")
frm_analyse_color = LabelFrame(frm_analyse, text="Цвета основных методов")
frm_analyse_draw = LabelFrame(frm_analyse, text="Изображение")


# _Canvas_
lbl_cnv_analyse_left_up = Label(frm_analyse_draw, text="(0; " + str(cnv_size[1]) + ")")
lbl_cnv_analyse_rigth_up = Label(frm_analyse_draw, text="(" + str(cnv_size[0]) + "; " + str(cnv_size[1]) + ")")
lbl_cnv_analyse_rigth_down = Label(frm_analyse_draw, text="(" + str(cnv_size[0]) + "; 0)")
lbl_cnv_analyse_left_down = Label(frm_analyse_draw, text="(0; 0)")

lbl_cnv_analyse_left_up.grid(row=0, column=0, sticky="WESN")
lbl_cnv_analyse_rigth_up.grid(row=0, column=2, sticky="WESN")

cnv_analyse_wall = Canvas(frm_analyse_draw, height=cnv_size[0], width=cnv_size[1], bg="white")
cnv_analyse_wall.grid(row=1, column=1, sticky="WESN")

lbl_cnv_analyse_left_down.grid(row=2, column=0, sticky="WESN")
lbl_cnv_analyse_rigth_down.grid(row=2, column=2, sticky="WESN")


# _Angle_
frm_analyse_angle = Frame(frm_analyse_param)

lbl_analyse_angle = Label(frm_analyse_angle, text="Угол:")
lbl_analyse_angle.grid(row=0, column=0, padx=1, pady=1, sticky="WESN")

ent_analyse_angle = Entry(frm_analyse_angle)
ent_analyse_angle.grid(row=0, column=1, padx=1, pady=1, sticky="WESN")

frm_analyse_angle.grid(row=0, column=0, sticky="WESN")


# _Methods_
frm_analyse_methods = LabelFrame(frm_analyse_param, text="Основные методы")
rbtn_analyse_methods = [0] * len(method_name)

for i in range(len(method_name)):
    rbtn_analyse_methods[i] = Radiobutton(frm_analyse_methods, text=method_name[i], variable=meth_analyse, value=i)
    rbtn_analyse_methods[i].grid(row=i, column=0, sticky="W")

frm_analyse_methods.grid(row=1, column=0, sticky="WESN")


# _Methods_bg_
frm_analyse_methods_bg = LabelFrame(frm_analyse_param, text="Методы для сравнения")
rbtn_analyse_methods_bg = [0] * (len(method_name) + 1)

for i in range(len(method_name) + 1):
    if i != len(method_name):
        rbtn_analyse_methods_bg[i] = Radiobutton(frm_analyse_methods_bg, text=method_name[i], variable=meth_bg_analyse, value=i)
        rbtn_analyse_methods_bg[i].grid(row=i, column=0, sticky="W")
    else:
        rbtn_analyse_methods_bg[i] = Radiobutton(frm_analyse_methods_bg, text="Не рисовать метод", variable=meth_bg_analyse, value=i)
        rbtn_analyse_methods_bg[i].grid(row=i, column=0, sticky="W")

frm_analyse_methods_bg.grid(row=2, column=0, sticky="WESN")


# _Buttons_
frm_analyse_button = Frame(frm_analyse_param)

btn_analyse_draw = Button(frm_analyse_button, text="Нарисовать", command=analyse_draw_line)
btn_analyse_draw.grid(row=0, column=0, padx=1, pady=1, sticky="WESN")

btn_analyse_clear = Button(frm_analyse_button, text="Очистить", command=analyse_draw_clear)
btn_analyse_clear.grid(row=1, column=0, padx=1, pady=1, sticky="WESN")

frm_analyse_button.grid(row=3, column=0, sticky="WESN")


# _Colors_
rbtn_analyse_color = [0] * len(colors)

for i in range(len(colors)):
    rbtn_analyse_color = Radiobutton(frm_analyse_color, text=colors_name[i], variable=color_analyse, value=i)
    rbtn_analyse_color.grid(row=0, column=i, padx=3, sticky="WESN")

frm_analyse_param.grid(row=0, column=0, rowspan=2, padx=1, pady=1, sticky="WESN")
frm_analyse_color.grid(row=0, column=1, padx=1, pady=1, sticky="WESN")
frm_analyse_draw.grid(row=1, column=1, padx=1, pady=1, sticky="WESN")


mainmenu = Menu(root)
root.config(menu=mainmenu)

modemenu = Menu(mainmenu, tearoff=0)
modemenu = Menu(mainmenu, tearoff=0)
modemenu.add_command(label="Рисование", command=construct_paint)
modemenu.add_command(label="Анализ", command=construct_analyse)
modemenu.add_command(label="Сравнение")

mainmenu.add_cascade(label="Режимы", menu=modemenu)

def main():
    construct_paint()

main()
root.mainloop()
