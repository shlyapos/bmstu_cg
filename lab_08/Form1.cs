using System;
using System.Drawing;
using System.Windows.Forms;

// Кликом устанавливаются вершины отсекателя, дабл кликом отсекатель замыкается

namespace lab_08
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
        Cutter CurrentCutter;
        Graphics Canvas;
        ColorDialog ColorPick = new ColorDialog();

        // Параметры отсекателя
        Color CutterColor = Color.Black;
        PointF CutterInitPoint;
        PointF CutterStartPoint;
        PointF CutterEndPoint;
        bool IsStartPointCutter = true;

        // Параметры отрезка
        Color SegmentColor = Color.Black;
        PointF SegmentStartPoint;
        PointF SegmentEndPoint;
        bool IsStartPointSegment = true;

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

            ButtonSegmentDraw.Enabled = false;
        }


        // ColorDialog binds
        private void LabelCutterColor_Click(object sender, EventArgs e)
        {
            if (ColorPick.ShowDialog() == DialogResult.OK)
            {
                CutterColor = ColorPick.Color;
                LabelCutterColor.BackColor = CutterColor;
            }
        }

        private void LabelSegmentColor_Click(object sender, EventArgs e)
        {
            if (ColorPick.ShowDialog() == DialogResult.OK)
            {
                SegmentColor = ColorPick.Color;
                LabelSegmentColor.BackColor = SegmentColor;
            }
        }

        private void LabelResultColor_Click(object sender, EventArgs e)
        {
            if (ColorPick.ShowDialog() == DialogResult.OK)
            {
                ResultColor = ColorPick.Color;
                LabelResultColor.BackColor = ResultColor;
            }
        }


        // PictureBox binds
        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            if (DrawCutter)
            {
                CanvasDrawCutter(e.Location);
            }
            else
            {
                CanvasDrawSegment(e.Location);
            }
        }

        private void pictureBox1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if (!IsStartPointCutter)
            {
                CutterStartPoint = CutterEndPoint;
                CutterEndPoint = CutterInitPoint;

                CanvasDrawLine(CutterStartPoint, CutterEndPoint, CutterColor);

                IsStartPointCutter = true;
                CutterExists = true;
            }

            CurrentCutter.ConvexCheck();
            ButtonSegmentDrawEnabled();
        }


        // Canvas draw methods
        private void CanvasDrawCutter(Point MouseLocate)
        {
            if (IsStartPointCutter)
            {
                CutterStartPoint = MouseLocate;
                CutterInitPoint = MouseLocate;
                IsStartPointCutter = false;
            }
            else
            {
                CutterEndPoint = MouseLocate;
                CanvasDrawLine(CutterStartPoint, CutterEndPoint, CutterColor);
                CutterStartPoint = CutterEndPoint;
            }

            CurrentCutter.AddPeak(MouseLocate);
        }

        private void CanvasDrawSegment(Point MouseLocate)
        {
            if (IsStartPointSegment)
            {
                SegmentStartPoint = MouseLocate;
                IsStartPointSegment = false;
            }
            else
            {
                SegmentEndPoint = MouseLocate;
                IsStartPointSegment = true;
                CanvasDrawLine(SegmentStartPoint, SegmentEndPoint, SegmentColor);

                if (CurrentCutter.IsConvex())
                {
                    Segment Result = CurrentCutter.CutSegment(SegmentStartPoint, SegmentEndPoint);
                    CanvasDrawLine(Result.Start, Result.End, ResultColor);
                }
                else
                {
                    MessageBox.Show("Отсекатель должен быть выпуклым", "Ошибка", MessageBoxButtons.OK);
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
            IsStartPointCutter = true;
            DrawCutter = true;
            CutterExists = false;
            CurrentCutter.Clear();

            IsStartPointSegment = true;


            ButtonSegmentDrawEnabled();

            Canvas.Clear(Color.White);
        }

        private void ButtonSegmentDrawEnabled()
        {
            if (CutterExists)
            {
                ButtonSegmentDraw.Enabled = true;
            }
            else
            {
                ButtonSegmentDraw.Enabled = false;
            }
        }

        private void ButtonCutterDraw_Click(object sender, EventArgs e)
        {
            DrawCutter = true;
        }

        private void ButtonSegmentDraw_Click(object sender, EventArgs e)
        {
            DrawCutter = false;
        }

        private void label6_Click(object sender, EventArgs e)
        {
            SegmentStartPoint = new Point(100, pictureBox1.Height / 2);
            SegmentEndPoint = new Point(pictureBox1.Width - 100, pictureBox1.Height / 2);
            CanvasDrawLine(SegmentStartPoint, SegmentEndPoint, SegmentColor);

            if (CurrentCutter.IsConvex())
            {
                Segment Result = CurrentCutter.CutSegment(SegmentStartPoint, SegmentEndPoint);
                CanvasDrawLine(Result.Start, Result.End, ResultColor);
            }
            else
            {
                MessageBox.Show("Ошибка", "Отсекатель не выпуклый", MessageBoxButtons.OK);
            }
        }

        private void label5_Click(object sender, EventArgs e)
        {
            SegmentStartPoint = new Point(pictureBox1.Width / 2, 100);
            SegmentEndPoint = new Point(pictureBox1.Width / 2, pictureBox1.Height - 100);
            CanvasDrawLine(SegmentStartPoint, SegmentEndPoint, SegmentColor);

            if (CurrentCutter.IsConvex())
            {
                Segment Result = CurrentCutter.CutSegment(SegmentStartPoint, SegmentEndPoint);
                CanvasDrawLine(Result.Start, Result.End, ResultColor);
            }
            else
            {
                MessageBox.Show("Ошибка", "Отсекатель не выпуклый", MessageBoxButtons.OK);
            }
        }
    }
}
