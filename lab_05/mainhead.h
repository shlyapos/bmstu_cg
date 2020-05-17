#ifndef MAINHEAD_H
#define MAINHEAD_H

#include <vector>
#include <math.h>

#include <QMainWindow>
#include <QGraphicsView>
#include <QMessageBox>
#include <QDoubleValidator>
#include <QMouseEvent>
#include <QGraphicsSceneMouseEvent>
#include <QDebug>
#include <QTimer>
#include <QtWidgets>

typedef enum
{
    EXIT_OK     = 0,
    EXIT_ERROR  = 1,
    ERROR_DATA  = 2
} out_t;

typedef float coord_t;

using namespace std;

#endif // MAINHEAD_H
