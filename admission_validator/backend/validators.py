import csv

def validate_input(data):
    errors = []
    match_found = False

    form_dob = f"{data['birth_year']}-{int(data['birth_month']):02d}-{int(data['birth_day']):02d}"
    print(form_dob)
    with open('data/students.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Check email as a primary key
            if data['email'].strip().lower() == row['email'].strip().lower():
                match_found = True

                if data['first_name'].strip().lower() != row['first_name'].strip().lower():
                    errors.append("First Name does not match")
                    print("First Name does not match")
                if data['middle_name'].strip().lower() != row['middle_name'].strip().lower():
                    errors.append("Middle Name does not match")
                    print("Middle Name does not match")
                if data['last_name'].strip().lower() != row['last_name'].strip().lower():
                    errors.append("Last Name does not match")
                    print("Last Name does not match")
                if data['phone'].strip() != row['phone'].strip():
                    errors.append("Phone number does not match")
                    print("Phone number does not match")
                if form_dob != row['dob'].strip():
                    errors.append("Date of Birth does not match")
                    print("Date of Birth does not match")
                if data['gender'].strip().lower() != row['gender'].strip().lower():
                    errors.append("Gender does not match")
                    print("Gender does not match")
                if data['student_id'].strip().upper() != row['student_id'].strip().upper():
                    errors.append("Student ID does not match")
                    print("Student ID does not match")
                if data['entry_year'].strip() != row['entry_year'].strip():
                    errors.append("Entry Year does not match")
                    print("Entry Year does not match")
                if data['course'].strip().lower() != row['course'].strip().lower():
                    errors.append("Course does not match")
                    print("Course does not match")
                if data['semester'].strip().upper() != row['semester'].strip().upper():
                    errors.append("Semester does not match")
                    print("Semester does not match")
                if data['marks'].strip() != row['marks'].strip():
                    errors.append("Marks do not match")
                    print("Marks do not match")

                break

    if not match_found:
        errors.append("Email not found in official records")

    return errors
