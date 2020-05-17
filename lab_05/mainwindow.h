#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "mainhead.h"
#include "sceneprocessing.h"

extern QColor bg_color;
extern QColor edge_color;
extern QColor fill_color;

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    Ui::MainWindow *ui;
    scene_t *scene;

private:
    void initLineEdits();
    void initGraphicScene();
    void initButton();
    void initRadiobuttons();
    void initCheckBox();
    void validateLineEdits();

private slots:
    void edgeAddNewButton();
    void figureFillButton();
    void figureClearButton();

    void edgeRadioToggledBlack(bool value);
    void edgeRadioToggledRed(bool value);
    void edgeRadioToggledGreen(bool value);
    void edgeRadioToggledBlue(bool value);

    void fillRadioToggledBlack(bool value);
    void fillRadioToggledRed(bool value);
    void fillRadioToggledGreen(bool value);
    void fillRadioToggledBlue(bool value);

    void delayToggledCheckButton(bool value);

    void bgRadioToggledBlack(bool value);
    void bgRadioToggledWhite(bool value);
};

typedef MainWindow mainwindow_t;

#endif // MAINWINDOW_H
