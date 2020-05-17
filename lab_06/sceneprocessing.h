#ifndef SCENEPROCESSING_H
#define SCENEPROCESSING_H

#include "mainhead.h"
#include "paintscene.h"

void scene_init(scene_t *s);
void scene_clear(scene_t *s);
void scene_update(scene_t *s);

void scene_draw_edge(scene_t *s, peak_t start, peak_t end, QColor color);
void scene_draw_edge_pixel(scene_t *s, coord_t x, coord_t y, QColor color);
void scene_draw_pixel(scene_t *s, coord_t x, coord_t y, QColor c);
void scene_do_delay();

#endif // SCENEPROCESSING_H
