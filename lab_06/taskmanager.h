#ifndef TASKMANAGER_H
#define TASKMANAGER_H

#include "mainhead.h"
#include "mainwindow.h"
#include "figureprocessing.h"

typedef enum
{
    BUTTON_ADD_EDGE     = 10,
    BUTTON_FILL         = 20,
    BUTTON_CLEAR        = 30,
    MOUSE_DOUBLE_CLICK  = 40
} button_type_t;

typedef struct
{
    button_type_t mode;
    peak_t peak;
    scene_t *scene;
} button_t;

button_t button_init(button_type_t mode, peak_t peak, scene_t *s);
out_t taskmanager(button_t action);

#endif // TASKMANAGER_H
