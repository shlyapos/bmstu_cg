using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows;

namespace lab_09
{
    class Cutter : Polygon
    {
        private int Direction = 0;

        public Cutter() : base()
        {
        }

        public override void Clear()
        {
            Peaks.Clear();
            Direction = 0;
        }

        public void ConvexCheck()
        {
            if (Peaks.Count < 3)
            {
                Direction = 0;
                return;
            }

            Vector a = new Vector(Peaks[1].X - Peaks[0].X, Peaks[1].Y - Peaks[0].Y);
            Vector b;

            double Temp;

            int sign = 0;

            for (int i = 0; i < Peaks.Count; i++)
            {
                PointF Temp1 = GetPeak(i + 1);
                PointF Temp2 = GetPeak(i);

                b = new Vector(Temp1.X - Temp2.X, Temp1.Y - Temp2.Y);

                Temp = a.X * b.Y - a.Y * b.X;

                if (sign == 0)
                {
                    sign = Math.Sign(Temp);
                }
                else if ((sign != Math.Sign(Temp)) && (Temp != 0))
                {
                    Direction = 0;
                    return;
                }

                a = b;
            }

            Direction = sign;
        }

        public bool IsConvex()
        {
            if (Direction == 0)
            {
                return false;
            }
            else
            {
                return true;
            }
        }


        private bool VisiblePeak(PointF P1, PointF P2, Vector Normal)
        {
            Vector Tmp = new Vector(P2.X - P1.X, P2.Y - P1.Y);
            float res = ScalarMultVector(Tmp, Normal);
            return res < 0;
        }

        private Vector GetNormal(PointF P1, PointF P2)
        {
            double Temp;
            Vector Normal = new Vector(P2.X - P1.X, P2.Y - P1.Y);

            Temp = Normal.X;
            Normal.X = Normal.Y;
            Normal.Y = Temp;

            if (Direction == -1)
            {
                Normal.Y *= -1;
            }
            else
            {
                Normal.X *= -1;
            }

            return Normal;
        }

        private float ScalarMultVector(Vector v1, Vector v2)
        {
            return (float)(v1.X * v2.X + v1.Y * v2.Y);
        }

        public Polygon CutPolygon(Polygon P)
        {
            PointF I, Tmp1, Tmp2;
            Vector Nv, D, W;
            List<PointF> Q = new List<PointF>();

            Peaks.Add(Peaks[0]);

            double Dsk, Wsk, t;

            // Обход по всем сторонам отсекателя
            for (int i = 1; i < Peaks.Count; i++)
            {
                Nv = GetNormal(Peaks[i - 1], Peaks[i]);

                if (VisiblePeak(P.GetPeak(0), Peaks[i], Nv))
                {
                    Q.Add(P.GetPeak(0));
                }

                // Обход по всем сторонам многоугольника
                for (int j = 1; j < P.Count(); j++)
                {
                    Tmp1 = P.GetPeak(j - 1);
                    Tmp2 = P.GetPeak(j);

                    // Вектор отрезка
                    D = new Vector(Tmp2.X - Tmp1.X, Tmp2.Y - Tmp1.Y);
                    // Угол и с какой он стороны
                    Dsk = ScalarMultVector(D, Nv);

                    // Проверка, что отрезок не вырождается в точку и не параллелен
                    if (Dsk != 0)
                    {
                        // Вектор, который соединяет начало отрезка и вершину многоугольника
                        W = new Vector(Tmp1.X - Peaks[i - 1].X, Tmp1.Y - Peaks[i - 1].Y);
                        Wsk = ScalarMultVector(W, Nv);

                        t = -Wsk / Dsk;

                        if (t >= 0 && t <= 1)
                        {
                            I = new PointF((float)(P.GetPeak(j - 1).X + t * D.X), (float)(P.GetPeak(j - 1).Y + t * D.Y));
                            Q.Add(I);
                        }
                    }

                    if (VisiblePeak(P.GetPeak(j), Peaks[i], Nv))
                    {
                        Q.Add(P.GetPeak(j));
                    }
                }

                Q.Add(Q[0]);
                P.Clear();
                P.AddRange(Q);
                Q.Clear();
            }

            return P;
        }
    }
}
