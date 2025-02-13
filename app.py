from flask import Flask, render_template, request, send_file, abort
import pdfkit
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def lesson_plan():
    if request.method == 'POST':
        required_fields = [
            'lesson_title', 'grade_level', 'session_schedule', 'motivation',
            'new_concepts', 'learning_process', 'learning_outcomes', 'lesson_steps',
            'assessment', 'duration', 'teaching_methods', 'activities_and_tools',
            'twenty_first_century_skills', 'cross_subject_links',
            'citizenship_and_responsibility', 'assignments'
        ]

        # التحقق من وجود جميع الحقول المطلوبة
        for field in required_fields:
            if field not in request.form or not request.form[field].strip():
                return "خطأ: يرجى ملء جميع الحقول المطلوبة.", 400

        lesson_data = {field: request.form[field] for field in required_fields}
        
        # إنشاء HTML للـ PDF
        html_content = render_template('lesson_plan_template.html', lesson_data=lesson_data)
        pdf_file = "lesson_plan.pdf"
        pdfkit.from_string(html_content, pdf_file)
        
        return send_file(pdf_file, as_attachment=True)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
