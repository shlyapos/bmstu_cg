from tkinter import Tk, LabelFrame, Frame, Label, Button, Entry, IntVar, Canvas, Radiobutton, Menu, ALL
from tkinter import messagebox as mb, messagebox
from math import sin, cos, pi, sqrt

import matplotlib.pyplot as plt
import time

from circle_methods import *
from ellipse_methods import *

root = Tk(className="Построение окружностей и эллипсов")

frm_circle = LabelFrame(root, text="Рисование окружностей")
frm_ellipse = LabelFrame(root, text="Рисование эллипсов")
frm_analyse_circle = LabelFrame(root, text="Анализ методов рисования окружностей")
frm_analyse_ellipse = LabelFrame(root, text="Анализ методов рисования эллипсов")


# _Service_parameters_
cnv_size = [500, 500]

# For radiobutton
# For circle
circle_meth = IntVar()
circle_meth.set(0)
circle_col = IntVar()
circle_col.set(0)
# For ellipse
ellipse_meth = IntVar()
ellipse_meth.set(0)
ellipse_col = IntVar()
ellipse_col.set(0)
# For analyse circle
analyse_circle_meth = IntVar()
analyse_circle_meth.set(0)
analyse_circle_meth_bg = IntVar()
analyse_circle_meth_bg.set(0)
analyse_circle_col = IntVar()
analyse_circle_col.set(0)
# For analyse ellipse
analyse_ellipse_meth = IntVar()
analyse_ellipse_meth.set(0)
analyse_ellipse_meth_bg = IntVar()
analyse_ellipse_meth_bg.set(0)
analyse_ellipse_col = IntVar()
analyse_ellipse_col.set(0)
# Useless canvas I do not know how to do it better :(
cnv_tmp = Canvas(root, height=0, width=0)

method_list = ["Каноническое уравнение",
               "Параметрическое уравнение",
               "Алгоритм Брезенхема",
               "Алгоритм средней точки",
               "Библиотечная функция"]
color_list = ["#000",
              "#f00",
              "#0f0",
              "#00f"]
color_name = ["Чёрный",
              "Красный",
              "Зелёный",
              "Голубой"]


def destruct_all():
    frm_circle.pack_forget()
    frm_ellipse.pack_forget()
    frm_analyse_circle.pack_forget()
    frm_analyse_ellipse.pack_forget()


def func_useless():
    pass


def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0



def circle_frame_construct():
    destruct_all()
    frm_circle.pack()


def circle_draw():
    color = color_list[circle_col.get()]

    try:
        x = float(ent_circle_center_x.get())
        y = float(ent_circle_center_y.get())
        r = float(ent_circle_rad.get())
    except:
        messagebox.showerror("Ошибка", "Введены пустые или некорректные данные")
        return

    center = [x, y]

    if (circle_meth.get() == 0):
        print("Kanon")
        circle_draw_kanon(center, r, color, cnv_circle_wall)
    elif (circle_meth.get() == 1):
        print("Param")
        circle_draw_param(center, r, color, cnv_circle_wall)
    elif (circle_meth.get() == 2):
        print("Bresenham")
        circle_draw_bresenham(center, r, color, cnv_circle_wall)
    elif (circle_meth.get() == 3):
        print("Middle point")
        circle_draw_middle_point(center, r, color, cnv_circle_wall)
    else:
        print("Standart")
        circle_draw_standart(center, r, color, cnv_circle_wall)


def circle_clear():
    cnv_circle_wall.delete(ALL)



def circle_analyse_frame_constructor():
    destruct_all()
    frm_analyse_circle.pack()


def circle_analyse_draw():
    color = color_list[analyse_circle_col.get()]

    try:
        x = float(ent_analyse_circle_center_x.get())
        y = float(ent_analyse_circle_center_y.get())
        rs = float(ent_analyse_circle_rs.get())
        rf = float(ent_analyse_circle_rf.get())
        cnt = float(ent_analyse_circle_cnt.get())
    except:
        messagebox.showerror("Ошибка", "Введены пустые или некорректные данные")
        return
    
    center = [x, y]
    step = (rf - rs) / cnt
    r = rs

    func_main = func_circle_picker(analyse_circle_meth.get())

    if (analyse_circle_meth_bg.get() == len(method_list)):
        func_bg = func_useless
    else:
        func_bg = func_circle_picker(analyse_circle_meth_bg.get())

    while r < rf:
        func_main(center, r, color, cnv_analyse_circle_wall)

        if (analyse_circle_meth_bg.get() != len(method_list)):
            func_bg(center, r, "white", cnv_analyse_circle_wall)

        r += step
    

def circle_analyse_clear():
    cnv_analyse_circle_wall.delete(ALL)


def circle_time_analyse():
    meth_c = ["black", "red", "green", "blue", "yellow"]
    radius = list()
    ftime = list()

    for i in range(len(method_list)):
        func = func_circle_picker_time(i)
        for r in range(1000, 11000, 1000):
            radius.append(r)
            if i != len(method_list) - 1:
                start = time.time()
                func([0, 0], r)
                result = time.time() - start
            else:
                start = time.time()
                func([0, 0], r, "white", cnv_tmp)
                result = time.time() - start
            ftime.append(result)

        plt.plot(radius, ftime, label=method_list[i], c=meth_c[i])
        radius.clear()
        ftime.clear()

    plt.xlabel("Радиус")
    plt.ylabel("Время")
    plt.legend()
    plt.show()
    




def ellipse_frame_contruct():
    destruct_all()
    frm_ellipse.pack()


def ellipse_draw():
    color = color_list[ellipse_col.get()]

    try:
        x = float(ent_ellipse_center_x.get())
        y = float(ent_ellipse_center_y.get())
        rx = float(ent_ellipse_rad_x.get())
        ry = float(ent_ellipse_rad_y.get())
    except:
        messagebox.showerror("Ошибка", "Введены пустые или некорректные данные")
        return

    center = [x, y]

    if (ellipse_meth.get() == 0):
        print("Kanon")
        ellipse_draw_kanon(center, rx, ry, color, cnv_ellipse_wall)
    elif (ellipse_meth.get() == 1):
        print("Param")
        ellipse_draw_param(center, rx, ry, color, cnv_ellipse_wall)
    elif (ellipse_meth.get() == 2):
        print("Bresenham")
        ellipse_draw_bresenham(center, rx, ry, color, cnv_ellipse_wall)
    elif (ellipse_meth.get() == 3):
        print("Middle point")
        ellipse_draw_middle_point(center, rx, ry, color, cnv_ellipse_wall)
    else:
        print("Standart")
        ellipse_draw_standart(center, rx, ry, color, cnv_ellipse_wall)


def ellipse_clear():
    cnv_ellipse_wall.delete(ALL)



def ellipse_analyse_frame_constructor():
    destruct_all()
    frm_analyse_ellipse.pack()


def ellipse_analyse_draw():
    color = color_list[analyse_ellipse_col.get()]

    try:
        x = float(ent_analyse_ellipse_center_x.get())
        y = float(ent_analyse_ellipse_center_y.get())
        rs_x = float(ent_analyse_ellipse_rs_x.get())
        rs_y = float(ent_analyse_ellipse_rs_y.get())
        rf_x = float(ent_analyse_ellipse_rf_x.get())
        rf_y = float(ent_analyse_ellipse_rf_y.get())
        cnt = float(ent_analyse_ellipse_cnt.get())
    except:
        messagebox.showerror("Ошибка", "Введены пустые или некорректные данные")
        return
    
    center = [x, y]
    step_a = (rf_x - rs_x) / cnt
    step_b = (rf_y - rs_y) / cnt
    a = rs_x
    b = rs_y

    func_main = func_ellipse_picker(analyse_ellipse_meth.get())

    if (analyse_ellipse_meth_bg.get() == len(method_list)):
        func_bg = func_useless
    else:
        func_bg = func_ellipse_picker(analyse_ellipse_meth_bg.get())

    while (a < rf_x) and (b < rf_y):
        func_main(center, a, b, color, cnv_analyse_ellipse_wall)

        if (analyse_ellipse_meth_bg.get() != len(method_list)):
            func_bg(center, a, b, "white", cnv_analyse_ellipse_wall)

        a += step_a
        b += step_b


def ellipse_analyse_clear():
    cnv_analyse_ellipse_wall.delete(ALL)


def ellipse_time_analyse():
    meth_c = ["black", "red", "green", "blue", "yellow"]
    radius = list()
    ftime = list()

    for i in range(len(method_list)):
        func = func_ellipse_picker_time(i)
        a = 500
        b = 1000
        while (b <= 11000) and (a <= 5500):
            radius.append(a)
            if i != len(method_list) - 1:
                start = time.time()
                func([0, 0], a, b)
                result = time.time() - start
            else:
                start = time.time()
                func([0, 0], a, b, "white", cnv_tmp)
                result = time.time() - start
            ftime.append(result)
            a += 500
            b += 1000
        plt.plot(radius, ftime, label=method_list[i], c=meth_c[i])
        radius.clear()
        ftime.clear()
    plt.xlabel("Радиус")
    plt.ylabel("Время")
    plt.legend()
    plt.show()




'''
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
'''
''' #### _Circle_ #### '''
frm_circle_option = LabelFrame(frm_circle, text="Параметры")
frm_circle_method = LabelFrame(frm_circle, text="Методы")
frm_circle_button = Frame(frm_circle)
frm_circle_colors = LabelFrame(frm_circle, text="Цвет")
frm_circle_canvas = LabelFrame(frm_circle, text="Изображение")


# _Canvas_ #
lbl_cnv_circle_lu = Label(frm_circle_canvas, text="(0; " + str(cnv_size[1]) + ")")
lbl_cnv_circle_ru = Label(frm_circle_canvas, text="(" + str(cnv_size[0]) + "; " + str(cnv_size[1]) + ")")
lbl_cnv_circle_rd = Label(frm_circle_canvas, text="(" + str(cnv_size[0]) + "; 0)")
lbl_cnv_circle_ld = Label(frm_circle_canvas, text="(0; 0)")

lbl_cnv_circle_lu.grid(row=0, column=0, sticky="WESN")
lbl_cnv_circle_ru.grid(row=0, column=2, sticky="WESN")

cnv_circle_wall = Canvas(frm_circle_canvas, height=cnv_size[0], width=cnv_size[1], bg="white")
cnv_circle_wall.grid(row=1, column=1, sticky="WESN")

lbl_cnv_circle_ld.grid(row=2, column=0, sticky="WESN")
lbl_cnv_circle_rd.grid(row=2, column=2, sticky="WESN")


# _Colors_
rbtn_circle_color = [0] * len(color_list)

for i in range(len(color_list)):
    rbtn_circle_color = Radiobutton(frm_circle_colors, text=color_name[i], variable=circle_col, value=i)
    rbtn_circle_color.grid(row=0, column=i, padx=3, pady=1, sticky="WESN")


# _Circle_options_
frm_circle_option = LabelFrame(frm_circle, text="Параметры окружности")

lbl_circle_center_h = Label(frm_circle_option, text="Координаты центра:")
lbl_circle_center_h.grid(row=0, column=0, columnspan=2, padx=1, pady=1, sticky="WESN")

lbl_circle_center_x = Label(frm_circle_option, text="X:")
lbl_circle_center_x.grid(row=1, column=0, sticky="E")

ent_circle_center_x = Entry(frm_circle_option)
ent_circle_center_x.insert(0, str(cnv_size[0] // 2))
ent_circle_center_x.grid(row=1, column=1, padx=4, pady=2, sticky="WESN")

lbl_circle_center_y = Label(frm_circle_option, text="Y:")
lbl_circle_center_y.grid(row=2, column=0, sticky="E")

ent_circle_center_y = Entry(frm_circle_option)
ent_circle_center_y.insert(0, str(cnv_size[1] // 2))
ent_circle_center_y.grid(row=2, column=1, padx=4, pady=2, sticky="WESN")

lbl_circle_rad = Label(frm_circle_option, text="Радиус:")
lbl_circle_rad.grid(row=3, column=0, columnspan=2, padx=1, pady=1, sticky="WESN")

ent_circle_rad = Entry(frm_circle_option)
ent_circle_rad.grid(row=4, column=1, padx=4, pady=2, sticky="WESN")

frm_circle_option.pack()


# _Methods_
rbtn_circle_method = [0] * len(method_list)

for i in range(len(method_list)):
    rbtn_circle_method[i] = Radiobutton(frm_circle_method, text=method_list[i], variable=circle_meth, value=i)
    rbtn_circle_method[i].grid(row=i, column=0, sticky="W")


# _Buttons_
btn_circle_draw = Button(frm_circle_button, text="Нарисовать", command=circle_draw)
btn_circle_draw.grid(row=0, column=0, padx=2, pady=2, sticky="WESN")

btn_circle_clear = Button(frm_circle_button, text="Очистить", command=circle_clear)
btn_circle_clear.grid(row=1, column=0, padx=2, pady=2, sticky="WESN")

btn_circle_time_analyse = Button(frm_circle_button, text="Анализ времени", command=circle_time_analyse)
btn_circle_time_analyse.grid(row=2, column=0, padx=2, pady=2, sticky="WESN")


frm_circle_option.grid(row=0, column=0, sticky="WESN")
frm_circle_method.grid(row=1, column=0, sticky="WESN")
frm_circle_button.grid(row=2, column=0, sticky="WESN")
frm_circle_colors.grid(row=0, column=1, sticky="WESN")
frm_circle_canvas.grid(row=1, column=1, rowspan=2, sticky="WESN")
'''
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
'''
''' #### _Ellipse_ #### '''
frm_ellipse_option = LabelFrame(frm_ellipse, text="Параметры")
frm_ellipse_method = LabelFrame(frm_ellipse, text="Методы")
frm_ellipse_button = Frame(frm_ellipse)
frm_ellipse_colors = LabelFrame(frm_ellipse, text="Цвет")
frm_ellipse_canvas = LabelFrame(frm_ellipse, text="Изображение")


# _Canvas_
lbl_cnv_ellipse_lu = Label(frm_ellipse_canvas, text="(0; " + str(cnv_size[1]) + ")")
lbl_cnv_ellipse_ru = Label(frm_ellipse_canvas, text="(" + str(cnv_size[0]) + "; " + str(cnv_size[1]) + ")")
lbl_cnv_ellipse_rd = Label(frm_ellipse_canvas, text="(" + str(cnv_size[0]) + "; 0)")
lbl_cnv_ellipse_ld = Label(frm_ellipse_canvas, text="(0; 0)")

lbl_cnv_ellipse_lu.grid(row=0, column=0, sticky="WESN")
lbl_cnv_ellipse_ru.grid(row=0, column=2, sticky="WESN")

cnv_ellipse_wall = Canvas(frm_ellipse_canvas, height=cnv_size[0], width=cnv_size[1], bg="white")
cnv_ellipse_wall.grid(row=1, column=1, sticky="WESN")

lbl_cnv_ellipse_ld.grid(row=2, column=0, sticky="WESN")
lbl_cnv_ellipse_rd.grid(row=2, column=2, sticky="WESN")


# _Colors_
rbtn_ellipse_color = [0] * len(color_list)

for i in range(len(color_list)):
    rbtn_ellipse_color = Radiobutton(frm_ellipse_colors, text=color_name[i], variable=ellipse_col, value=i)
    rbtn_ellipse_color.grid(row=0, column=i, padx=3, pady=1, sticky="WESN")


# _Ellipse_options_
frm_ellipse_option = LabelFrame(frm_ellipse, text="Параметры окружности")

lbl_ellipse_center_h = Label(frm_ellipse_option, text="Координаты центра:")
lbl_ellipse_center_h.grid(row=0, column=0, columnspan=2, padx=1, pady=2, sticky="WESN")

lbl_ellipse_center_x = Label(frm_ellipse_option, text="X:")
lbl_ellipse_center_x.grid(row=1, column=0, sticky="E")

ent_ellipse_center_x = Entry(frm_ellipse_option)
ent_ellipse_center_x.insert(0, str(cnv_size[0] // 2))
ent_ellipse_center_x.grid(row=1, column=1, padx=4, pady=2, sticky="WESN")

lbl_ellipse_center_y = Label(frm_ellipse_option, text="Y:")
lbl_ellipse_center_y.grid(row=2, column=0, sticky="E")

ent_ellipse_center_y = Entry(frm_ellipse_option)
ent_ellipse_center_y.insert(0, str(cnv_size[1] // 2))
ent_ellipse_center_y.grid(row=2, column=1, padx=4, pady=2, sticky="WESN")

lbl_ellipse_rad_h = Label(frm_ellipse_option, text="Радиусы:")
lbl_ellipse_rad_h.grid(row=3, column=0, sticky="WESN")

lbl_ellipse_rad_x = Label(frm_ellipse_option, text="По X:")
lbl_ellipse_rad_x.grid(row=4, column=0, padx=1, pady=2, sticky="E")

ent_ellipse_rad_x = Entry(frm_ellipse_option)
ent_ellipse_rad_x.grid(row=4, column=1, padx=4, pady=2, sticky="WESN")

lbl_ellipse_rad_y = Label(frm_ellipse_option, text="По Y:")
lbl_ellipse_rad_y.grid(row=5, column=0, padx=1, pady=2, sticky="E")

ent_ellipse_rad_y = Entry(frm_ellipse_option)
ent_ellipse_rad_y.grid(row=5, column=1, padx=4, pady=2, sticky="WESN")

frm_ellipse_option.pack()


# _Methods_
rbtn_ellipse_method = [0] * len(method_list)

for i in range(len(method_list)):
    rbtn_ellipse_method[i] = Radiobutton(frm_ellipse_method, text=method_list[i], variable=ellipse_meth, value=i)
    rbtn_ellipse_method[i].grid(row=i, column=0, sticky="W")


# _Buttons_
btn_ellipse_draw = Button(frm_ellipse_button, text="Нарисовать", command=ellipse_draw)
btn_ellipse_draw.grid(row=0, column=0, padx=2, pady=2, sticky="WESN")

btn_ellipse_clear = Button(frm_ellipse_button, text="Очистить", command=ellipse_clear)
btn_ellipse_clear.grid(row=1, column=0, padx=2, pady=2, sticky="WESN")

btn_ellipse_time_analyse = Button(frm_ellipse_button, text="Анализ времени", command=ellipse_time_analyse)
btn_ellipse_time_analyse.grid(row=2, column=0, padx=2, pady=2, sticky="WESN")


frm_ellipse_option.grid(row=0, column=0, sticky="WESN")
frm_ellipse_method.grid(row=1, column=0, sticky="WESN")
frm_ellipse_button.grid(row=2, column=0, sticky="WESN")
frm_ellipse_colors.grid(row=0, column=1, sticky="WESN")
frm_ellipse_canvas.grid(row=1, column=1, rowspan=2, sticky="WESN")
'''
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
'''
''' #### _Analyse_circle_ #### '''
frm_analyse_circle_option = LabelFrame(frm_analyse_circle, text="Параметры")
frm_analyse_circle_method = LabelFrame(frm_analyse_circle, text="Основные методы")
frm_analyse_circle_method_bg = LabelFrame(frm_analyse_circle, text="Методы для сравнения")
frm_analyse_circle_button = Frame(frm_analyse_circle)
frm_analyse_circle_colors = LabelFrame(frm_analyse_circle, text="Цвета для основных методов")
frm_analyse_circle_canvas = LabelFrame(frm_analyse_circle, text="Изображение")


# _Canvas_
lbl_cnv_analyse_circle_lu = Label(frm_analyse_circle_canvas, text="(0; " + str(cnv_size[1]) + ")")
lbl_cnv_analyse_circle_ru = Label(frm_analyse_circle_canvas, text="(" + str(cnv_size[0]) + "; " + str(cnv_size[1]) + ")")
lbl_cnv_analyse_circle_rd = Label(frm_analyse_circle_canvas, text="(" + str(cnv_size[0]) + "; 0)")
lbl_cnv_analyse_circle_ld = Label(frm_analyse_circle_canvas, text="(0; 0)")

lbl_cnv_analyse_circle_lu.grid(row=0, column=0, sticky="WESN")
lbl_cnv_analyse_circle_ru.grid(row=0, column=2, sticky="WESN")

cnv_analyse_circle_wall = Canvas(frm_analyse_circle_canvas, height=cnv_size[0], width=cnv_size[1], bg="white")
cnv_analyse_circle_wall.grid(row=1, column=1, sticky="WESN")

lbl_cnv_analyse_circle_ld.grid(row=2, column=0, sticky="WESN")
lbl_cnv_analyse_circle_rd.grid(row=2, column=2, sticky="WESN")


# _Colors_
rbtn_analyse_circle_color = [0] * len(color_list)

for i in range(len(color_list)):
    rbtn_analyse_circle_color[i] = Radiobutton(frm_analyse_circle_colors, text=color_name[i], variable=analyse_circle_col, value=i)
    rbtn_analyse_circle_color[i].grid(row=0, column=i, padx=2, pady=2, sticky="WESN")


# _Options_
lbl_analyse_circle_center_h = Label(frm_analyse_circle_option, text="Координаты центра:")
lbl_analyse_circle_center_h.grid(row=0, column=0, columnspan=2, padx=1, pady=2, sticky="W")

# _X_
lbl_analyse_circle_center_x = Label(frm_analyse_circle_option, text="X:")
lbl_analyse_circle_center_x.grid(row=1, column=0, padx=1, pady=2, sticky="E")

ent_analyse_circle_center_x = Entry(frm_analyse_circle_option)
ent_analyse_circle_center_x.grid(row=1, column=1, padx=1, pady=2, sticky="WESN")
ent_analyse_circle_center_x.insert(0, str(cnv_size[0] // 2))

# _Y_
lbl_analyse_circle_center_y = Label(frm_analyse_circle_option, text="Y:")
lbl_analyse_circle_center_y.grid(row=2, column=0, padx=1, pady=2, sticky="E")

ent_analyse_circle_center_y = Entry(frm_analyse_circle_option)
ent_analyse_circle_center_y.grid(row=2, column=1, padx=1, pady=2, sticky="WESN")
ent_analyse_circle_center_y.insert(0, str(cnv_size[1] // 2))

# _Start_Radius_
lbl_analyse_circle_rs = Label(frm_analyse_circle_option, text="Нач. радиус:")
lbl_analyse_circle_rs.grid(row=3, column=0, padx=1, pady=2, sticky="E")

ent_analyse_circle_rs = Entry(frm_analyse_circle_option)
ent_analyse_circle_rs.grid(row=3, column=1, padx=1, pady=2, sticky="WESN")

# _Finish_Radius_
lbl_analyse_circle_rf = Label(frm_analyse_circle_option, text="Кон. радиус:")
lbl_analyse_circle_rf.grid(row=4, column=0, padx=1, pady=2, sticky="E")

ent_analyse_circle_rf = Entry(frm_analyse_circle_option)
ent_analyse_circle_rf.grid(row=4, column=1, padx=1, pady=2, sticky="WESN")

# _Count_
lbl_analyse_circle_cnt = Label(frm_analyse_circle_option, text="Кол-во:")
lbl_analyse_circle_cnt.grid(row=5, column=0, padx=1, pady=2, sticky="E")

ent_analyse_circle_cnt = Entry(frm_analyse_circle_option)
ent_analyse_circle_cnt.grid(row=5, column=1, padx=1, pady=2, sticky="WESN")


# _Methods_
rbtn_analyse_circle_method = [0] * len(method_list)

for i in range(len(method_list)):
    rbtn_analyse_circle_method[i] = Radiobutton(frm_analyse_circle_method, text=method_list[i], variable=analyse_circle_meth, value=i)
    rbtn_analyse_circle_method[i].grid(row=i, column=0, sticky="W")


# _Methods_bg_
rbtn_analyse_circle_method_bg = [0] * (len(method_list) + 1)

for i in range(len(method_list) + 1):
    if i == len(method_list):
        rbtn_analyse_circle_method_bg[i] = Radiobutton(frm_analyse_circle_method_bg, text="Не рисовать", variable=analyse_circle_meth_bg, value=i)
        rbtn_analyse_circle_method_bg[i].grid(row=i, column=0, sticky="W")
    else:
        rbtn_analyse_circle_method_bg[i] = Radiobutton(frm_analyse_circle_method_bg, text=method_list[i], variable=analyse_circle_meth_bg, value=i)
        rbtn_analyse_circle_method_bg[i].grid(row=i, column=0, sticky="W")


# _Buttons_
btn_analyse_circle_draw = Button(frm_analyse_circle_button, text="Нарисовать", command=circle_analyse_draw)
btn_analyse_circle_draw.grid(row=0, column=0, padx=2, pady=2, sticky="WESN")

btn_analyse_circle_clear = Button(frm_analyse_circle_button, text="Очистить", command=circle_analyse_clear)
btn_analyse_circle_clear.grid(row=1, column=0, padx=2, pady=2, sticky="WESN")


frm_analyse_circle_option.grid(row=0, column=0, padx=1, pady=1, sticky="WESN")
frm_analyse_circle_method.grid(row=1, column=0, padx=1, pady=1, sticky="WESN")
frm_analyse_circle_method_bg.grid(row=2, column=0, padx=1, pady=1, sticky="WESN")
frm_analyse_circle_button.grid(row=3, column=0, padx=1, pady=1, sticky="WESN")
frm_analyse_circle_colors.grid(row=0, column=1, padx=1, pady=1, sticky="WESN")
frm_analyse_circle_canvas.grid(row=1, column=1, rowspan=3, padx=1, pady=1, sticky="WESN")
'''
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
'''
''' #### _Analyse_ellipse_ #### '''
frm_analyse_ellipse_option = LabelFrame(frm_analyse_ellipse, text="Параметры")
frm_analyse_ellipse_method = LabelFrame(frm_analyse_ellipse, text="Основные методы")
frm_analyse_ellipse_method_bg = LabelFrame(frm_analyse_ellipse, text="Методы для сравнения")
frm_analyse_ellipse_button = Frame(frm_analyse_ellipse)
frm_analyse_ellipse_colors = LabelFrame(frm_analyse_ellipse, text="Цвета для основных методов")
frm_analyse_ellipse_canvas = LabelFrame(frm_analyse_ellipse, text="Изображение")


# _Canvas_
lbl_cnv_analyse_ellipse_lu = Label(frm_analyse_ellipse_canvas, text="(0; " + str(cnv_size[1]) + ")")
lbl_cnv_analyse_ellipse_ru = Label(frm_analyse_ellipse_canvas, text="(" + str(cnv_size[0]) + "; " + str(cnv_size[1]) + ")")
lbl_cnv_analyse_ellipse_rd = Label(frm_analyse_ellipse_canvas, text="(" + str(cnv_size[0]) + "; 0)")
lbl_cnv_analyse_ellipse_ld = Label(frm_analyse_ellipse_canvas, text="(0; 0)")

lbl_cnv_analyse_ellipse_lu.grid(row=0, column=0, sticky="WESN")
lbl_cnv_analyse_ellipse_ru.grid(row=0, column=2, sticky="WESN")

cnv_analyse_ellipse_wall = Canvas(frm_analyse_ellipse_canvas, height=cnv_size[0], width=cnv_size[1], bg="white")
cnv_analyse_ellipse_wall.grid(row=1, column=1, sticky="WESN")

lbl_cnv_analyse_ellipse_ld.grid(row=2, column=0, sticky="WESN")
lbl_cnv_analyse_ellipse_rd.grid(row=2, column=2, sticky="WESN")


# _Colors_
rbtn_analyse_ellipse_color = [0] * len(color_list)

for i in range(len(color_list)):
    rbtn_analyse_ellipse_color[i] = Radiobutton(frm_analyse_ellipse_colors, text=color_name[i], variable=analyse_ellipse_col, value=i)
    rbtn_analyse_ellipse_color[i].grid(row=0, column=i, padx=2, pady=2, sticky="WESN")


# _Options_
lbl_analyse_ellipse_center_h = Label(frm_analyse_circle_option, text="Координаты центра:")
lbl_analyse_ellipse_center_h.grid(row=0, column=0, columnspan=2, padx=1, pady=2, sticky="W")

# _X_
lbl_analyse_ellipse_center_x = Label(frm_analyse_ellipse_option, text="X:")
lbl_analyse_ellipse_center_x.grid(row=1, column=0, padx=1, pady=2, sticky="E")

ent_analyse_ellipse_center_x = Entry(frm_analyse_ellipse_option)
ent_analyse_ellipse_center_x.grid(row=1, column=1, padx=1, pady=2, sticky="WESN")
ent_analyse_ellipse_center_x.insert(0, str(cnv_size[0] // 2))

# _Y_
lbl_analyse_ellipse_center_y = Label(frm_analyse_ellipse_option, text="Y:")
lbl_analyse_ellipse_center_y.grid(row=2, column=0, padx=1, pady=2, sticky="E")

ent_analyse_ellipse_center_y = Entry(frm_analyse_ellipse_option)
ent_analyse_ellipse_center_y.grid(row=2, column=1, padx=1, pady=2, sticky="WESN")
ent_analyse_ellipse_center_y.insert(0, str(cnv_size[1] // 2))

# _Start_radius_X_
lbl_analyse_ellipse_rs_x = Label(frm_analyse_ellipse_option, text="Нач. полуось X:")
lbl_analyse_ellipse_rs_x.grid(row=3, column=0, padx=1, pady=2, sticky="E")

ent_analyse_ellipse_rs_x = Entry(frm_analyse_ellipse_option)
ent_analyse_ellipse_rs_x.grid(row=3, column=1, padx=1, pady=2, sticky="WESN")

# _Start_radius_Y_
lbl_analyse_ellipse_rs_y = Label(frm_analyse_ellipse_option, text="Нач. полуось Y:")
lbl_analyse_ellipse_rs_y.grid(row=4, column=0, padx=1, pady=2, sticky="E")

ent_analyse_ellipse_rs_y = Entry(frm_analyse_ellipse_option)
ent_analyse_ellipse_rs_y.grid(row=4, column=1, padx=1, pady=2, sticky="WESN")

# _Finish_radius_X_
lbl_analyse_ellipse_rf_x = Label(frm_analyse_ellipse_option, text="Кон. полуось X:")
lbl_analyse_ellipse_rf_x.grid(row=5, column=0, padx=1, pady=2, sticky="E")

ent_analyse_ellipse_rf_x = Entry(frm_analyse_ellipse_option)
ent_analyse_ellipse_rf_x.grid(row=5, column=1, padx=1, pady=2, sticky="WESN")

# _Finish_radius_Y_
lbl_analyse_ellipse_rf_y = Label(frm_analyse_ellipse_option, text="Кон. полуось Y:")
lbl_analyse_ellipse_rf_y.grid(row=6, column=0, padx=1, pady=2, sticky="E")

ent_analyse_ellipse_rf_y = Entry(frm_analyse_ellipse_option)
ent_analyse_ellipse_rf_y.grid(row=6, column=1, padx=1, pady=2, sticky="WESN")

# _Count_
lbl_analyse_ellipse_cnt = Label(frm_analyse_ellipse_option, text="Кол-во:")
lbl_analyse_ellipse_cnt.grid(row=7, column=0, padx=1, pady=2, sticky="E")

ent_analyse_ellipse_cnt = Entry(frm_analyse_ellipse_option)
ent_analyse_ellipse_cnt.grid(row=7, column=1, padx=1, pady=2, sticky="WESN")


# _Methods_
rbtn_analyse_ellipse_method = [0] * len(method_list)

for i in range(len(method_list)):
    rbtn_analyse_ellipse_method[i] = Radiobutton(frm_analyse_ellipse_method, text=method_list[i], variable=analyse_ellipse_meth, value=i)
    rbtn_analyse_ellipse_method[i].grid(row=i, column=0, sticky="W")


# _Methods_bg_
rbtn_analyse_ellipse_method_bg = [0] * (len(method_list) + 1)

for i in range(len(method_list) + 1):
    if i == len(method_list):
        rbtn_analyse_ellipse_method_bg[i] = Radiobutton(frm_analyse_ellipse_method_bg, text="Не рисовать", variable=analyse_ellipse_meth_bg, value=i)
        rbtn_analyse_ellipse_method_bg[i].grid(row=i, column=0, sticky="W")
    else:
        rbtn_analyse_ellipse_method_bg[i] = Radiobutton(frm_analyse_ellipse_method_bg, text=method_list[i], variable=analyse_ellipse_meth_bg, value=i)
        rbtn_analyse_ellipse_method_bg[i].grid(row=i, column=0, sticky="W")


# _Buttons_
btn_analyse_ellipse_draw = Button(frm_analyse_ellipse_button, text="Нарисовать", command=ellipse_analyse_draw)
btn_analyse_ellipse_draw.grid(row=0, column=0, padx=2, pady=2, sticky="WESN")

btn_analyse_ellipse_clear = Button(frm_analyse_ellipse_button, text="Очистить", command=ellipse_analyse_clear)
btn_analyse_ellipse_clear.grid(row=1, column=0, padx=2, pady=2, sticky="WESN")


frm_analyse_ellipse_option.grid(row=0, column=0, padx=1, pady=1, sticky="WESN")
frm_analyse_ellipse_method.grid(row=1, column=0, padx=1, pady=1, sticky="WESN")
frm_analyse_ellipse_method_bg.grid(row=2, column=0, padx=1, pady=1, sticky="WESN")
frm_analyse_ellipse_button.grid(row=3, column=0, padx=1, pady=1, sticky="WESN")
frm_analyse_ellipse_colors.grid(row=0, column=1, padx=1, pady=1, sticky="WESN")
frm_analyse_ellipse_canvas.grid(row=1, column=1, rowspan=3, padx=1, pady=1, sticky="WESN")
'''
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
'''

mainmenu = Menu(root)
root.config(menu=mainmenu)

mode_draw_menu = Menu(mainmenu, tearoff=0)
mode_draw_menu.add_command(label="Рисование окружностей", command=circle_frame_construct)
mode_draw_menu.add_command(label="Рисование эллипсов", command=ellipse_frame_contruct)

mode_analyse_menu = Menu(mainmenu, tearoff=0)
mode_analyse_menu.add_command(label="Анализ для окружностей", command=circle_analyse_frame_constructor)
mode_analyse_menu.add_command(label="Анализ для эллипсов", command=ellipse_analyse_frame_constructor)

mainmenu.add_cascade(label="Рисование", menu=mode_draw_menu)
mainmenu.add_cascade(label="Анализ методов", menu=mode_analyse_menu)

def main():
    circle_frame_construct()

main()
root.mainloop()