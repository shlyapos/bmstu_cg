from tkinter import Tk, Menu, LabelFrame, Frame, Label, Entry, Button, Canvas, ALL
from tkinter import messagebox as mb, messagebox

from math import sqrt, acos, pi

main_root = Tk(className="Geometry")

# Service parameters
cnv_size = [640, 480]
point_width = 5
bunch1 = list()
bunch2 = list()
x_axis = [100, 0]
txt_point1 = [0] * 3
txt_point2 = [0] * 3
triangle1 = [[0, 0]] * 3
triangle2 = [[0, 0]] * 3
ort1 = [0] * 2
ort2 = [0] * 2
line_width = 3
axis_width = 2


def init_point(point, index, frame):
    point[0] = LabelFrame(frame)
    point[1] = Label(point[0], text="Точка {:2d}:".format(index))
    point[2] = Entry(point[0], width=8)
    point[2].insert(0, '0')
    point[3] = Entry(point[0], width=8)
    point[3].insert(0, '0')
    point[4] = index

    return point


def add_point(point, index):
    point[1].grid(row=0, column=0, padx=5)
    point[2].grid(row=0, column=1, padx=5)
    point[3].grid(row=0, column=2, padx=5)
    point[0].pack()


def rem_point(point):
    point[1].destroy()
    point[2].destroy()
    point[3].destroy()
    point[0].destroy()

    return point


def take_point(index, coords):
    x = float(coords[index][2].get())
    #y = cnv_size[1] - float(coords[index][3].get())
    y = float(coords[index][3].get())

    return [x, y]



def add_point_bunch1():
    global bunch1
    bunch1.append([0, 0, 0, 0, 0])

    bunch1[len(bunch1) - 1] = init_point(bunch1[len(bunch1) - 1], len(bunch1), frm_bunch1_pnt)
    add_point(bunch1[len(bunch1) - 1], len(bunch1) - 1)


def rem_point_bunch1():
    global bunch1

    if (len(bunch1) == 3):
        messagebox.showerror("Error", "Количество точек не может быть меньше 3")
        return

    bunch1[len(bunch1) - 1] = rem_point(bunch1[len(bunch1) - 1])
    bunch1.pop()


def add_point_bunch2():
    global bunch2
    bunch2.append([0, 0, 0, 0, 0])

    bunch2[len(bunch2) - 1] = init_point(bunch2[len(bunch2) - 1], len(bunch2), frm_bunch2_pnt)
    add_point(bunch2[len(bunch2) - 1], len(bunch2) - 1)


def rem_point_bunch2():
    global bunch2

    if (len(bunch2) == 3):
        messagebox.showerror("Error", "Количество точек не может быть меньше 3")
        return
    
    bunch2[len(bunch2) - 1] = rem_point(bunch2[len(bunch2) - 1])
    bunch2.pop()



def len_calculate(p1, p2):
    lenght = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return lenght


def check_triangle(pnt1, pnt2, pnt3):
    a = len_calculate(pnt1, pnt2)
    b = len_calculate(pnt2, pnt3)
    c = len_calculate(pnt3, pnt1)

    if (((a + b) < c) or ((a + c) < b) or ((b + c) < a)):
        return False
    return True



def find_k(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def find_height_ort(p1, p2, p3):
    k1 = find_k(p1, p2)
    k2 = find_k(p2, p3)

    x = ((p1[1] - p3[1]) * k1 * k2 + k1 * p1[0] - k2 * p3[0]) / (k1 - k2)
    y = (-1 / k2) * (x - p1[0]) + p1[1]

    return x, y


def vector_axis_angle(vect):
    return acos(vect[0] / sqrt(vect[0]**2 + vect[1]**2)) * 180 / pi


def find_b(k, pnt):
    return pnt[1] - (k * pnt[0])


def find_height_crossing(p1, p2, p3):
    try:
        ks = find_k(p1, p2)
    except:
        return p1[0], p3[1]

    if (ks == 0):
        return p3[0], p1[1]

    kh = -1 / ks

    bs = find_b(ks, p1)
    bh = find_b(kh, p3)

    x = (bh - bs) / (ks - kh)
    y = ks * x + bs

    return x, y
    

def scaling(x_arr, y_arr):
    x_min = min(x_arr)
    x_max = max(x_arr)

    y_min = min(y_arr)
    y_max = max(y_arr)

    x_min -= (x_max - x_min) / 10
    x_max += (x_max - x_min) / 10
    y_min -= (y_max - y_min) / 10
    y_max += (y_max - y_min) / 10

    x_pixel = list()
    y_pixel = list()

    for i in range(len(x_arr)):
        x_pixel.append(cnv_size[0] * ((x_arr[i] - x_min) / (x_max - x_min)))
        y_pixel.append(cnv_size[1] * ((y_max - y_arr[i]) / (y_max - y_min)))

    return x_pixel, y_pixel


def draw_figure():
    cnv_wall.delete(ALL)

    x_array = [0]
    y_array = [0]

    # Triangle_1_[i = 1,2,3]
    for i in range(len(triangle1)):
        x_array.append(triangle1[i][0])
        y_array.append(triangle1[i][1])
    # Ortcenter [i = 4]
    x_array.append(ort1[0])
    y_array.append(ort1[1])


    # Осталось добавить точки пересечения высоты и стороны функция -> find_height_crossing
    # Heights [i=5,6,7]
    x_tmp, y_tmp = find_height_crossing(triangle1[0], triangle1[1], triangle1[2])
    x_array.append(x_tmp)
    y_array.append(y_tmp)

    x_tmp, y_tmp = find_height_crossing(triangle1[1], triangle1[2], triangle1[0])
    x_array.append(x_tmp)
    y_array.append(y_tmp)

    x_tmp, y_tmp = find_height_crossing(triangle1[2], triangle1[0], triangle1[1])
    x_array.append(x_tmp)
    y_array.append(y_tmp)


    # Triangle_1_[i = 8,9,10]
    for i in range(len(triangle2)):
        x_array.append(triangle2[i][0])
        y_array.append(triangle2[i][1])
    # Ortcenter [i = 11]
    x_array.append(ort2[0])
    y_array.append(ort2[1])

    # i = [12,13,14]
    x_tmp, y_tmp = find_height_crossing(triangle2[0], triangle2[1], triangle2[2])
    x_array.append(x_tmp)
    y_array.append(y_tmp)

    x_tmp, y_tmp = find_height_crossing(triangle2[1], triangle2[2], triangle2[0])
    x_array.append(x_tmp)
    y_array.append(y_tmp)

    x_tmp, y_tmp = find_height_crossing(triangle2[2], triangle2[0], triangle2[1])
    x_array.append(x_tmp)
    y_array.append(y_tmp)
    

    # Scaling picture
    x_scaled, y_scaled = scaling(x_array, y_array)

    ''' _Axis_ '''
    # X axis
    cnv_wall.create_line(0, y_scaled[0], x_scaled[0] + cnv_size[0], y_scaled[0], fill="blue", width=axis_width)
    cnv_wall.create_text(x_scaled[0], y_scaled[0], text="(0; 0)")
    # Y axis
    cnv_wall.create_line(x_scaled[0], 0, x_scaled[0], y_scaled[0] + cnv_size[1], fill="green", width=axis_width)


    ''' _Triangle_1_ '''
    # Triangle
    cnv_wall.create_line(x_scaled[1], y_scaled[1], x_scaled[2], y_scaled[2], width=line_width)
    if (triangle1[0] != [0, 0]):
        cnv_wall.create_text(x_scaled[1], y_scaled[1], text=txt_point1[0])

    cnv_wall.create_line(x_scaled[2], y_scaled[2], x_scaled[3], y_scaled[3], width=line_width)
    if (triangle1[1] != [0, 0]):
        cnv_wall.create_text(x_scaled[2], y_scaled[2], text=txt_point1[1])

    cnv_wall.create_line(x_scaled[3], y_scaled[3], x_scaled[1], y_scaled[1], width=line_width)
    if (triangle2[2] != [0, 0]):
        cnv_wall.create_text(x_scaled[3], y_scaled[3], text=txt_point1[2])

    # Heights
    cnv_wall.create_line(x_scaled[1], y_scaled[1], x_scaled[4], y_scaled[4], fill="steel blue", width=line_width)
    cnv_wall.create_line(x_scaled[5], y_scaled[5], x_scaled[4], y_scaled[4], fill="steel blue", width=line_width)

    cnv_wall.create_line(x_scaled[2], y_scaled[2], x_scaled[4], y_scaled[4], fill="steel blue", width=line_width)
    cnv_wall.create_line(x_scaled[6], y_scaled[6], x_scaled[4], y_scaled[4], fill="steel blue", width=line_width)

    cnv_wall.create_line(x_scaled[3], y_scaled[3], x_scaled[4], y_scaled[4], fill="steel blue", width=line_width)
    cnv_wall.create_line(x_scaled[7], y_scaled[7], x_scaled[4], y_scaled[4], fill="steel blue", width=line_width)


    ''' _Triangle_2_ '''
    # Triangle
    cnv_wall.create_line(x_scaled[8], y_scaled[8], x_scaled[9], y_scaled[9], width=line_width)
    if (triangle2[0] != [0, 0]):
        cnv_wall.create_text(x_scaled[8], y_scaled[8], text=txt_point2[0])

    cnv_wall.create_line(x_scaled[9], y_scaled[9], x_scaled[10], y_scaled[10], width=line_width)
    if (triangle2[1] != [0, 0]):
        cnv_wall.create_text(x_scaled[9], y_scaled[9], text=txt_point2[1])

    cnv_wall.create_line(x_scaled[10], y_scaled[10], x_scaled[8], y_scaled[8], width=line_width)
    if (triangle2[2] != [0, 0]):
        cnv_wall.create_text(x_scaled[10], y_scaled[10], text=txt_point2[2])

    # Heights
    cnv_wall.create_line(x_scaled[8], y_scaled[8], x_scaled[11], y_scaled[11], fill="steel blue", width=line_width)
    cnv_wall.create_line(x_scaled[12], y_scaled[12], x_scaled[11], y_scaled[11], fill="steel blue", width=line_width)

    cnv_wall.create_line(x_scaled[9], y_scaled[9], x_scaled[11], y_scaled[11], fill="steel blue", width=line_width)
    cnv_wall.create_line(x_scaled[13], y_scaled[13], x_scaled[11], y_scaled[11], fill="steel blue", width=line_width)

    cnv_wall.create_line(x_scaled[10], y_scaled[10], x_scaled[11], y_scaled[11], fill="steel blue", width=line_width)
    cnv_wall.create_line(x_scaled[14], y_scaled[14], x_scaled[11], y_scaled[11], fill="steel blue", width=line_width)

    ''' _Straight_ '''
    cnv_wall.create_line(x_scaled[4], y_scaled[4], x_scaled[11], y_scaled[11], fill="gold", width=line_width)

    ''' _Ortcenters_ '''
    # 1
    cnv_wall.create_oval(x_scaled[4], y_scaled[4], x_scaled[4], y_scaled[4], width=line_width + 2)
    # 2
    cnv_wall.create_oval(x_scaled[11], y_scaled[11], x_scaled[11], y_scaled[11], width=line_width + 2)



def start_search():
    global ort1
    global ort2
    global txt_point1
    global txt_point2
    global triangle1
    global triangle2

    counter = 0
    min_angle = 370

    for i1 in range(len(bunch1)):
        for j1 in range(len(bunch1)):
            if (i1 == j1):
                continue
            for k1 in range(len(bunch1)):
                if ((i1 == k1) or (j1 == k1)):
                    continue
                try:
                    b1_pnt1 = take_point(i1, bunch1)
                    b1_pnt2 = take_point(j1, bunch1)
                    b1_pnt3 = take_point(k1, bunch1)
                except:
                    messagebox.showerror("Error", "Введены некорректные координаты для точки")
                    return

                if (not(check_triangle(b1_pnt1, b1_pnt2, b1_pnt3))):
                    continue

                for i2 in range(len(bunch2)):
                    for j2 in range(len(bunch2)):
                        if (i2 == j2):
                            continue
                        for k2 in range(len(bunch2)):
                            if ((i2 == k2) or (j2 == k2)):
                                continue
                            try:
                                b2_pnt1 = take_point(i2, bunch2)
                                b2_pnt2 = take_point(j2, bunch2)
                                b2_pnt3 = take_point(k2, bunch2)
                            except:
                                messagebox.showerror("Error", "Введены некорректные координаты для точки")
                                return
                            
                            if (not(check_triangle(b2_pnt1, b2_pnt2, b2_pnt3))):
                                continue
                            
                            try:
                                b1_x, b1_y = find_height_ort(b1_pnt1, b1_pnt2, b1_pnt3)
                            except:
                                continue

                            try:
                                b2_x, b2_y = find_height_ort(b2_pnt1, b2_pnt2, b2_pnt3)
                            except:
                                continue

                            print("ort1 = ", b1_x, b1_y)
                            print("ort2 = ", b2_x, b2_y)

                            vector = [b2_x - b1_x, b2_y - b1_y]
                            angle = vector_axis_angle(vector)

                            if (angle < min_angle):
                                counter += 1
                                min_angle = angle
                                ort1 = [b1_x, b1_y]
                                ort2 = [b2_x, b2_y]
                                triangle1 = [b1_pnt1, b1_pnt2, b1_pnt3]
                                triangle2 = [b2_pnt1, b2_pnt2, b2_pnt3]
                                #txt_point1 = [bunch1[i1][4], bunch1[j1][4], bunch1[k1][4]]
                                #txt_point2 = [bunch2[i2][4], bunch2[j2][4], bunch2[k2][4]]
                                txt_point1 = ["({:3.2f};{:3.2f})".format(b1_pnt1[0], b1_pnt1[1]), 
                                              "({:3.2f};{:3.2f})".format(b1_pnt2[0], b1_pnt2[1]),
                                              "({:3.2f};{:3.2f})".format(b1_pnt3[0], b1_pnt3[1])]
                                txt_point2 = ["({:3.2f};{:3.2f})".format(b2_pnt1[0], b2_pnt1[1]), 
                                              "({:3.2f};{:3.2f})".format(b2_pnt2[0], b2_pnt2[1]),
                                              "({:3.2f};{:3.2f})".format(b2_pnt3[0], b2_pnt3[1])]
    '''
    print("triangle1 = ", triangle1)
    print("triangle1 = ", triangle2)

    print("\nort1 = ", ort1)
    print("ort2 = ", ort2)

    print("\ntxt_point1 = ", txt_point1)
    print("txt_point1 = ", txt_point2)
    '''

    if (counter == 0):
        messagebox.showerror("Error", "Треугольники не найдены")
        return
    
    cnv_wall.delete(ALL)
    draw_figure()



# Bunch_1____________________________________________
frm_bunch1 = LabelFrame(main_root, text="Множество 1")
frm_bunch1_pnt = Frame(frm_bunch1)
frm_bunch1_key = Frame(main_root)

btn_bunch1_add = Button(frm_bunch1_key, text='+', command=add_point_bunch1)
btn_bunch1_rem = Button(frm_bunch1_key, text='-', command=rem_point_bunch1)

btn_bunch1_add.grid(row=0, column=0, sticky="WESN", pady=5)
btn_bunch1_rem.grid(row=0, column=1, sticky="WESN", pady=5)

frm_bunch1_pnt.grid(row=0, column=0, sticky="WESN")
frm_bunch1.grid(row=0, column=0, sticky="WESN")
frm_bunch1_key.grid(row=1, column=0, sticky="WESN")


# Bunch_2____________________________________________
frm_bunch2 = LabelFrame(main_root, text="Множество 2")
frm_bunch2_pnt = Frame(frm_bunch2)
frm_bunch2_key = Frame(main_root)

btn_bunch2_add = Button(frm_bunch2_key, text='+', command=add_point_bunch2)
btn_bunch2_rem = Button(frm_bunch2_key, text='-', command=rem_point_bunch2)

btn_bunch2_add.grid(row=0, column=0, sticky="WESN", pady=5)
btn_bunch2_rem.grid(row=0, column=1, sticky="WESN", pady=5)

frm_bunch2_pnt.grid(row=0, column=0, sticky="WESN")
frm_bunch2.grid(row=0, column=1, sticky="WESN")
frm_bunch2_key.grid(row=1, column=1, sticky="WESN")


# Draw
frm_draw = LabelFrame(main_root, text="Изображение")

cnv_wall = Canvas(frm_draw, width=cnv_size[0], height=cnv_size[1], bg="white")
cnv_wall.pack()

frm_draw.grid(row=0, column=2, rowspan=2, sticky="WESN")


def main():
    global bunch1
    global bunch2

    for i in range(3):
        add_point_bunch1()
        add_point_bunch2()


main()

start_menu = Menu(main_root, tearoff=0)
main_root.config(menu=start_menu)
start_menu.add_command(label="Запустить", command=start_search)

main_root.mainloop()