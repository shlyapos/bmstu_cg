using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows;

namespace lab_08
{
    class Cutter
    {
        // Вершины отсекателя
        private List<PointF> Peaks;
        private List<Vector> Normals;

        private int Direction = 0;

        public Cutter()
        {
            Peaks = new List<PointF>();
            Normals = new List<Vector>();
        }


        public void AddPeak(PointF NewPeak)
        {
            Peaks.Add(NewPeak);
        }

        public PointF GetPeak(int index)
        {
            if (index >= 0)
            {
                return Peaks[index % Peaks.Count];
            }
            else
            {
                return Peaks[Peaks.Count + index];
            }
        }

        public void Clear()
        {
            Peaks.Clear();
            Normals.Clear();
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
            Vector b = new Vector();

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


        private void GetNormals()
        {
            Vector b;
            double tmp;
            Normals.Clear();

            for (int i = 0; i < Peaks.Count; i++)
            {
                PointF Temp1 = GetPeak(i + 1);
                PointF Temp2 = GetPeak(i);

                b = new Vector(Temp1.X - Temp2.X, Temp1.Y - Temp2.Y);

                tmp = b.X;
                b.X = b.Y;
                b.Y = tmp;

                if (Direction == -1)
                {
                    b.Y *= -1;
                }
                else
                {
                    b.X *= -1;
                }

                Normals.Add(b);
            }
        }

        private float ScalarMultVector(Vector v1, Vector v2)
        {
            return (float)(v1.X * v2.X + v1.Y * v2.Y);
        }

        public Segment CutSegment(PointF P1, PointF P2)
        {
            // Получение заранее нормалей
            GetNormals();

            float T_down = 0;
            float T_up = 1;
            float T_tmp;

            float D_sc, W_sc;

            Vector D = new Vector(P2.X - P1.X, P2.Y - P1.Y);
            Vector w;

            for (int i = 0; i < Peaks.Count; i++)
            {
                w = new Vector(P1.X - Peaks[i].X, P1.Y - Peaks[i].Y);

                D_sc = ScalarMultVector(D, Normals[i]);
                W_sc = ScalarMultVector(w, Normals[i]);

                // Отрезок выродился в точку / D и сторона параллельны
                if (D_sc == 0)
                {
                    if (W_sc < 0)
                    {
                        return new Segment();
                    }
                    // Точка видима относительно текущей границы
                }
                else
                {
                    T_tmp = -W_sc / D_sc;

                    if (D_sc > 0) // Поиск нижнего предела
                    {
                        if (T_tmp > 1)
                        {
                            return new Segment();
                        }

                        T_down = Math.Max(T_down, T_tmp);
                    }
                    else // Поиск верхнего предела
                    {
                        if (T_tmp < 0)
                        {
                            return new Segment();
                        }

                        T_up = Math.Min(T_up, T_tmp);
                    }
                }
            }

            if (T_down > T_up)
            {
                return new Segment();
            }

            PointF Tmp1 = new PointF(P1.X + (P2.X - P1.X) * T_down, P1.Y + (P2.Y - P1.Y) * T_down);
            PointF Tmp2 = new PointF(P1.X + (P2.X - P1.X) * T_up, P1.Y + (P2.Y - P1.Y) * T_up);

            return new Segment(Tmp1, Tmp2);
        }
    }
}
