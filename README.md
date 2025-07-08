# 🎓 Student Admission Validation System

This is a Flask-based web application designed to validate student admission form details against official records stored in a CSV file. If all details match, a pre-filled admission confirmation letter is generated in DOCX format.

## 🚀 Features

- 📝 HTML form for student data entry  
- ✅ Validates input against official `students.csv`  
- 📄 Generates personalized DOCX confirmation letter on successful match  
- ❌ Returns validation errors for incorrect/mismatched fields  
- 🌐 Built with Flask (Python backend) and HTML/CSS (frontend)

## 🖥️ Frontend

- Simple HTML form with fields such as:
  - Name, DOB, Email, Phone
  - Gender, Student ID, Entry Year
  - Course, Semester, Marks
- Minimal styling and validation using HTML5

## 🧠 Backend

- Built using **Flask**
- Uses `csv` module to validate form data
- Uses `python-docx` to generate confirmation letter
- Email acts as a unique identifier
- Full validation on fields like:
  - Name, DOB, Gender, Phone, ID, Course, Marks, etc.

## 📂 Directory Structure
Student-validation/
├── app.py
├── validate.py
├── generate_docx.py
├── data/
│ └── students.csv
├── templates/
│ └── form.html
├── output/
│ └── [generated letters]
├── venv/
└── README.md


## 🛠️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/panchami283/student-validation.git
cd student-validation

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
hen go to http://127.0.0.1:5000/ in your browser to use the system.

📦 Requirements
Python 3.8+

Flask

python-docx

lxml

opencv-python

numpy

pillow

(See requirements.txt)

✍️ Author
Panchami M
GitHub Profile

📌 Note
Make sure your students.csv in /data folder is correctly structured for validation.

css
Copy
Edit
email,first_name,middle_name,last_name,phone,dob,gender,student_id,entry_year,course,semester,marks


