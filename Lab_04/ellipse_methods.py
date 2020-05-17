from math import sin, cos, pi, sqrt
from draw_options import *

angle_step = 0.1


''' ##### Drawing ##### '''
def ellipse_draw_kanon(cnt, a, b, color, wall):
    x = 0
    while x <= a:
        y = round(b * sqrt(1 - x ** 2 / a / a))

        draw_pixel(cnt[0] + x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] + x, cnt[1] - y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] - y, color, wall)

        x += 1
    
    y = 0
    while y <= b:
        x = round(a * sqrt(1 - y ** 2 / b / b))

        draw_pixel(cnt[0] + x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] + x, cnt[1] - y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] - y, color, wall)

        y += 1


def ellipse_draw_param(cnt, a, b, color, wall):
    m = max(a, b)
    l = round(pi * m / 2)
    for i in range(0, l + 1, 1):
        x = round(a * cos(i / m))
        y = round(b * sin(i / m))
        draw_pixel(cnt[0] + x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] + x, cnt[1] - y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] - y, color, wall)


def ellipse_draw_bresenham(cnt, a, b, color, wall):
    x = 0
    y = b
    a = a ** 2
    d = round((b * b / 2) - (a * b * 2) + (a / 2))
    b = b ** 2
    while y >= 0:
        draw_pixel(cnt[0] + x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] + x, cnt[1] - y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] - y, color, wall)

        if d < 0:   # пиксель лежит внутри эллипса
            buf = (2 * d) + (2 * a * y) - a
            x += 1
            if buf <= 0:    # Горизонтальный шаг
                d = d + (2 * b * x) + b
            else:           # Диагональный шаг
                y -= 1
                d = d + (2 * b * x) - (2 * a * y) + a + b
            continue
        if d > 0:   # Пиксель лежит вне эллипса
            buf = (2 * d) - (2 * b * x) - b
            y -= 1
            if buf > 0:     # Вертикальный шаг
                d = d - (2 * y * a) + a
            else:           # Диагональный шаг
                x += 1
                d = d + (2 * x * b) - (2 * y * a) + a + b
            continue
        if d == 0:  # Пиксель лежит на окружности
            x += 1  # Диагональный шаг
            y -= 1
            d = d + (2 * x * b) - (2 * y * a) + a + b


def ellipse_draw_middle_point(cnt, a, b, color, wall):
    x = 0
    y = b
    p = (b * b) - (a * a * b) + (0.25 * a * a)  # Начальное значение параметра принятия решения в области tg < 1
    while (2 * (b ** 2) * x) < (2 * a * a * y): # Пака тангенс угла наклона меньше 1
        draw_pixel(cnt[0] - x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] + x, cnt[1] - y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] - y, color, wall)
        draw_pixel(cnt[0] + x, cnt[1] + y, color, wall)

        x += 1

        if p < 0:   # Средняя точка внутри эллипса, ближе верхний пиксель, горизонтальный шаг
            p += (2 * b * b * x) + (b * b)
        else:       # Средняя точка вне эллипса, ближе диагональный пиксель, диагональный шаг
            y -= 1
            p += (2 * b * b * x) - (2 * a * a * y) + (b * b)
        
    p = (b * b * (x + 0.5) * (x + 0.5)) + ((a * a) * (y - 1) * (y - 1)) - (a * a * b * b)
    # Начальное значение параметра принятия решения в области tg > 1 в точке (x + 0.5, y - 1) последнего положения
    while y >= 0:
        draw_pixel(cnt[0] - x, cnt[1] + y, color, wall)
        draw_pixel(cnt[0] + x, cnt[1] - y, color, wall)
        draw_pixel(cnt[0] - x, cnt[1] - y, color, wall)
        draw_pixel(cnt[0] + x, cnt[1] + y, color, wall)

        y -= 1

        if p > 0:
            p -= (2 * a * a * y) + (a * a)
        else:
            x += 1
            p += (2 * b * b * x) - (2 * a * a * y) + (a * a)


def ellipse_draw_standart(center, a, b, color, wall):
    wall.create_oval(center[0] - a, center[1] - b,
                     center[0] + a, center[1] + b, width=pxl_width, outline=color)



''' ##### Time analyse ##### '''                   
def ellipse_draw_kanon_time(cnt, a, b):
    x = 0
    while x <= a:
        y = round(b * sqrt(1 - x ** 2 / a / a))
        x += 1
    
    y = 0
    while y <= b:
        x = round(a * sqrt(1 - y ** 2 / b / b))
        y += 1


def ellipse_draw_param_time(cnt, a, b):
    m = max(a, b)
    l = round(pi * m / 2)
    for i in range(0, l + 1, 1):
        x = round(a * cos(i / m))
        y = round(b * sin(i / m))


def ellipse_draw_bresenham_time(cnt, a, b):
    x = 0   # Начальное значение
    y = b
    a = a ** 2
    d = round(b * b / 2 - (a * b * 2) + a / 2)
    b = b ** 2
    while y >= 0:
        if d < 0:   # Пиксель внутри эллипса
            buf = (2 * d) + (2 * a * y) - a
            x += 1
            if buf <= 0:    # Горизонтальный шаг
                d = d + (2 * b * x) + b
            else:
                y -= 1
                d = d + (2 * b * x) - (2 * a * y) + a + b
            continue
        if d > 0:   # Пиксель лежит вне эллипса
            buf = (2 * d) - (2 * b * x) - b
            y -= 1
            if buf > 0: # Вертикальный шаг
                d = d - (2 * y * a) + a
            else:       # Диагональный шаг
                x += 1
                d = d + (2 * x * b) - (2 * y * a) + a + b
            continue
        if d == 0.0:    # Пиксель лежит на окружности
            x += 1
            y -= 1
            d = d + (2 * x * b) - (2 * y * a) + a + b


    '''
    x = 0
    y = b
    a = a ** 2
    d = (b * b / 2) - (a * b * 2) + (a / 2)
    b = b ** 2
    while y >= 0:
        if d < 0:   # пиксель лежит внутри эллипса
            buf = (2 * d) + (2 * a * y) - a
            x += 1
            if buf <= 0:    # Горизонтальный шаг
                d = d + (2 * b * x) + b
            else:           # Диагональный шаг
                y -= 1
                d = d + (2 * b * x) - (2 * a * y) + a + b
            continue
        if d > 0:   # Пиксель лежит вне эллипса
            buf = (2 * d) - (2 * b * x) - b
            y -= 1
            if buf > 0:     # Вертикальный шаг
                d = d - (2 * y * a) + a
            else:           # Диагональный шаг
                x += 1
                d = d + (2 * x * b) - (2 * y * a) + a + b
            continue
        if d == 0:  # Пиксель лежит на окружности
            x += 1  # Диагональный шаг
            y -= 1
            d = d + (2 * x * b) - (2 * y * a) + a + b
    '''


def ellipse_draw_middle_point_time(cnt, a, b):
    x = 0
    y = b
    p = (b * b) - (a * a * b) + (0.25 * a * a)  # Начальное значение параметра принятия решения в области tg < 1
    while (2 * (b ** 2) * x) < (2 * a * a * y): # Пака тангенс угла наклона меньше 1
        x += 1

        if p < 0:   # Средняя точка внутри эллипса, ближе верхний пиксель, горизонтальный шаг
            p += (2 * b * b * x) + (b * b)
        else:       # Средняя точка вне эллипса, ближе диагональный пиксель, диагональный шаг
            y -= 1
            p += (2 * b * b * x) - (2 * a * a * y) + (b * b)
        
    p = (b * b * (x + 0.5) * (x + 0.5)) + ((a * a) * (y - 1) * (y - 1)) - (a * a * b * b)
    # Начальное значение параметра принятия решения в области tg > 1 в точке (x + 0.5, y - 1) последнего положения
    while y >= 0:
        y -= 1

        if p > 0:
            p -= (2 * a * a * y) + (a * a)
        else:
            x += 1
            p += (2 * b * b * x) - (2 * a * a * y) + (a * a)


def ellipse_draw_standart_time(center, a, b, color, wall):
    wall.create_oval(center[0] - a, center[1] - b,
                     center[0] + a, center[1] + b, outline=color)
                     # center[0] + a, center[1] + b, width=pxl_width, outline=color)



''' ##### Func pickers ##### '''
def func_ellipse_picker(ind):
    if ind == 0:
        return ellipse_draw_kanon
    elif ind == 1:
        return ellipse_draw_param
    elif ind == 2:
        return ellipse_draw_bresenham
    elif ind == 3:
        return ellipse_draw_middle_point
    else:
        return ellipse_draw_standart


def func_ellipse_picker_time(ind):
    if ind == 0:
        return ellipse_draw_kanon_time
    elif ind == 1:
        return ellipse_draw_param_time
    elif ind == 2:
        return ellipse_draw_bresenham_time
    elif ind == 3:
        return ellipse_draw_middle_point_time
    else:
        return ellipse_draw_standart_time