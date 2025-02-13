from flask import Flask, render_template, request, send_file, abort
import pdfkit
import os

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET', 'POST'])
def lesson_plan():
    try:
        if request.method == 'POST':
            required_fields = [
                'lesson_title', 'grade_level', 'session_schedule', 'motivation',
                'new_concepts', 'learning_process', 'learning_outcomes', 'lesson_steps',
                'assessment', 'duration', 'teaching_methods', 'activities_and_tools',
                'twenty_first_century_skills', 'cross_subject_links',
                'citizenship_and_responsibility', 'assignments'
            ]

            # التحقق من الحقول المطلوبة
            for field in required_fields:
                if field not in request.form or not request.form[field].strip():
                    return "خطأ: جميع الحقول مطلوبة!", 400

            lesson_data = {field: request.form[field] for field in required_fields}

            # التحقق من وجود قالب HTML قبل محاولة استخدامه
            template_path = os.path.join("templates", "lesson_plan_template.html")
            if not os.path.exists(template_path):
                return "خطأ: ملف القالب `lesson_plan_template.html` غير موجود!", 500

            html_content = render_template('lesson_plan_template.html', lesson_data=lesson_data)

            # التحقق من تثبيت `wkhtmltopdf`
            pdfkit_config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
            pdf_file = "lesson_plan.pdf"

            pdfkit.from_string(html_content, pdf_file, configuration=pdfkit_config)

            return send_file(pdf_file, as_attachment=True)

        return render_template('form.html')

    except Exception as e:
        return f"حدث خطأ داخلي: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
