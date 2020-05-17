using System;
using System.Drawing;
using System.Windows.Forms;

namespace lab_07
{
    public partial class MainWindow : Form
    {
        Graphics Canvas;

        // Параметры отсекателя
        ColorDialog CutterClrDialog = new ColorDialog();
        Color CutterColor = Color.Black;
        Point CutterStartPoint;
        Point CutterEndPoint;
        bool IsStartPointCutter = true;

        // Параметры линии
        ColorDialog LineClrDialog = new ColorDialog();
        Color LineColor = Color.Black;
        Point LineStartPoint;
        Point LineEndPoint;
        bool IsStartPointLine = true;

        // Параметры результата
        ColorDialog ResultClrDialog = new ColorDialog();
        Color ResultColor = Color.Black;

        // True если рисуем отсекатель, иначе если рисуем отрезки
        bool DrawCutter = true;
        // Проверка существования отсекателя
        bool CutterExists = false;

        public MainWindow()
        {
            InitializeComponent();
            InitGraphics();

            ButtonLineDraw.Enabled = false;
        }

        private void InitGraphics()
        {
            //pictureBox1.Image = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Canvas = pictureBox1.CreateGraphics();
            Canvas.Clear(Color.White);
            pictureBox1.BackColor = Color.White;
        }

        private void lbl_cutter_clr_Click(object sender, EventArgs e)
        {
            if (CutterClrDialog.ShowDialog() == DialogResult.OK)
            {
                CutterColor = CutterClrDialog.Color;
                lbl_cutter_clr.BackColor = CutterClrDialog.Color;
            }
        }

        private void lbl_line_clr_Click(object sender, EventArgs e)
        {
            if (LineClrDialog.ShowDialog() == DialogResult.OK)
            {
                LineColor = LineClrDialog.Color;
                lbl_line_clr.BackColor = LineClrDialog.Color;
            }
        }

        private void lbl_result_clr_Click(object sender, EventArgs e)
        {
            if (ResultClrDialog.ShowDialog() == DialogResult.OK)
            {
                ResultColor = ResultClrDialog.Color;
                lbl_result_clr.BackColor = ResultClrDialog.Color;
            }
        }


        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            if (DrawCutter)
            {
                CanvasDrawCutter(e.Location);
                ButtonLineDrawEnabled();
            }
            else
            {
                if (IsStartPointLine)
                {
                    LineStartPoint = e.Location;
                    IsStartPointLine = false;
                }
                else
                {
                    LineEndPoint = e.Location;
                    IsStartPointLine = true;

                    CanvasDrawLine(LineStartPoint, LineEndPoint, LineColor, 2);

                    SegmentCutOff(LineStartPoint, LineEndPoint);
                }
            }
        }


        // Получение кода точки
        private int[] PointFindCode(Point Point, Point CutterLeft, Point CutterRight)
        {
            int[] T = new int[4] { 0, 0, 0, 0 };

            T[0] = Point.X < CutterLeft.X ? 1 : 0;
            T[1] = Point.X > CutterRight.X ? 1 : 0;
            T[2] = Point.Y > CutterRight.Y ? 1 : 0;
            T[3] = Point.Y < CutterLeft.Y ? 1 : 0;

            return T;
        }

        // Поиск отсечения
        private Point FindRPoint(ref bool fl, Point Start, Point End, Point CutterL, Point CutterR, bool first)
        {
            float Epsilon = 0.0000001f;
            double m = Math.Pow(10, 30);
            Point Q = first ? Start : End;

            if (Start.X != End.X)
            {
                m = (double)(End.Y - Start.Y) / (End.X - Start.X);

                if (CutterL.X >= Q.X)
                {
                    int y = (int)Math.Round(m * (CutterL.X - Q.X) + Q.Y);
                    if ((y >= CutterL.Y) && (y <= CutterR.Y))
                    {
                        return new Point(CutterL.X, y);
                    }
                }

                if (CutterR.X <= Q.X)
                {
                    int y = (int)Math.Round(m * (CutterR.X - Q.X) + Q.Y);
                    if ((y >= CutterL.Y) && (y <= CutterR.Y))
                    {
                        return new Point(CutterR.X, y);
                    }
                }
            }

            if (Math.Abs(m - 0) <= Epsilon)
            {
                fl = false;
                return Q;
            }

            if (CutterL.Y >= Q.Y)
            {
                int x = (int)Math.Round((CutterL.Y - Q.Y) / m + Q.X);
                if ((x >= CutterL.X) && (x <= CutterR.X))
                {
                    return new Point(x, CutterL.Y);
                }
            }

            if (CutterR.Y <= Q.Y)
            {
                int x = (int)Math.Round((CutterR.Y - Q.Y) / m + Q.X);
                if ((x >= CutterL.X) && (x <= CutterR.X))
                {
                    return new Point(x, CutterR.Y);
                }
            }

            fl = false;
            return Q;
        }
        
        // Простой алгоритм отсечения отрезка
        private void SegmentCutOff(Point Start, Point End)
        {
            Point R1 = Start;
            Point R2 = End;

            int S1 = 0;
            int S2 = 0;
            int Pl = 0;

            bool flag = true;

            int[] T1 = PointFindCode(Start, CutterStartPoint, CutterEndPoint);
            int[] T2 = PointFindCode(End, CutterStartPoint, CutterEndPoint);

            for (int k = 0; k < 4; k++)
            {
                S1 += T1[k];
                S2 += T2[k];

                Pl += T1[k] * T2[k];
            }

            if ((S1 == 0) && (S2 == 0))
            {
                CanvasDrawLine(Start, End, ResultColor, 3);
                return;
            }

            if (Pl != 0)
            {
                return;
            }

            if (S1 != 0)
            {
                R1 = FindRPoint(ref flag, Start, End, CutterStartPoint, CutterEndPoint, true);
            }

            if (S2 != 0)
            {
                R2 = FindRPoint(ref flag, Start, End, CutterStartPoint, CutterEndPoint, false);
            }

            if (flag)
            {
                CanvasDrawLine(R1, R2, ResultColor, 3);
            }
        }


        // Методы рисования
        private void CanvasDrawCutter(Point MouseLocate)
        {
            if (IsStartPointCutter)
            {
                CutterStartPoint = MouseLocate;
                IsStartPointCutter = false;
            }
            else
            {
                Pen CutterPen = new Pen(CutterColor, 3);

                CutterEndPoint = MouseLocate;
                IsStartPointCutter = true;
                CutterExists = true;

                if ((CutterStartPoint.X > CutterEndPoint.X) || (CutterStartPoint.Y > CutterEndPoint.Y))
                {
                    Point Temp = CutterStartPoint;
                    CutterStartPoint = CutterEndPoint;
                    CutterEndPoint = Temp;
                }

                Rectangle Cutter = new Rectangle(CutterStartPoint.X, CutterStartPoint.Y,
                    Math.Abs(CutterStartPoint.X - CutterEndPoint.X),
                    Math.Abs(CutterStartPoint.Y - CutterEndPoint.Y));

                Canvas.DrawRectangle(CutterPen, Cutter);
            }
        }

        private void CanvasDrawLine(Point Start, Point End, Color LineColor, int width)
        {
            Pen LinePen = new Pen(LineColor, width);
            Canvas.DrawLine(LinePen, Start, End);
        }


        // Buttons
        private void ButtonClear_Click(object sender, EventArgs e)
        {
            IsStartPointLine = true;
            IsStartPointCutter = true;
            CutterExists = false;

            DrawCutter = true;

            ButtonLineDrawEnabled();

            Canvas.Clear(Color.White);
        }

        private void ButtonCutterDraw_Click(object sender, EventArgs e)
        {
            DrawCutter = true;
        }

        private void ButtonLineDrawEnabled()
        {
            if (CutterExists)
            {
                ButtonLineDraw.Enabled = true;
            }
            else
            {
                ButtonLineDraw.Enabled = false;
            }
        }

        private void ButtonLineDraw_Click(object sender, EventArgs e)
        {
            DrawCutter = false;
        }
    }
}
