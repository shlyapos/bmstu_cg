pxl_width = 1

def draw_pixel(x, y, color, wall):
    wall.create_oval(x, y, x, y, outline=color)
    # wall.create_oval(x, y, x, y, width=pxl_width, outline=color)