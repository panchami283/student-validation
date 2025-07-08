from flask import Flask, render_template, request
from admission_validator.backend.validators import validate_input
from admission_validator.backend.generator import generate_docx

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "first_name": request.form.get('first_name', '').strip(),
        "middle_name": request.form.get('middle_name', '').strip(),
        "last_name": request.form.get('last_name', '').strip(),
        "email": request.form.get('email', '').strip(),
        "phone": request.form.get('phone', '').strip(),
        "birth_day": request.form.get('birth_day', '').strip(),
        "birth_month": request.form.get('birth_month', '').strip(),
        "birth_year": request.form.get('birth_year', '').strip(),
        "gender": request.form.get('gender', '').strip(),
        "student_id": request.form.get('student_id', '').strip(),
        "entry_year": request.form.get('entry_year', '').strip(),
        "course": request.form.get('course', '').strip(),
        "semester": request.form.get('semester', '').strip(),
        "marks": request.form.get('marks', '').strip()
    }

    errors = validate_input(data)
    if errors:
        return f"Validation failed: {', '.join(errors)}"
    
    generate_docx(data)
    full_name = f"{data['first_name']} {data['middle_name']} {data['last_name']}".strip()
    return f"Admission form for {full_name} generated successfully!"

if __name__ == '__main__':
    app.run(debug=True)
