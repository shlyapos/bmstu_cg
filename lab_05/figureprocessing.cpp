#include "figureprocessing.h"
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "sceneprocessing.h"

static bool is_first(true);

static peak_t init_peak;
static peak_t start_peak;

float find_area(figure_t f)
{
    double result = 1;
    double len;

    auto size = f.size();
    auto i = size;

    for (i = 0; i < size; i++)
    {
        len = sqrt(pow((f[i].start.x - f[i].end.x), 2) + pow((f[i].start.y - f[i].end.y), 2));
        result *= len;
    }
    return static_cast<float>(result);
}

void figure_add_edge(figure_t &f, edge_t e)
{
    f.push_back(e);
}

void figure_draw_edge(scene_t *s, edge_t e)
{
    scene_draw_edge(s, e.start.x, e.start.y, e.end.x, e.end.y);
}

void figure_init_edge(figure_t &f, peak_t peak, scene_t *s)
{
    edge_t new_edge;

    if (is_first == true)
    {
        init_peak = peak;
        start_peak = peak;
        is_first = false;
    }
    else
    {
        new_edge.start = start_peak;
        new_edge.end = peak;

        figure_add_edge(f, new_edge);
        figure_draw_edge(s, new_edge);

        start_peak = peak;
    }
}

void figure_init_last_edge(figure_t &f, peak_t peak, scene_t *s)
{
    edge_t last_edge;

    figure_init_edge(f, peak, s);

    last_edge.start = peak;
    last_edge.end = init_peak;

    figure_add_edge(f, last_edge);
    figure_draw_edge(s, last_edge);

    is_first = true;
}

void figure_clear_edge(figure_t &f)
{
    f.clear();
    is_first = true;
}

void figure_fill_by_edge(figure_t &f, scene_t *s)
{
    QColor col;
    QColor col_bg = bg_color;
    QColor col_fill = fill_color;

    coord_t x, y;
    coord_t end_y;
    coord_t start_x, dx;

    peak_t start, end;

    auto size = f.size();
    auto i = size;
    auto j = size;

    if (size == 0)
        return;

    coord_t max_x = coord_find_max(f);

    for (i = 0; i < size; i++)
    {
        start = f[i].start;
        end = f[i].end;

        // Проверка на горизонтальность
        if (coord_is_equal(start.y, end.y) == true)
            continue;

        // Первое больше второго, если да, то поменять местами
        if (coord_is_larger(start.y, end.y))
        {
            coord_switch(start.x, end.x);
            coord_switch(start.y, end.y);
        }

        // Подготовка данных
        y = start.y;
        end_y = end.y;

        dx = (end.x - start.x) / (end.y - start.y);
        start_x = start.x;

        while (y < end_y)
        {
            x = start_x;
            while (x < max_x)
            {
                col = QColor(s->image.pixel(static_cast<int>(x), static_cast<int>(y)));

                if (col == col_bg)
                    scene_draw_pixel(s, x, y, col_fill);
                else
                    scene_draw_pixel(s, x, y, col_bg);
                x += 1;
            }
            start_x += dx;
            y += 1;

            // Если установлена задержка, то обновлять каждую скан. строку
            if (is_delay == true)
            {
                scene_do_delay();
                s->clear();

                s->addPixmap(QPixmap::fromImage(s->image));

                for (j = 0; j < size; j++)
                    figure_draw_edge(s, f[j]);
            }
        }
        if (is_delay == false)
        {
            s->addPixmap(QPixmap::fromImage(s->image));
        }
    }
    for (i = 0; i < size; i++)
        figure_draw_edge(s, f[i]);
}

void figure_clear(figure_t &f, scene_t *s)
{
    figure_clear_edge(f);
    scene_clear(s);
}


coord_t coord_find_max(figure_t f)
{
    unsigned long long int size = f.size();
    unsigned long long int i = size;

    coord_t max = f[0].start.x;

    for (i = 0; i < size; i++)
    {
        if (f[i].start.x > max)
            max = f[i].start.x;

        if (f[i].end.x > max)
            max = f[i].end.x;
    }

    return max;
}

bool coord_is_equal(coord_t c1, coord_t c2)
{
    double n1 = static_cast<double>(c1);
    double n2 = static_cast<double>(c2);

    return fabs(n1 - n2) <= ((fabs(n1) < fabs(n2) ? fabs(n2) : fabs(n1)) * EPSILON);
}

bool coord_is_larger(coord_t c1, coord_t c2)
{
    bool result = false;

    if (c1 > c2)
        result = true;

    return result;
}

void coord_switch(coord_t &c1, coord_t &c2)
{
    coord_t tmp = c1;
    c1 = c2;
    c2 = tmp;
}
