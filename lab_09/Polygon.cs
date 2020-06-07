using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;

namespace lab_09
{
    class Polygon
    {
        protected List<PointF> Peaks;

        public Polygon()
        {
            Peaks = new List<PointF>();
        }

        public void AddPeak(PointF NewPeak)
        {
            Peaks.Add(NewPeak);
        }

        public PointF GetPeak(int Index)
        {
            if (Index >= 0)
            {
                return Peaks[Index % Peaks.Count];
            }
            else
            {
                return Peaks[Peaks.Count + Index];
            }
        }

        public PointF GetLast()
        {
            return Peaks[Peaks.Count - 1];
        }

        public void AddRange(List<PointF> Range)
        {
            Peaks.AddRange(Range);
        }

        public int Count()
        {
            return Peaks.Count;
        }

        public virtual void Clear()
        {
            Peaks.Clear();
        }

        public PointF[] ToArray()
        {
            return Peaks.ToArray();
        }
    }
}
