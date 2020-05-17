#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "mainhead.h"
#include "sceneprocessing.h"
#include "figureprocessing.h"
#include "taskmanager.h"

bool is_delay;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    initLineEdits();
    initGraphicScene();
    initButton();
    initRadiobuttons();
    initCheckBox();
    validateLineEdits();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::initLineEdits()
{
    ui->lineEdit_add_xs->setText("0");
    ui->lineEdit_add_ys->setText("0");

    ui->lineEdit_add_xe->setText("0");
    ui->lineEdit_add_ye->setText("0");
}

void MainWindow::initGraphicScene()
{
    int width = ui->graphicsView->width();
    int height = ui->graphicsView->height();

    scene = new PaintScene(this);

    ui->graphicsView->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    ui->graphicsView->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    ui->graphicsView->setAlignment(Qt::AlignCenter);

    scene->image = QImage(width, height, QImage::Format_RGB32);
    scene->image.fill(bg_color);

    ui->graphicsView->setScene(scene);

    ui->graphicsView->setSceneRect(QRect(0, 0, width, height));
    ui->graphicsView->setMouseTracking(true);

    scene->addPixmap(QPixmap::fromImage(scene->image));
}

void MainWindow::initButton()
{
    connect(ui->btn_add_edge, SIGNAL(released()), this, SLOT(edgeAddNewButton()));
    connect(ui->btn_fill_figure, SIGNAL(released()), this, SLOT(figureFillButton()));
    connect(ui->btn_clear_figure, SIGNAL(released()), this, SLOT(figureClearButton()));
}

void MainWindow::initRadiobuttons()
{
    ui->rbtn_edge_black->toggle();
    ui->rbtn_fill_black->toggle();
    ui->radioButton->toggle();

    connect(ui->rbtn_edge_black, SIGNAL(toggled(bool)), this, SLOT(edgeRadioToggledBlack(bool)));
    connect(ui->rbtn_edge_red, SIGNAL(toggled(bool)), this, SLOT(edgeRadioToggledRed(bool)));
    connect(ui->rbtn_edge_green, SIGNAL(toggled(bool)), this, SLOT(edgeRadioToggledGreen(bool)));
    connect(ui->rbtn_edge_blue, SIGNAL(toggled(bool)), this, SLOT(edgeRadioToggledBlue(bool)));

    connect(ui->rbtn_fill_black, SIGNAL(toggled(bool)), this, SLOT(fillRadioToggledBlack(bool)));
    connect(ui->rbtn_fill_red, SIGNAL(toggled(bool)), this, SLOT(fillRadioToggledRed(bool)));
    connect(ui->rbtn_fill_green, SIGNAL(toggled(bool)), this, SLOT(fillRadioToggledGreen(bool)));
    connect(ui->rbtn_fill_blue, SIGNAL(toggled(bool)), this, SLOT(fillRadioToggledBlue(bool)));

    connect(ui->radioButton, SIGNAL(toggled(bool)), this, SLOT(bgRadioToggledWhite(bool)));
    connect(ui->radioButton_2, SIGNAL(toggled(bool)), this, SLOT(bgRadioToggledBlack(bool)));
}

void MainWindow::initCheckBox()
{
    connect(ui->checkBox_sleep, SIGNAL(toggled(bool)), this, SLOT(delayToggledCheckButton(bool)));
}

void MainWindow::validateLineEdits()
{
    QValidator *val = new QDoubleValidator();
    val->setLocale(QLocale(QLocale::English));

    ui->lineEdit_add_xs->setValidator(val);
    ui->lineEdit_add_ys->setValidator(val);

    ui->lineEdit_add_xe->setValidator(val);
    ui->lineEdit_add_ye->setValidator(val);
}


// Slots for edges
void MainWindow::edgeRadioToggledBlack(bool value)
{
    if (value)
    {
        edge_color = Qt::black;
    }
}

void MainWindow::edgeRadioToggledRed(bool value)
{
    if (value)
    {
        edge_color = Qt::red;
    }
}

void MainWindow::edgeRadioToggledGreen(bool value)
{
    if (value)
    {
        edge_color = Qt::green;
    }
}

void MainWindow::edgeRadioToggledBlue(bool value)
{
    if (value)
    {
        edge_color = Qt::blue;
    }
}


// Slots for fill
void MainWindow::fillRadioToggledBlack(bool value)
{
    if (value)
    {
        fill_color = Qt::black;
    }
}

void MainWindow::fillRadioToggledRed(bool value)
{
    if (value)
    {
        fill_color = Qt::red;
    }
}

void MainWindow::fillRadioToggledGreen(bool value)
{
    if (value)
    {
        fill_color = Qt::green;
    }
}

void MainWindow::fillRadioToggledBlue(bool value)
{
    if (value)
    {
        fill_color = Qt::blue;
    }
}


// Slots for delay
void MainWindow::delayToggledCheckButton(bool value)
{
    if (value)
        is_delay = true;
    else
        is_delay = false;
}


// Slot for bg color
void MainWindow::bgRadioToggledWhite(bool value)
{
    if (value)
    {
        int width = ui->graphicsView->width();
        int height = ui->graphicsView->height();

        bg_color = Qt::white;

        QImage new_image = QImage(width, height, QImage::Format_RGB32);
        new_image.fill(bg_color);

        scene->image = new_image;
        scene->addPixmap(QPixmap::fromImage(scene->image));
    }
}

void MainWindow::bgRadioToggledBlack(bool value)
{
    if (value)
    {
        int width = ui->graphicsView->width();
        int height = ui->graphicsView->height();

        bg_color = Qt::black;

        QImage new_image = QImage(width, height, QImage::Format_RGB32);
        new_image.fill(bg_color);

        scene->image = new_image;
        scene->addPixmap(QPixmap::fromImage(scene->image));
    }
}

// Slots for button
void MainWindow::edgeAddNewButton()
{
    out_t error = EXIT_OK;
    button_t button;

    peak_t start, end;
    int height;

    if (ui->lineEdit_add_xs->text().isEmpty())
        error = ERROR_DATA;
    if (ui->lineEdit_add_ys->text().isEmpty())
        error = ERROR_DATA;
    if (ui->lineEdit_add_xe->text().isEmpty())
        error = ERROR_DATA;
    if (ui->lineEdit_add_ye->text().isEmpty())
        error = ERROR_DATA;

    if (error == EXIT_OK)
    {
        height = ui->graphicsView->height();

        start.x = ui->lineEdit_add_xs->text().toFloat();
        start.y = height - ui->lineEdit_add_ys->text().toFloat();

        end.x = ui->lineEdit_add_xe->text().toFloat();
        end.y = height - ui->lineEdit_add_ye->text().toFloat();

        button = button_init(BUTTON_ADD_EDGE, start, scene);
        error = taskmanager(button);

        button = button_init(BUTTON_ADD_EDGE, end, scene);
        error = taskmanager(button);
    }
}

void MainWindow::figureFillButton()
{
    out_t error = EXIT_OK;

    peak_t peak;
    button_t button;

    peak.x = 0;
    peak.x = 0;

    button = button_init(BUTTON_FILL, peak, scene);
    error = taskmanager(button);

    if (error != EXIT_OK)
        return;
}

void MainWindow::figureClearButton()
{
    out_t error = EXIT_OK;

    peak_t peak;
    button_t button;

    peak.x = 0;
    peak.x = 0;

    button = button_init(BUTTON_CLEAR, peak, scene);
    error = taskmanager(button);

    if (error != EXIT_OK)
        return;
}
