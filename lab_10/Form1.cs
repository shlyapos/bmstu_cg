using System;
using System.Drawing;
using System.Windows.Forms;

namespace lab_10
{
    public partial class Form1 : Form
    {
        Bitmap ResultPicture;
        Graphics Canvas;
        Pen PenDraw;
        Horizon horizon;

        public Form1()
        {
            InitializeComponent();
            comboBox1.SelectedIndex = 0;
            comboBox1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;

            // Graphic options
            ResultPicture = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Canvas = Graphics.FromImage(ResultPicture);
            pictureBox1.Image = ResultPicture;

            PenDraw = new Pen(Color.White, 1);
        }

        private double f1(double x, double z) => (x + z) / 2;
        private double f2(double x, double z) => Math.Sin(x) * Math.Cos(z);
        private double f3(double x, double z) => Math.Sin(x) + Math.Cos(z);
        private double f4(double x, double z) => Math.Sqrt(x * x + z * z) - 3;
        private double f5(double x, double z)
        {
            double sX = Math.Sin(x);
            double cZ = Math.Cos(z);

            return sX * sX - cZ * cZ;
        }
        private double f6(double x, double z) => Math.Abs(Math.Sin(x) * Math.Cos(z));
        private double f7(double x, double z) => x * Math.Sin(Math.Sqrt(x * x + z * z)); 
        private double f8(double x, double z) => Math.Sin(x * z);

        private Func<double, double, double> GetFunction()
        {
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                    return f1;
                case 1:
                    return f2;
                case 2:
                    return f3;
                case 3:
                    return f4;
                case 4:
                    return f5;
                case 5:
                    return f6;
                case 6:
                    return f7;
                default:
                    return f8;
            }
        }


        private Spacing GetXSpacing()
        {
            Spacing X = new Spacing();

            X.Start = Convert.ToDouble(NumUpDownXLeft.Value);
            X.End = Convert.ToDouble(NumUpDownXRight.Value);
            X.Delta = Convert.ToDouble(NumUpDownXStep.Value);

            return X;
        }

        private Spacing GetZSpacing()
        {
            Spacing Z = new Spacing();

            Z.Start = Convert.ToDouble(NumUpDownZLeft.Value);
            Z.End = Convert.ToDouble(NumUpDownZRight.Value);
            Z.Delta = Convert.ToDouble(NumUpDownZStep.Value);

            return Z;
        }

        private void AlgorithmProcessing()
        {
            pictureBox1.Refresh();
            Canvas.Clear(Color.Black);

            Spacing x = GetXSpacing();
            Spacing z = GetZSpacing();

            double Ox = Convert.ToDouble(TrackBarX.Value);
            double Oy = Convert.ToDouble(TrackBarY.Value);
            double Oz = Convert.ToDouble(TrackBarZ.Value);

            var f = GetFunction();

            horizon = new Horizon(PenDraw, pictureBox1.Size, f);
            horizon.HorizonAlgrorithm(x, z, Canvas, Ox, Oy, Oz);
            pictureBox1.Refresh();
        }

        private void ButtonDraw_Click(object sender, EventArgs e)
        {
            TrackBarX.Value = 0;
            TrackBarY.Value = 0;
            TrackBarZ.Value = 0;

            AlgorithmProcessing();
        }

        private void TrackBarX_Scroll(object sender, EventArgs e)
        {
            AlgorithmProcessing();
        }

        private void TrackBarY_Scroll(object sender, EventArgs e)
        {
            AlgorithmProcessing();
        }

        private void TrackBarZ_Scroll(object sender, EventArgs e)
        {
            AlgorithmProcessing();
        }

        private void ButtonClear_Click(object sender, EventArgs e)
        {
            Canvas.Clear(Color.Black);
            pictureBox1.Refresh();
        }
    }
}
