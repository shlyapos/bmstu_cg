#ifndef SCENEPROCESSING_H
#define SCENEPROCESSING_H

#include "mainhead.h"
#include "paintscene.h"

void scene_clear(scene_t *s);
void scene_draw_edge(scene_t *s, coord_t xs, coord_t ys, coord_t xe, coord_t ye);
void scene_draw_pixel(scene_t *s, coord_t x, coord_t y, QColor c);
void scene_do_delay();

#endif // SCENEPROCESSING_H
