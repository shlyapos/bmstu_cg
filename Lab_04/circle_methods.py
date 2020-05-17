from math import sin, cos, pi, sqrt
from draw_options import *

angle_step = 0.1



''' ##### Drawing ##### '''
def circle_draw_kanon(cnt, r, color, wall):
    x = -r;
    while x <= r:
        crd = sqrt(r * r - x * x)
        draw_pixel(cnt[0] + x, cnt[1] + crd, color, wall)
        draw_pixel(cnt[0] + x, cnt[1] - crd, color, wall)
        draw_pixel(cnt[0] + crd, cnt[1] + x, color, wall)
        draw_pixel(cnt[0] - crd, cnt[1] + x, color, wall)
        x += 1


def circle_draw_param(cnt, r, color, wall):
    l = round(pi * r / 2)   # Длина четверти
    for i in range(0, l + 1, 1):
        x = round(r * cos(i / r))
        y = round(r * sin(i / r))
        draw_pixel(cnt[0] + x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] + x, cnt[1] - y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] - y, color, wall)


def circle_draw_bresenham(cnt, r, color, wall):
    x = 0
    y = r
    delta = 1 - 2 * r
    err = 0
    while y >= 0:
        draw_pixel(cnt[0] + x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] + x, cnt[1] - y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] - y, color, wall)
        
        err = 2 * (delta + y) - 1

        if (delta < 0) and (err <= 0):
            x += 1
            delta += (2 * x) + 1
            continue
        if (delta > 0) and (err > 0):
            y -= 1
            delta -= (2 * y) + 1
            continue
        
        x += 1
        delta += 2 * (x - y)
        y -= 1


def circle_draw_middle_point(cnt, r, color, wall):
    x = 0
    y = r
    p = 5 / 4 - r   # (x + 1)^2 + (y - 1)^2 - r^2
    while True:
        draw_pixel(cnt[0] - x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] + x, cnt[1] - y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] - y, color, wall)
        draw_pixel(cnt[0] + x, cnt[1] + y, color, wall)

        draw_pixel(cnt[0] - y, cnt[1] + x, color, wall)
        draw_pixel(cnt[0] + y, cnt[1] - x, color, wall)
        draw_pixel(cnt[0] - y, cnt[1] - x, color, wall)
        draw_pixel(cnt[0] + y, cnt[1] + x, color, wall)

        x += 1

        if p < 0:   # Средняя точка внутри окр., ближе верхний пиксель, горизонт. шаг
            p += (2 * x) + 1
        else:       # Средняя точка вне окр., ближе диагональный пиксель, диагональный шаг
            p += (2 * x) - (2 * y) + 5
            y -= 1
        
        if x > y:
            break


def circle_draw_standart(center, r, color, wall):
    wall.create_oval(center[0] - r, center[1] - r, 
                     center[0] + r, center[1] + r, width=pxl_width, outline=color)



''' ##### Time analyse ##### '''
def circle_draw_kanon_time(center, r):
    x = 0
    while x <= r:
        y = sqrt(r ** 2 - x ** 2)
        x += 1
    
    y = 0
    while y <= r:
        x = sqrt(r ** 2 - y ** 2)
        y += 1


def circle_draw_param_time(center, r):
    l = round(pi * r / 2)   # Длина четверти окружности
    for i in range(0, l + 1, 1):
        x = round(r * cos(i / r))
        y = round(r * sin(i / r))


def circle_draw_bresenham_time(center, r):
    x = 0
    y = r
    delta = 1 - 2 * r
    err = 0
    while y >= 0:
        err = 2 * (delta + y) - 1

        if (delta < 0) and (err <= 0):
            x += 1
            delta += (2 * x) + 1
            continue
        if (delta > 0) and (err > 0):
            y -= 1
            delta -= (2 * y) + 1
            continue
        
        x += 1
        delta += 2 * (x - y)
        y -= 1


def circle_draw_middle_point_time(center, r):
    x = 0
    y = r
    p = 5 / 4 - r
    while True:
        x += 1

        if p < 0:
            p += (2 * x) + 1
        else:
            p += (2 * x) - (2 * y) + 5
            y -= 1
        
        if x > y:
            break


def circle_draw_standart_time(center, r, color, wall):
    wall.create_oval(center[0] - r, center[1] - r, 
                     center[0] + r, center[1] + r, width=pxl_width, outline=color)



''' ##### Pickers ##### '''
def func_circle_picker(ind):
    if ind == 0:
        return circle_draw_kanon
    elif ind == 1:
        return circle_draw_param
    elif ind == 2:
        return circle_draw_bresenham
    elif ind == 3:
        return circle_draw_middle_point
    else:
        return circle_draw_standart


def func_circle_picker_time(ind):
    if ind == 0:
        return circle_draw_kanon_time
    elif ind == 1:
        return circle_draw_param_time
    elif ind == 2:
        return circle_draw_bresenham_time
    elif ind == 3:
        return circle_draw_middle_point_time
    else:
        return circle_draw_standart_time
