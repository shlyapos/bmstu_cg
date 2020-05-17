#include "paintscene.h"
#include "figureprocessing.h"
#include "taskmanager.h"
#include "mainwindow.h"

PaintScene::PaintScene(QObject *parent) : QGraphicsScene (parent)
{}

PaintScene::~PaintScene()
{}


void PaintScene::mousePressEvent(QGraphicsSceneMouseEvent *event)
{
    peak_t new_peak;
    button_t button;

    new_peak.x = static_cast<float>(event->scenePos().x());
    new_peak.y = static_cast<float>(event->scenePos().y());

    button = button_init(BUTTON_ADD_EDGE, new_peak, this);

    taskmanager(button);
}

void PaintScene::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)
{
    peak_t new_peak;
    button_t button;

    new_peak.x = static_cast<float>(event->scenePos().x());
    new_peak.y = static_cast<float>(event->scenePos().y());

    button = button_init(MOUSE_DOUBLE_CLICK, new_peak, this);

    taskmanager(button);
}


void PaintScene::timerDelay()
{
    return;
}
