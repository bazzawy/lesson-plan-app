from flask import Flask, render_template, request, send_file
import pdfkit
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def lesson_plan():
    if request.method == 'POST':
        lesson_data = {
            "عنوان الدرس": request.form['lesson_title'],
            "الفصل": request.form['grade_level'],
            "الحصة حسب الجدول": request.form['session_schedule'],
            "التهيئة الحافزة": request.form['motivation'],
            "المفاهيم الجديدة": request.form['new_concepts'],
            "عملية التعليم والتعلم": request.form['learning_process'],
            "نواتج التعلم": request.form['learning_outcomes'],
            "خطوات الدرس": request.form['lesson_steps'],
            "التقييم": request.form['assessment'],
            "الزمن": request.form['duration'],
            "طرائق التدريس": request.form['teaching_methods'],
            "الأنشطة والوسائل المستخدمة": request.form['activities_and_tools'],
            "مهارات القرن الواحد والعشرين": request.form['twenty_first_century_skills'],
            "الربط مع المواد الأخرى": request.form['cross_subject_links'],
            "المواطنة والمسئولية": request.form['citizenship_and_responsibility'],
            "الأنشطة اللاصفية / التكليفات": request.form['assignments']
        }
        
        # Create HTML content for PDF
        html_content = render_template('lesson_plan_template.html', lesson_data=lesson_data)
        pdf_file = "lesson_plan.pdf"
        pdfkit.from_string(html_content, pdf_file)
        
        return send_file(pdf_file, as_attachment=True)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
