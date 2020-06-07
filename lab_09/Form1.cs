using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using System.Windows.Input;

namespace lab_09
{
    struct Segment
    {
        public PointF Start;
        public PointF End;

        public Segment(PointF S, PointF E)
        {
            Start = S;
            End = E;
        }
    }

    public partial class Form1 : Form
    { 
        Graphics Canvas;
        ColorDialog PickColor = new ColorDialog();

        // Параметры отсекателя
        Cutter CurrentCutter;
        Color CutterColor = Color.Black;

        // Параметры многоугольника
        Polygon CurrentPolygon;
        Color PolygonColor = Color.Black;

        // Параметры результата
        Color ResultColor = Color.Black;

        // True если рисуем отсекатель, иначе если рисуем отрезки
        bool DrawCutter = true;
        // Проверка существования отсекателя
        bool CutterExists = false;


        public Form1()
        {
            InitializeComponent();
            Canvas = pictureBox1.CreateGraphics();

            CurrentCutter = new Cutter();
            CurrentPolygon = new Polygon();

            ButtonPolygonDraw.Enabled = false;
        }


        // ColorDialog binds
        private void LabelCutterColor_Click(object sender, EventArgs e)
        {
            if (PickColor.ShowDialog() == DialogResult.OK)
            {
                CutterColor = PickColor.Color;
                LabelCutterColor.BackColor = CutterColor;
            }
        }

        private void LabelSegmentColor_Click(object sender, EventArgs e)
        {
            if (PickColor.ShowDialog() == DialogResult.OK)
            {
                PolygonColor = PickColor.Color;
                LabelPolygonColor.BackColor = PolygonColor;
            }
        }

        private void LabelResultColor_Click(object sender, EventArgs e)
        {
            if (PickColor.ShowDialog() == DialogResult.OK)
            {
                ResultColor = PickColor.Color;
                LabelResultColor.BackColor = ResultColor;
            }
        }


        // PictureBox binds
        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            CanvasDrawPolygon(e.Location);
        }

        private void pictureBox1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            CanvasDrawPolygonEnd(e.Location);
        }


        // Canvas draw methods
        private void CanvasDrawPolygon(Point MouseLocate)
        {
            if (DrawCutter)
            {
                if (CurrentCutter.Count() != 0)
                {
                    CanvasDrawLine(CurrentCutter.GetLast(), MouseLocate, CutterColor);
                }

                CurrentCutter.AddPeak(MouseLocate);
            }
            else
            {
                if (CurrentPolygon.Count() != 0)
                {
                    CanvasDrawLine(CurrentPolygon.GetLast(), MouseLocate, PolygonColor);
                }

                CurrentPolygon.AddPeak(MouseLocate);
            }
        }

        private void CanvasDrawPolygonEnd(PointF MouseLocate)
        {
            if (DrawCutter)
            {
                if (CurrentCutter.Count() > 2)
                {
                    CanvasDrawLine(CurrentCutter.GetPeak(0), MouseLocate, CutterColor);

                    CutterExists = true;

                    CurrentCutter.ConvexCheck();
                    ButtonPolygonDrawEnabled();
                }
            }
            else
            {
                if (CurrentPolygon.Count() > 2)
                {
                    CanvasDrawLine(CurrentPolygon.GetPeak(0), MouseLocate, PolygonColor);
                    
                    CurrentPolygon.AddPeak(CurrentPolygon.GetPeak(0));

                    if (CurrentCutter.IsConvex())
                    {
                        Pen PolygonPen = new Pen(ResultColor, 3);
                        Polygon Result = CurrentCutter.CutPolygon(CurrentPolygon);
                        Canvas.DrawPolygon(PolygonPen, Result.ToArray());
                    }
                    else
                    { 
                        MessageBox.Show("Отсекатель должен быть выпуклым", "Ошибка", MessageBoxButtons.OK);
                    }
                }
            }
        }

        private void CanvasDrawLine(PointF Start, PointF End, Color LineColor)
        {
            Pen LinePen = new Pen(LineColor, 2);
            Canvas.DrawLine(LinePen, Start, End);
        }


        // Buttons binds
        private void ButtonClear_Click(object sender, EventArgs e)
        {
            DrawCutter = true;
            CutterExists = false;

            CurrentCutter.Clear();
            CurrentPolygon.Clear();

            ButtonPolygonDrawEnabled();

            Canvas.Clear(Color.White);
        }

        private void ButtonPolygonDrawEnabled()
        {
            if (CutterExists)
            {
                ButtonPolygonDraw.Enabled = true;
            }
            else
            {
                ButtonPolygonDraw.Enabled = false;
            }
        }

        private void ButtonCutterDraw_Click(object sender, EventArgs e)
        {
            DrawCutter = true;
        }

        private void ButtonPolygonDraw_Click(object sender, EventArgs e)
        {
            DrawCutter = false;
        }
    }
}