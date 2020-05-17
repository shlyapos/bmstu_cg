#include "figureprocessing.h"
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "sceneprocessing.h"

static bool is_first(true);
static peak_t init_peak;
static peak_t start_peak;

void figure_draw_edge(scene_t *s, edge_t e)
{
    scene_draw_edge(s, e.start, e.end, edge_color);
}

void figure_find_seed(stack_t &st, scene_t *s, int lx, int rx, int y)
{
    int x = lx;
    bool fl = false;

    peak_t tmp;

    while (x <= rx)
    {
        while ((s->image.pixelColor(x, y) != edge_color) &&
               (s->image.pixelColor(x, y) != fill_color) && (x <= rx))
        {
            fl = true;
            x++;
        }

        if (fl)
        {
            tmp.x = x - 1;
            tmp.y = y;

            st.push(tmp);
        }

        do
        {
            x++;
        }
        while ((s->image.pixelColor(x, y) == edge_color ||
                s->image.pixelColor(x, y) == fill_color) && x < rx);
    }
}

void figure_init_edge(peak_t peak, scene_t *s)
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

        figure_draw_edge(s, new_edge);

        start_peak = peak;
    }
}

void figure_init_last_edge(peak_t peak, scene_t *s)
{
    edge_t last_edge;

    last_edge.start = peak;
    last_edge.end = init_peak;

    figure_draw_edge(s, last_edge);

    is_first = true;
}

void figure_fill(peak_t peak, scene_t *s)
{
    peak_t pnt;
    stack_t stack;

    int x, y;
    int lx, rx, tmp_x;

    int height = static_cast<int>(s->width());

    stack.push(peak);

    while (stack.size())
    {
        pnt = stack.top();
        stack.pop();

        x = static_cast<int>(pnt.x);
        y = static_cast<int>(pnt.y);

        if (x > s->width() || y > s->height() || x < 0 || y < 0)
        {
            return;
        }

        scene_draw_pixel(s, x, y, fill_color);

        tmp_x = x;

        while (s->image.pixelColor(x, y) != edge_color)
        {
            scene_draw_pixel(s, x, y, fill_color);
            x++;
        }

        rx = x - 1;
        x = tmp_x - 1;

        while (s->image.pixelColor(x, y) != edge_color)
        {
            scene_draw_pixel(s, x, y, fill_color);
            x--;
        }

        lx = x + 1;

        if (y > 0)
        {
            figure_find_seed(stack, s, lx, rx, y - 1);
        }
        if (is_delay)
        {
            scene_do_delay();
        }

        if (y < height)
        {
            figure_find_seed(stack, s, lx, rx, y + 1);
        }
        if (is_delay)
        {
            scene_do_delay();
            scene_update(s);
        }
    }
    scene_update(s);
}

void figure_clear(scene_t *s)
{
    scene_clear(s);
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
