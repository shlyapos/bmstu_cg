namespace lab_07
{
    partial class MainWindow
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
            this.components = new System.ComponentModel.Container();
            this.label1 = new System.Windows.Forms.Label();
            this.lbl_cutter_clr = new System.Windows.Forms.Label();
            this.lbl_line_clr = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.bindingSource1 = new System.Windows.Forms.BindingSource(this.components);
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label2 = new System.Windows.Forms.Label();
            this.ButtonLineDraw = new System.Windows.Forms.Button();
            this.ButtonCutterDraw = new System.Windows.Forms.Button();
            this.ButtonClear = new System.Windows.Forms.Button();
            this.lbl_result_clr = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource1)).BeginInit();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label1.Location = new System.Drawing.Point(37, 26);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(126, 18);
            this.label1.TabIndex = 0;
            this.label1.Text = "Цвет отсекателя";
            // 
            // lbl_cutter_clr
            // 
            this.lbl_cutter_clr.BackColor = System.Drawing.Color.Black;
            this.lbl_cutter_clr.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lbl_cutter_clr.Location = new System.Drawing.Point(6, 25);
            this.lbl_cutter_clr.Margin = new System.Windows.Forms.Padding(3);
            this.lbl_cutter_clr.Name = "lbl_cutter_clr";
            this.lbl_cutter_clr.Size = new System.Drawing.Size(25, 25);
            this.lbl_cutter_clr.TabIndex = 3;
            this.lbl_cutter_clr.Click += new System.EventHandler(this.lbl_cutter_clr_Click);
            // 
            // lbl_line_clr
            // 
            this.lbl_line_clr.BackColor = System.Drawing.Color.Black;
            this.lbl_line_clr.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lbl_line_clr.Location = new System.Drawing.Point(169, 25);
            this.lbl_line_clr.Margin = new System.Windows.Forms.Padding(3);
            this.lbl_line_clr.Name = "lbl_line_clr";
            this.lbl_line_clr.Padding = new System.Windows.Forms.Padding(3);
            this.lbl_line_clr.Size = new System.Drawing.Size(25, 25);
            this.lbl_line_clr.TabIndex = 4;
            this.lbl_line_clr.Click += new System.EventHandler(this.lbl_line_clr_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label3.Location = new System.Drawing.Point(200, 25);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(102, 18);
            this.label3.TabIndex = 5;
            this.label3.Text = "Цвет отрезка";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label5.Location = new System.Drawing.Point(339, 25);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(124, 18);
            this.label5.TabIndex = 7;
            this.label5.Text = "Цвет результата";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.ButtonLineDraw);
            this.groupBox1.Controls.Add(this.ButtonCutterDraw);
            this.groupBox1.Controls.Add(this.ButtonClear);
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.lbl_cutter_clr);
            this.groupBox1.Controls.Add(this.lbl_result_clr);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.lbl_line_clr);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.groupBox1.Size = new System.Drawing.Size(982, 64);
            this.groupBox1.TabIndex = 8;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Параметры";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label2.Location = new System.Drawing.Point(484, 25);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(104, 20);
            this.label2.TabIndex = 13;
            this.label2.Text = "Рисование:";
            // 
            // ButtonLineDraw
            // 
            this.ButtonLineDraw.Location = new System.Drawing.Point(700, 16);
            this.ButtonLineDraw.Name = "ButtonLineDraw";
            this.ButtonLineDraw.Size = new System.Drawing.Size(100, 38);
            this.ButtonLineDraw.TabIndex = 12;
            this.ButtonLineDraw.Text = "Отрезков";
            this.ButtonLineDraw.UseVisualStyleBackColor = true;
            this.ButtonLineDraw.Click += new System.EventHandler(this.ButtonLineDraw_Click);
            // 
            // ButtonCutterDraw
            // 
            this.ButtonCutterDraw.Location = new System.Drawing.Point(594, 16);
            this.ButtonCutterDraw.Name = "ButtonCutterDraw";
            this.ButtonCutterDraw.Size = new System.Drawing.Size(100, 38);
            this.ButtonCutterDraw.TabIndex = 11;
            this.ButtonCutterDraw.Text = "Отсекателя";
            this.ButtonCutterDraw.UseVisualStyleBackColor = true;
            this.ButtonCutterDraw.Click += new System.EventHandler(this.ButtonCutterDraw_Click);
            // 
            // ButtonClear
            // 
            this.ButtonClear.Location = new System.Drawing.Point(848, 16);
            this.ButtonClear.Name = "ButtonClear";
            this.ButtonClear.Size = new System.Drawing.Size(128, 38);
            this.ButtonClear.TabIndex = 10;
            this.ButtonClear.Text = "Очистить экран";
            this.ButtonClear.UseVisualStyleBackColor = true;
            this.ButtonClear.Click += new System.EventHandler(this.ButtonClear_Click);
            // 
            // lbl_result_clr
            // 
            this.lbl_result_clr.BackColor = System.Drawing.Color.Black;
            this.lbl_result_clr.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lbl_result_clr.Location = new System.Drawing.Point(308, 26);
            this.lbl_result_clr.Margin = new System.Windows.Forms.Padding(3);
            this.lbl_result_clr.Name = "lbl_result_clr";
            this.lbl_result_clr.Size = new System.Drawing.Size(25, 25);
            this.lbl_result_clr.TabIndex = 6;
            this.lbl_result_clr.Click += new System.EventHandler(this.lbl_result_clr_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(12, 82);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(982, 627);
            this.pictureBox1.TabIndex = 9;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.MouseClick += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseClick);
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1006, 721);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.groupBox1);
            this.Name = "MainWindow";
            this.Text = "Cutters";
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lbl_cutter_clr;
        private System.Windows.Forms.Label lbl_line_clr;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.BindingSource bindingSource1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label lbl_result_clr;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button ButtonClear;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button ButtonLineDraw;
        private System.Windows.Forms.Button ButtonCutterDraw;
    }
}

