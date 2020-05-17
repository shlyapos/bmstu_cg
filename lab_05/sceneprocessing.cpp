#include "sceneprocessing.h"
#include "figureprocessing.h"
#include "paintscene.h"

QColor bg_color(Qt::white);
QColor edge_color(Qt::black);
QColor fill_color(Qt::black);

void scene_clear(scene_t *s)
{
    QPixmap pixmap;
    QImage new_image = QImage(static_cast<int>(s->width()), static_cast<int>(s->height()), QImage::Format_RGB32);
    new_image.fill(bg_color);

    s->clear();

    s->image = new_image;
    pixmap.convertFromImage(s->image);
    s->addPixmap(pixmap);
}

void scene_draw_edge(scene_t *s, coord_t xs, coord_t ys, coord_t xe, coord_t ye)
{
    QPen pen;

    pen.setColor(edge_color);
    pen.setWidth(2);

    s->addLine(static_cast<double>(xs), static_cast<double>(ys), \
               static_cast<double>(xe), static_cast<double>(ye), pen);
}

void scene_draw_pixel(scene_t *s, coord_t x, coord_t y, QColor c)
{
    QColor col;

    if (c != fill_color)
        col = bg_color;
    else
        col = fill_color;

    s->image.setPixelColor(static_cast<int>(x), static_cast<int>(y), col);
}

void scene_do_delay()
{
    QEventLoop loop;
    QTimer::singleShot(10, &loop, SLOT(quit()));
    loop.exec();
}
