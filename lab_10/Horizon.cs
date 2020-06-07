using System;
using System.Drawing;

namespace lab_10
{
    public struct Spacing
    {
        public double Start;
        public double End;
        public double Delta;

        public int Count;

        public Spacing(double Start, double End, double Step)
        {
            this.Start = Start;
            this.End = End;
            this.Delta = Step;

            Count = (int)Math.Ceiling((End - Start) / Step);
        }
    }

    class Horizon
    {
        private Size ScreenSize;
        private int[] Down, Top;

        private Func<double, double, double> f;
        private Pen PenDraw;

        public Horizon(Pen P, Size S, Func<double, double, double> func)
        {
            Down = new int[S.Width];
            Top = new int[S.Width];

            ScreenSize = S;
            f = func;
            PenDraw = P;
        }

        // Инициализация массивов горизонта
        private void PrepareArray()
        {
            for (int i = 0; i < Top.Length; i++)
            {
                Down[i] = ScreenSize.Height;
                Top[i] = 0;
            }
        }

        // Пересечение двух отрезков прямых
        private void GetIntersection(int x1, int y1, int x2, int y2, int[] Horizon, ref int xi, ref int yi)
        {
            xi = x1;
            yi = y1;

            int delta_x = x2 - x1;
            int delta_y_c = y2 - y1;
            int delta_y_p = Horizon[x2] - Horizon[x1];
            double m = delta_y_c / (double)delta_x;

            if (delta_x == 0)
            {
                xi = x2;
                yi = Horizon[x2];
            }
            else if ((y1 == Horizon[x1]) && (y2 == Horizon[x2]))
            {
                xi = x1;
                yi = y1;
            }
            else
            {
                xi = x1 - (int)Math.Round(delta_x * (y1 - Horizon[x1]) / (double)(delta_y_c - delta_y_p));
                yi = (int)Math.Round((xi - x1) * m + y1);
            }
        }

        // Используя линейную интерполяцию, заполняет массивы горизонтов между точками
        private void horizon(int x1, int y1, int x2, int y2, Graphics Painter)
        {
            if ((x2 < 0) || (x2 > ScreenSize.Width - 1))
            {
                return;
            }
            if ((x1 < 0) || (x1 > ScreenSize.Width - 1))
            {
                return;
            }

            if (x2 < x1)
            {
                Swap(ref x1, ref x2);
                Swap(ref y1, ref y2);
            }

            if (x2 - x1 == 0)
            {
                Top[x2] = Math.Max(Top[x2], y2);
                Down[x2] = Math.Min(Down[x2], y2);

                if ((x2 >= 0) && (x2 <= ScreenSize.Width))
                {
                    Painter.DrawLine(PenDraw, x1, y1, x2, y2);
                }
            }
            else
            {
                int PrevX = x1;
                int PrevY = y1;
                double m = (y2 - y1) / (double)(x2 - x1);

                for (int x = x1; x <= x2; x++)
                {
                    int y = (int)Math.Round(m * (x - x1) + y1);

                    Top[x] = Math.Max(Top[x], y);
                    Down[x] = Math.Min(Down[x], y);

                    if ((x >= 0) && (x <= ScreenSize.Width))
                    {
                        Painter.DrawLine(PenDraw, PrevX, PrevY, x, y);
                    }
                }
            }
        }


        // Обработка концевого ребра
        private void EdgeProcessing(ref int x, ref int y, ref int EdgeX, ref int EdgeY, Graphics Painter)
        {
            if (EdgeX != -1)
            {
                horizon(EdgeX, EdgeY, x, y, Painter);
            }

            EdgeX = x;
            EdgeY = y;
        }


        // Проверка видимости текущей точки
        private int Visible(int x, int y)
        {
            if ((y < Top[x]) && (y > Down[x]))
            {
                return 0;
            }

            if (y >= Top[x])
            {
                return 1;
            }

            return -1;
        }


        // Повороты
        private void RotateX(ref double y, ref double z, ref double Tetax)
        {
            Tetax *= Math.PI / 180;
            double buf = y;

            y = Math.Cos(Tetax) * y - Math.Sin(Tetax) * z;
            z = Math.Cos(Tetax) * z + Math.Sin(Tetax) * buf;
        }

        private void RotateY(ref double x, ref double z, double Tetay)
        {
            Tetay *= Math.PI / 180;
            double buf = x;

            x = Math.Cos(Tetay) * x - Math.Sin(Tetay) * z;
            z = Math.Cos(Tetay) * z + Math.Sin(Tetay) * buf;
        }

        private void RotateZ(ref double x, ref double y, double Tetaz)
        {
            Tetaz *= Math.PI / 180;
            double buf = x;

            x = Math.Cos(Tetaz) * x - Math.Sin(Tetaz) * y;
            y = Math.Cos(Tetaz) * y + Math.Sin(Tetaz) * buf;
        }


        private void Transform(ref double x, ref double y, ref double z, double Tetax, double Tetay, double Tetaz, ref int ResX, ref int ResY)
        {
            double coef = 35;

            double x_center = ScreenSize.Width / 2;
            double y_center = ScreenSize.Width / 2;

            double TempX = x;
            double TempY = y;
            double TempZ = z;

            RotateX(ref TempY, ref TempZ, ref Tetax);
            RotateY(ref TempX, ref TempZ, Tetay);
            RotateZ(ref TempX, ref TempY, Tetaz);

            ResX = (int)Math.Round(TempX * coef + x_center);
            ResY = (int)Math.Round(TempY * coef + y_center);
        }

        public void HorizonAlgrorithm(Spacing ParX, Spacing ParZ, Graphics Painter, double Tetax, double Tetay, double Tetaz)
        {
            PrepareArray();

            int LeftX = -1, LeftY = -1, RightX = -1, RightY = -1;
            int PrevX = 0, PrevY = 0;

            for (double z = ParZ.End; z >= ParZ.Start; z -= ParZ.Delta)
            {
                double Yp = f(ParX.Start, z);

                Transform(ref ParX.Start, ref Yp, ref z, Tetax, Tetay, Tetaz, ref PrevX, ref PrevY);
                EdgeProcessing(ref PrevX, ref PrevY, ref LeftX, ref LeftY, Painter);
                int Pflag = Visible(PrevX, PrevY);

                for (double x = ParX.Start; x <= ParX.End; x += ParX.Delta)
                {
                    int CurrX = 0, CurrY = 0;
                    int xi = 0, yi = 0;

                    Yp = f(x, z);

                    Transform(ref x, ref Yp, ref z, Tetax, Tetay, Tetaz, ref CurrX, ref CurrY);

                    int Tflag = Visible(CurrX, CurrY);

                    if (Tflag == Pflag)
                    {
                        if (Pflag != 0)
                        {
                            horizon(PrevX, PrevY, CurrX, CurrY, Painter);
                        }
                    }
                    else if (Tflag == 0)
                    {
                        if (Pflag == 1)
                        {
                            GetIntersection(PrevX, PrevY, CurrX, CurrY, Top, ref xi, ref yi);
                        }
                        else
                        {
                            GetIntersection(PrevX, PrevY, CurrX, CurrY, Down, ref xi, ref yi);
                        }

                        horizon(PrevX, PrevY, xi, yi, Painter);
                    }
                    else if (Tflag == 1)
                    {
                        if (Pflag == 0)
                        {
                            GetIntersection(PrevX, PrevY, CurrX, CurrY, Top, ref xi, ref yi);
                            horizon(PrevX, PrevY, xi, yi, Painter);
                        }
                        else
                        {
                            GetIntersection(PrevX, PrevY, CurrX, CurrY, Top, ref xi, ref yi);
                            horizon(PrevX, PrevY, xi, yi, Painter);

                            GetIntersection(PrevX, PrevY, CurrX, CurrY, Down, ref xi, ref yi);
                            horizon(xi, yi, CurrX, CurrY, Painter);
                        }
                    }
                    else
                    {
                        if (Pflag == 0)
                        {
                            GetIntersection(PrevX, PrevY, CurrX, CurrY, Down, ref xi, ref yi);
                            horizon(PrevX, PrevY, xi, yi, Painter);
                        }
                        else
                        {
                            GetIntersection(PrevX, PrevY, CurrX, CurrY, Top, ref xi, ref yi);
                            horizon(PrevX, PrevY, xi, yi, Painter);

                            GetIntersection(PrevX, PrevY, CurrX, CurrY, Down, ref xi, ref yi);
                            horizon(xi, yi, CurrX, CurrY, Painter);
                        }
                    }

                    Pflag = Tflag;
                    PrevX = CurrX;
                    PrevY = CurrY;
                }

                EdgeProcessing(ref PrevX, ref PrevY, ref RightX, ref RightY, Painter);
            }
        }

        static void Swap<T>(ref T a, ref T b)
        {
            T Temp = a;
            a = b;
            b = Temp;
        }
    }
}
