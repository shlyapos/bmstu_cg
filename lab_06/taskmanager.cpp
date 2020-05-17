#include "taskmanager.h"
#include "mainhead.h"
#include "figureprocessing.h"
#include "mainhead.h"

button_t button_init(button_type_t mode, peak_t peak, scene_t *s)
{
    button_t b;

    b.mode = mode;
    b.peak = peak;
    b.scene = s;

    return b;
}

out_t taskmanager(button_t action)
{
    out_t error = EXIT_OK;

    switch (action.mode)
    {
    case BUTTON_ADD_EDGE:
        figure_init_edge(action.peak, action.scene);
        break;
    case MOUSE_DOUBLE_CLICK:
        figure_init_last_edge(action.peak, action.scene);
        break;
    case BUTTON_FILL:
        figure_fill(action.peak, action.scene);
        break;
    case BUTTON_CLEAR:
        figure_clear(action.scene);
        break;
    }
    return error;
}
