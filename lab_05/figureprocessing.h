#ifndef EDGEPROCESSING_H
#define EDGEPROCESSING_H

#include "mainhead.h"
#include "mainwindow.h"

extern bool is_delay;

extern QColor bg_color;
extern QColor edge_color;
extern QColor fill_color;

typedef struct
{
    coord_t x;
    coord_t y;
} peak_t;

typedef struct
{
    peak_t start;
    peak_t end;
} edge_t;

typedef vector <edge_t> figure_t;

#define EPSILON 1e-8

void figure_add_edge(figure_t &f, edge_t e);
void figure_draw_edge(edge_t e);
void figure_init_edge(figure_t &f, peak_t peak, scene_t *s);
void figure_init_last_edge(figure_t &f, peak_t peak, scene_t *s);
void figure_clear_edge(figure_t &f);
void figure_fill_by_edge(figure_t &f, scene_t *s);
void figure_clear(figure_t &f, scene_t *s);

coord_t coord_find_max(figure_t f);
bool coord_is_equal(coord_t c1, coord_t c2);
bool coord_is_larger(coord_t c1, coord_t c2);
void coord_switch(coord_t &c1, coord_t &c2);

#endif // EDGEPROCESSING_H
