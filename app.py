import pdfkit
import os
from flask import Flask, render_template, request, send_file

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET', 'POST'])
def lesson_plan():
    if request.method == 'POST':
        lesson_data = {
            "عنوان الدرس": request.form.get('lesson_title', 'اضف عنوان الدرس هنا'),
            "الفصل": request.form.get('grade_level', 'اضف الفصل هنا'),
            "الحصة حسب الجدول": request.form.get('session_schedule', 'اضف الحصة هنا'),
            "التهيئة الحافزة": request.form.get('motivation', 'اضف التهيئة الحافزة هنا'),
            "المفاهيم الجديدة": request.form.get('new_concepts', 'اضف المفاهيم الجديدة هنا'),
            "عملية التعليم والتعلم": request.form.get('learning_process', 'اضف عملية التعليم والتعلم هنا'),
            "نواتج التعلم": request.form.get('learning_outcomes', 'اضف نواتج التعلم هنا'),
            "خطوات الدرس": request.form.get('lesson_steps', 'اضف خطوات الدرس هنا'),
            "التقييم": request.form.get('assessment', 'اضف التقييم هنا'),
            "الزمن": request.form.get('duration', 'اضف الزمن هنا'),
            "طرائق التدريس": request.form.get('teaching_methods', 'اضف طرائق التدريس هنا'),
            "الأنشطة والوسائل المستخدمة": request.form.get('activities_and_tools', 'اضف الأنشطة والوسائل المستخدمة هنا'),
            "مهارات القرن الواحد والعشرين": request.form.get('twenty_first_century_skills', 'اضف مهارات القرن الواحد والعشرين هنا'),
            "الربط مع المواد الأخرى": request.form.get('cross_subject_links', 'اضف الربط مع المواد الأخرى هنا'),
            "المواطنة والمسئولية": request.form.get('citizenship_and_responsibility', 'اضف المواطنة والمسئولية هنا'),
            "الأنشطة اللاصفية / التكليفات": request.form.get('assignments', 'اضف الأنشطة اللاصفية / التكليفات هنا')
        }
        
        # توليد HTML من القالب
        html_content = render_template('lesson_plan_template.html', lesson_data=lesson_data)
        pdf_file = "lesson_plan.pdf"

        # ضبط مسار `wkhtmltopdf`
        pdfkit_config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
        
        # توليد الـ PDF باستخدام `pdfkit`
        pdfkit.from_string(html_content, pdf_file, configuration=pdfkit_config)

        return send_file(pdf_file, as_attachment=True)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
