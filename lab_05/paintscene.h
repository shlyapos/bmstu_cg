#ifndef PAINTSCENE_H
#define PAINTSCENE_H

#include "mainhead.h"

typedef QImage image_t;

class PaintScene : public QGraphicsScene
{
    Q_OBJECT

public:
    explicit PaintScene(QObject *parent = nullptr);
    ~PaintScene();
    image_t image;

private:
    void mousePressEvent(QGraphicsSceneMouseEvent *event);
    void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event);

private slots:
    void timerDelay();
};

typedef PaintScene scene_t;

#endif // PAINTSCENE_H
