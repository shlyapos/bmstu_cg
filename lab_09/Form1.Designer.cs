namespace lab_09
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label8 = new System.Windows.Forms.Label();
            this.ButtonCutterDraw = new System.Windows.Forms.Button();
            this.ButtonPolygonDraw = new System.Windows.Forms.Button();
            this.ButtonClear = new System.Windows.Forms.Button();
            this.label6 = new System.Windows.Forms.Label();
            this.LabelResultColor = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.LabelPolygonColor = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.LabelCutterColor = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.label8);
            this.groupBox1.Controls.Add(this.ButtonCutterDraw);
            this.groupBox1.Controls.Add(this.ButtonPolygonDraw);
            this.groupBox1.Controls.Add(this.ButtonClear);
            this.groupBox1.Controls.Add(this.label6);
            this.groupBox1.Controls.Add(this.LabelResultColor);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.LabelPolygonColor);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.LabelCutterColor);
            this.groupBox1.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(982, 57);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Параметры";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label8.Location = new System.Drawing.Point(545, 23);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(87, 18);
            this.label8.TabIndex = 1;
            this.label8.Text = "Рисование:";
            // 
            // ButtonCutterDraw
            // 
            this.ButtonCutterDraw.Location = new System.Drawing.Point(638, 14);
            this.ButtonCutterDraw.Name = "ButtonCutterDraw";
            this.ButtonCutterDraw.Size = new System.Drawing.Size(100, 36);
            this.ButtonCutterDraw.TabIndex = 8;
            this.ButtonCutterDraw.Text = "Отсекателя";
            this.ButtonCutterDraw.UseVisualStyleBackColor = true;
            this.ButtonCutterDraw.Click += new System.EventHandler(this.ButtonCutterDraw_Click);
            // 
            // ButtonPolygonDraw
            // 
            this.ButtonPolygonDraw.Location = new System.Drawing.Point(744, 14);
            this.ButtonPolygonDraw.Name = "ButtonPolygonDraw";
            this.ButtonPolygonDraw.Size = new System.Drawing.Size(132, 36);
            this.ButtonPolygonDraw.TabIndex = 7;
            this.ButtonPolygonDraw.Text = "Многоугольника";
            this.ButtonPolygonDraw.UseVisualStyleBackColor = true;
            this.ButtonPolygonDraw.Click += new System.EventHandler(this.ButtonPolygonDraw_Click);
            // 
            // ButtonClear
            // 
            this.ButtonClear.Location = new System.Drawing.Point(893, 14);
            this.ButtonClear.Name = "ButtonClear";
            this.ButtonClear.Size = new System.Drawing.Size(83, 36);
            this.ButtonClear.TabIndex = 6;
            this.ButtonClear.Text = "Очистить";
            this.ButtonClear.UseVisualStyleBackColor = true;
            this.ButtonClear.Click += new System.EventHandler(this.ButtonClear_Click);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(397, 25);
            this.label6.Margin = new System.Windows.Forms.Padding(3);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(124, 18);
            this.label6.TabIndex = 5;
            this.label6.Text = "Цвет результата";
            // 
            // LabelResultColor
            // 
            this.LabelResultColor.BackColor = System.Drawing.Color.Black;
            this.LabelResultColor.Location = new System.Drawing.Point(366, 23);
            this.LabelResultColor.Margin = new System.Windows.Forms.Padding(3);
            this.LabelResultColor.Name = "LabelResultColor";
            this.LabelResultColor.Size = new System.Drawing.Size(25, 25);
            this.LabelResultColor.TabIndex = 4;
            this.LabelResultColor.Click += new System.EventHandler(this.LabelResultColor_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(200, 25);
            this.label4.Margin = new System.Windows.Forms.Padding(3);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(160, 18);
            this.label4.TabIndex = 3;
            this.label4.Text = "Цвет многоугольника";
            // 
            // LabelPolygonColor
            // 
            this.LabelPolygonColor.BackColor = System.Drawing.Color.Black;
            this.LabelPolygonColor.Location = new System.Drawing.Point(169, 23);
            this.LabelPolygonColor.Margin = new System.Windows.Forms.Padding(3);
            this.LabelPolygonColor.Name = "LabelPolygonColor";
            this.LabelPolygonColor.Size = new System.Drawing.Size(25, 25);
            this.LabelPolygonColor.TabIndex = 2;
            this.LabelPolygonColor.Click += new System.EventHandler(this.LabelSegmentColor_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(37, 25);
            this.label2.Margin = new System.Windows.Forms.Padding(3);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(126, 18);
            this.label2.TabIndex = 1;
            this.label2.Text = "Цвет отсекателя";
            // 
            // LabelCutterColor
            // 
            this.LabelCutterColor.BackColor = System.Drawing.Color.Black;
            this.LabelCutterColor.Location = new System.Drawing.Point(6, 23);
            this.LabelCutterColor.Margin = new System.Windows.Forms.Padding(3);
            this.LabelCutterColor.Name = "LabelCutterColor";
            this.LabelCutterColor.Size = new System.Drawing.Size(25, 25);
            this.LabelCutterColor.TabIndex = 0;
            this.LabelCutterColor.Click += new System.EventHandler(this.LabelCutterColor_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.White;
            this.pictureBox1.Location = new System.Drawing.Point(12, 75);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(982, 634);
            this.pictureBox1.TabIndex = 1;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.MouseClick += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseClick);
            this.pictureBox1.MouseDoubleClick += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseDoubleClick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1006, 721);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Button ButtonCutterDraw;
        private System.Windows.Forms.Button ButtonPolygonDraw;
        private System.Windows.Forms.Button ButtonClear;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label LabelResultColor;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label LabelPolygonColor;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label LabelCutterColor;
        private System.Windows.Forms.PictureBox pictureBox1;
    }
}

