namespace lab_08
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
            this.ButtonClear = new System.Windows.Forms.Button();
            this.ButtonSegmentDraw = new System.Windows.Forms.Button();
            this.ButtonCutterDraw = new System.Windows.Forms.Button();
            this.label6 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.LabelResultColor = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.LabelSegmentColor = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.LabelCutterColor = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.ButtonClear);
            this.groupBox1.Controls.Add(this.ButtonSegmentDraw);
            this.groupBox1.Controls.Add(this.ButtonCutterDraw);
            this.groupBox1.Controls.Add(this.label6);
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.LabelResultColor);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.LabelSegmentColor);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.LabelCutterColor);
            this.groupBox1.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(982, 55);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Параметры";
            // 
            // ButtonClear
            // 
            this.ButtonClear.Location = new System.Drawing.Point(849, 14);
            this.ButtonClear.Name = "ButtonClear";
            this.ButtonClear.Size = new System.Drawing.Size(127, 35);
            this.ButtonClear.TabIndex = 9;
            this.ButtonClear.Text = "Очистить экран";
            this.ButtonClear.UseVisualStyleBackColor = true;
            this.ButtonClear.Click += new System.EventHandler(this.ButtonClear_Click);
            // 
            // ButtonSegmentDraw
            // 
            this.ButtonSegmentDraw.Location = new System.Drawing.Point(705, 14);
            this.ButtonSegmentDraw.Name = "ButtonSegmentDraw";
            this.ButtonSegmentDraw.Size = new System.Drawing.Size(99, 35);
            this.ButtonSegmentDraw.TabIndex = 8;
            this.ButtonSegmentDraw.Text = "Отрезков";
            this.ButtonSegmentDraw.UseVisualStyleBackColor = true;
            this.ButtonSegmentDraw.Click += new System.EventHandler(this.ButtonSegmentDraw_Click);
            // 
            // ButtonCutterDraw
            // 
            this.ButtonCutterDraw.Location = new System.Drawing.Point(600, 14);
            this.ButtonCutterDraw.Name = "ButtonCutterDraw";
            this.ButtonCutterDraw.Size = new System.Drawing.Size(99, 35);
            this.ButtonCutterDraw.TabIndex = 7;
            this.ButtonCutterDraw.Text = "Отсекателя";
            this.ButtonCutterDraw.UseVisualStyleBackColor = true;
            this.ButtonCutterDraw.Click += new System.EventHandler(this.ButtonCutterDraw_Click);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(507, 24);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(87, 18);
            this.label6.TabIndex = 6;
            this.label6.Text = "Рисование:";
            this.label6.Click += new System.EventHandler(this.label6_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(339, 24);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(124, 18);
            this.label5.TabIndex = 5;
            this.label5.Text = "Цвет результата";
            this.label5.Click += new System.EventHandler(this.label5_Click);
            // 
            // LabelResultColor
            // 
            this.LabelResultColor.BackColor = System.Drawing.Color.Black;
            this.LabelResultColor.Location = new System.Drawing.Point(308, 24);
            this.LabelResultColor.Name = "LabelResultColor";
            this.LabelResultColor.Padding = new System.Windows.Forms.Padding(3);
            this.LabelResultColor.Size = new System.Drawing.Size(25, 25);
            this.LabelResultColor.TabIndex = 4;
            this.LabelResultColor.Click += new System.EventHandler(this.LabelResultColor_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(200, 24);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(102, 18);
            this.label3.TabIndex = 3;
            this.label3.Text = "Цвет отрезка";
            // 
            // LabelSegmentColor
            // 
            this.LabelSegmentColor.BackColor = System.Drawing.Color.Black;
            this.LabelSegmentColor.Location = new System.Drawing.Point(169, 24);
            this.LabelSegmentColor.Name = "LabelSegmentColor";
            this.LabelSegmentColor.Padding = new System.Windows.Forms.Padding(3);
            this.LabelSegmentColor.Size = new System.Drawing.Size(25, 25);
            this.LabelSegmentColor.TabIndex = 2;
            this.LabelSegmentColor.Click += new System.EventHandler(this.LabelSegmentColor_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(37, 24);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(126, 18);
            this.label1.TabIndex = 1;
            this.label1.Text = "Цвет отсекателя";
            // 
            // LabelCutterColor
            // 
            this.LabelCutterColor.BackColor = System.Drawing.Color.Black;
            this.LabelCutterColor.Location = new System.Drawing.Point(6, 24);
            this.LabelCutterColor.Name = "LabelCutterColor";
            this.LabelCutterColor.Padding = new System.Windows.Forms.Padding(3);
            this.LabelCutterColor.Size = new System.Drawing.Size(25, 25);
            this.LabelCutterColor.TabIndex = 0;
            this.LabelCutterColor.Click += new System.EventHandler(this.LabelCutterColor_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.White;
            this.pictureBox1.ErrorImage = null;
            this.pictureBox1.InitialImage = null;
            this.pictureBox1.Location = new System.Drawing.Point(12, 73);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(982, 636);
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
        private System.Windows.Forms.Button ButtonClear;
        private System.Windows.Forms.Button ButtonSegmentDraw;
        private System.Windows.Forms.Button ButtonCutterDraw;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label LabelResultColor;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label LabelSegmentColor;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label LabelCutterColor;
        private System.Windows.Forms.PictureBox pictureBox1;
    }
}

