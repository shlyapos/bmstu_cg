#include "sceneprocessing.h"
#include "figureprocessing.h"
#include "paintscene.h"

QColor bg_color(Qt::white);
QColor fr_color(Qt::black);

QColor fill_color(Qt::black);
QColor edge_color(Qt::black);

void scene_init(scene_t *s)
{
//    coord_t d = 1;
    peak_t st, en;

    coord_t w = static_cast<coord_t>(s->image.width());
    coord_t h = static_cast<coord_t>(s->image.height());

    // Up
    st = { 0, 0 };
    en = { w - 4, 0 };
    scene_draw_edge(s, st, en, fr_color);

    // Right
    st = en;
    en = { w - 4, h - 4 };
    scene_draw_edge(s, st, en, fr_color);

    // Down
    st = en;
    en = { 0, h - 4 };
    scene_draw_edge(s, st, en, fr_color);

    // Left
    st = en;
    en = { 0, 0 };
    scene_draw_edge(s, st, en, fr_color);
}

void scene_clear(scene_t *s)
{
    QImage new_image = QImage(static_cast<int>(s->width()), static_cast<int>(s->height()), QImage::Format_RGB32);
    new_image.fill(bg_color);
    s->image = new_image;

    scene_update(s);
    scene_init(s);
}

void scene_update(scene_t *s)
{
    s->clear();
    s->addPixmap(QPixmap::fromImage(s->image));
}


void scene_draw_edge(scene_t *s, peak_t start, peak_t end, QColor color)
{
    float l;

    float x, y;
    float dx, dy;

    if (abs(end.x - start.x) > abs(end.y - start.y))
    {
        l = abs(end.x - start.x);
    }
    else
    {
        l = abs(end.y - start.y);
    }

    dx = (end.x - start.x) / l;
    dy = (end.y - start.y) / l;

    x = start.x;
    y = start.y;

    for (int i = 0; i < dx + l; i++)
    {
        scene_draw_edge_pixel(s, x, y, color);

        x += dx;
        y += dy;
    }
    scene_update(s);
}

void scene_draw_edge_pixel(scene_t *s, coord_t x, coord_t y, QColor color)
{
    scene_draw_pixel(s, x, y, color);
    scene_draw_pixel(s, x + 1, y, color);
    scene_draw_pixel(s, x + 1, y + 1, color);
    scene_draw_pixel(s, x, y + 1, color);
}

void scene_draw_pixel(scene_t *s, coord_t x, coord_t y, QColor color)
{
    s->image.setPixelColor(static_cast<int>(x), static_cast<int>(y), color);
}

void scene_do_delay()
{
    QEventLoop loop;
    QTimer::singleShot(10, &loop, SLOT(quit()));
    loop.exec();
}
