#ifndef FIGUREPROCESSING_H
#define FIGUREPROCESSING_H

#include "mainhead.h"
#include "mainwindow.h"

extern bool is_delay;

extern QColor bg_color;
extern QColor edge_color;
extern QColor fill_color;

typedef struct
{
    peak_t start;
    peak_t end;
} edge_t;

typedef vector <edge_t> figure_t;
typedef stack <peak_t> stack_t;

#define EPSILON 1e-8

void figure_draw_edge(scene_t s, edge_t e);
void figure_find_seed(stack_t &st, scene_t *s, int lx, int rx, int y);
void figure_init_edge(peak_t peak, scene_t *s);
void figure_init_last_edge(peak_t peak, scene_t *s);
void figure_fill(peak_t peak, scene_t *s);
void figure_clear(scene_t *s);

bool coord_is_equal(coord_t c1, coord_t c2);
bool coord_is_larger(coord_t c1, coord_t c2);
void coord_switch(coord_t &c1, coord_t &c2);

#endif // FIGUREPROCESSING_H
