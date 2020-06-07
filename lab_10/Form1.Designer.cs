namespace lab_10
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
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.NumUpDownXStep = new System.Windows.Forms.NumericUpDown();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.NumUpDownXRight = new System.Windows.Forms.NumericUpDown();
            this.NumUpDownXLeft = new System.Windows.Forms.NumericUpDown();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.NumUpDownZStep = new System.Windows.Forms.NumericUpDown();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.NumUpDownZRight = new System.Windows.Forms.NumericUpDown();
            this.NumUpDownZLeft = new System.Windows.Forms.NumericUpDown();
            this.ButtonDraw = new System.Windows.Forms.Button();
            this.ButtonClear = new System.Windows.Forms.Button();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.label7 = new System.Windows.Forms.Label();
            this.TrackBarZ = new System.Windows.Forms.TrackBar();
            this.label6 = new System.Windows.Forms.Label();
            this.TrackBarY = new System.Windows.Forms.TrackBar();
            this.label5 = new System.Windows.Forms.Label();
            this.TrackBarX = new System.Windows.Forms.TrackBar();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.NumUpDownXStep)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.NumUpDownXRight)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.NumUpDownXLeft)).BeginInit();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.NumUpDownZStep)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.NumUpDownZRight)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.NumUpDownZLeft)).BeginInit();
            this.groupBox3.SuspendLayout();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.TrackBarZ)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.TrackBarY)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.TrackBarX)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.Black;
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(945, 710);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.NumUpDownXStep);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.NumUpDownXRight);
            this.groupBox1.Controls.Add(this.NumUpDownXLeft);
            this.groupBox1.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.groupBox1.Location = new System.Drawing.Point(963, 42);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(261, 94);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Параметры X";
            // 
            // NumUpDownXStep
            // 
            this.NumUpDownXStep.DecimalPlaces = 2;
            this.NumUpDownXStep.Increment = new decimal(new int[] {
            1,
            0,
            0,
            131072});
            this.NumUpDownXStep.Location = new System.Drawing.Point(91, 56);
            this.NumUpDownXStep.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            131072});
            this.NumUpDownXStep.Name = "NumUpDownXStep";
            this.NumUpDownXStep.Size = new System.Drawing.Size(76, 24);
            this.NumUpDownXStep.TabIndex = 7;
            this.NumUpDownXStep.Value = new decimal(new int[] {
            1,
            0,
            0,
            65536});
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(46, 58);
            this.label2.Margin = new System.Windows.Forms.Padding(3);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(39, 18);
            this.label2.TabIndex = 6;
            this.label2.Text = "Шаг:";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 25);
            this.label1.Margin = new System.Windows.Forms.Padding(3);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(79, 18);
            this.label1.TabIndex = 4;
            this.label1.Text = "Интервал:";
            // 
            // NumUpDownXRight
            // 
            this.NumUpDownXRight.Location = new System.Drawing.Point(173, 25);
            this.NumUpDownXRight.Minimum = new decimal(new int[] {
            100,
            0,
            0,
            -2147483648});
            this.NumUpDownXRight.Name = "NumUpDownXRight";
            this.NumUpDownXRight.Size = new System.Drawing.Size(76, 24);
            this.NumUpDownXRight.TabIndex = 5;
            this.NumUpDownXRight.Value = new decimal(new int[] {
            4,
            0,
            0,
            0});
            // 
            // NumUpDownXLeft
            // 
            this.NumUpDownXLeft.Location = new System.Drawing.Point(91, 25);
            this.NumUpDownXLeft.Minimum = new decimal(new int[] {
            100,
            0,
            0,
            -2147483648});
            this.NumUpDownXLeft.Name = "NumUpDownXLeft";
            this.NumUpDownXLeft.Size = new System.Drawing.Size(76, 24);
            this.NumUpDownXLeft.TabIndex = 4;
            this.NumUpDownXLeft.Value = new decimal(new int[] {
            4,
            0,
            0,
            -2147483648});
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Items.AddRange(new object[] {
            "y = (x + z) / 2",
            "y = sin(x) * cos(z)",
            "y = sin(x) + cos(z)",
            "y = √(x² + z²) - 3;",
            "y = sin(x)² - cos(z)²",
            "y = |sin(x) * cos(z)|",
            "y = x * sin(√(x² + z²))",
            "y = sin(x * z)"});
            this.comboBox1.Location = new System.Drawing.Point(963, 12);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(261, 24);
            this.comboBox1.TabIndex = 3;
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.NumUpDownZStep);
            this.groupBox2.Controls.Add(this.label3);
            this.groupBox2.Controls.Add(this.label4);
            this.groupBox2.Controls.Add(this.NumUpDownZRight);
            this.groupBox2.Controls.Add(this.NumUpDownZLeft);
            this.groupBox2.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.groupBox2.Location = new System.Drawing.Point(963, 142);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(261, 94);
            this.groupBox2.TabIndex = 8;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Параметры Z";
            // 
            // NumUpDownZStep
            // 
            this.NumUpDownZStep.DecimalPlaces = 2;
            this.NumUpDownZStep.Increment = new decimal(new int[] {
            1,
            0,
            0,
            131072});
            this.NumUpDownZStep.Location = new System.Drawing.Point(91, 56);
            this.NumUpDownZStep.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            131072});
            this.NumUpDownZStep.Name = "NumUpDownZStep";
            this.NumUpDownZStep.Size = new System.Drawing.Size(76, 24);
            this.NumUpDownZStep.TabIndex = 7;
            this.NumUpDownZStep.Value = new decimal(new int[] {
            1,
            0,
            0,
            65536});
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(46, 58);
            this.label3.Margin = new System.Windows.Forms.Padding(3);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(39, 18);
            this.label3.TabIndex = 6;
            this.label3.Text = "Шаг:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(6, 25);
            this.label4.Margin = new System.Windows.Forms.Padding(3);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(79, 18);
            this.label4.TabIndex = 4;
            this.label4.Text = "Интервал:";
            // 
            // NumUpDownZRight
            // 
            this.NumUpDownZRight.Location = new System.Drawing.Point(173, 25);
            this.NumUpDownZRight.Minimum = new decimal(new int[] {
            100,
            0,
            0,
            -2147483648});
            this.NumUpDownZRight.Name = "NumUpDownZRight";
            this.NumUpDownZRight.Size = new System.Drawing.Size(76, 24);
            this.NumUpDownZRight.TabIndex = 5;
            this.NumUpDownZRight.Value = new decimal(new int[] {
            4,
            0,
            0,
            0});
            // 
            // NumUpDownZLeft
            // 
            this.NumUpDownZLeft.Location = new System.Drawing.Point(91, 25);
            this.NumUpDownZLeft.Minimum = new decimal(new int[] {
            100,
            0,
            0,
            -2147483648});
            this.NumUpDownZLeft.Name = "NumUpDownZLeft";
            this.NumUpDownZLeft.Size = new System.Drawing.Size(76, 24);
            this.NumUpDownZLeft.TabIndex = 4;
            this.NumUpDownZLeft.Value = new decimal(new int[] {
            4,
            0,
            0,
            -2147483648});
            // 
            // ButtonDraw
            // 
            this.ButtonDraw.Location = new System.Drawing.Point(963, 648);
            this.ButtonDraw.Name = "ButtonDraw";
            this.ButtonDraw.Size = new System.Drawing.Size(261, 34);
            this.ButtonDraw.TabIndex = 9;
            this.ButtonDraw.Text = "Изобразить";
            this.ButtonDraw.UseVisualStyleBackColor = true;
            this.ButtonDraw.Click += new System.EventHandler(this.ButtonDraw_Click);
            // 
            // ButtonClear
            // 
            this.ButtonClear.Location = new System.Drawing.Point(963, 688);
            this.ButtonClear.Name = "ButtonClear";
            this.ButtonClear.Size = new System.Drawing.Size(261, 34);
            this.ButtonClear.TabIndex = 10;
            this.ButtonClear.Text = "Очистить";
            this.ButtonClear.UseVisualStyleBackColor = true;
            this.ButtonClear.Click += new System.EventHandler(this.ButtonClear_Click);
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.panel1);
            this.groupBox3.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.groupBox3.Location = new System.Drawing.Point(963, 242);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(261, 400);
            this.groupBox3.TabIndex = 12;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Повороты";
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.label7);
            this.panel1.Controls.Add(this.TrackBarZ);
            this.panel1.Controls.Add(this.label6);
            this.panel1.Controls.Add(this.TrackBarY);
            this.panel1.Controls.Add(this.label5);
            this.panel1.Controls.Add(this.TrackBarX);
            this.panel1.Location = new System.Drawing.Point(39, 23);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(179, 371);
            this.panel1.TabIndex = 13;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(142, 3);
            this.label7.Margin = new System.Windows.Forms.Padding(3);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(17, 18);
            this.label7.TabIndex = 16;
            this.label7.Text = "Z";
            // 
            // TrackBarZ
            // 
            this.TrackBarZ.Location = new System.Drawing.Point(127, 21);
            this.TrackBarZ.Maximum = 180;
            this.TrackBarZ.Minimum = -180;
            this.TrackBarZ.Name = "TrackBarZ";
            this.TrackBarZ.Orientation = System.Windows.Forms.Orientation.Vertical;
            this.TrackBarZ.Size = new System.Drawing.Size(56, 347);
            this.TrackBarZ.SmallChange = 5;
            this.TrackBarZ.TabIndex = 15;
            this.TrackBarZ.TickStyle = System.Windows.Forms.TickStyle.Both;
            this.TrackBarZ.Scroll += new System.EventHandler(this.TrackBarZ_Scroll);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(80, 3);
            this.label6.Margin = new System.Windows.Forms.Padding(3);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(17, 18);
            this.label6.TabIndex = 14;
            this.label6.Text = "Y";
            // 
            // TrackBarY
            // 
            this.TrackBarY.Location = new System.Drawing.Point(65, 21);
            this.TrackBarY.Maximum = 180;
            this.TrackBarY.Minimum = -180;
            this.TrackBarY.Name = "TrackBarY";
            this.TrackBarY.Orientation = System.Windows.Forms.Orientation.Vertical;
            this.TrackBarY.Size = new System.Drawing.Size(56, 347);
            this.TrackBarY.SmallChange = 5;
            this.TrackBarY.TabIndex = 13;
            this.TrackBarY.TickStyle = System.Windows.Forms.TickStyle.Both;
            this.TrackBarY.Scroll += new System.EventHandler(this.TrackBarY_Scroll);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(18, 3);
            this.label5.Margin = new System.Windows.Forms.Padding(3);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(18, 18);
            this.label5.TabIndex = 12;
            this.label5.Text = "X";
            // 
            // TrackBarX
            // 
            this.TrackBarX.Location = new System.Drawing.Point(3, 21);
            this.TrackBarX.Maximum = 180;
            this.TrackBarX.Minimum = -180;
            this.TrackBarX.Name = "TrackBarX";
            this.TrackBarX.Orientation = System.Windows.Forms.Orientation.Vertical;
            this.TrackBarX.Size = new System.Drawing.Size(56, 347);
            this.TrackBarX.SmallChange = 5;
            this.TrackBarX.TabIndex = 11;
            this.TrackBarX.TickStyle = System.Windows.Forms.TickStyle.Both;
            this.TrackBarX.Scroll += new System.EventHandler(this.TrackBarX_Scroll);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1236, 734);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.ButtonClear);
            this.Controls.Add(this.ButtonDraw);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.NumUpDownXStep)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.NumUpDownXRight)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.NumUpDownXLeft)).EndInit();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.NumUpDownZStep)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.NumUpDownZRight)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.NumUpDownZLeft)).EndInit();
            this.groupBox3.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.TrackBarZ)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.TrackBarY)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.TrackBarX)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.NumericUpDown NumUpDownXLeft;
        private System.Windows.Forms.NumericUpDown NumUpDownXStep;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.NumericUpDown NumUpDownXRight;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.NumericUpDown NumUpDownZStep;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.NumericUpDown NumUpDownZRight;
        private System.Windows.Forms.NumericUpDown NumUpDownZLeft;
        private System.Windows.Forms.Button ButtonDraw;
        private System.Windows.Forms.Button ButtonClear;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TrackBar TrackBarZ;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TrackBar TrackBarY;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TrackBar TrackBarX;
    }
}

