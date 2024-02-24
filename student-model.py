from home.models import Standard
from home.models import Student
students_data = [
    {'name': 'John Doe', 'rollno': 21, 'standard': '10th', 'course': 'Science'},
    {'name': 'Jane Smith', 'rollno': 22, 'standard': '11th', 'course': 'Mathematics'},
    {'name': 'David Johnson', 'rollno': 23,
        'standard': '12th', 'course': 'History'},
    {'name': 'Emily Brown', 'rollno': 24, 'standard': '10th', 'course': 'Science'},
    {'name': 'Michael Wilson', 'rollno': 25,
        'standard': '11th', 'course': 'Mathematics'},
    {'name': 'Sophia Martinez', 'rollno': 26,
        'standard': '12th', 'course': 'History'},
    {'name': 'William Taylor', 'rollno': 27,
        'standard': '10th', 'course': 'Science'},
    {'name': 'Olivia Garcia', 'rollno': 28,
        'standard': '11th', 'course': 'Mathematics'},
    {'name': 'Daniel Martinez', 'rollno': 29,
        'standard': '12th', 'course': 'History'},
    {'name': 'Isabella Rodriguez', 'rollno': 30,
        'standard': '10th', 'course': 'Science'},
]

for student_data in students_data:
    student = Student(name=student_data['name'],
                      rollno=student_data['rollno'],
                      standard=student_data['standard'],
                      course=student_data['course'])
    student.save()


standard_names = ['A', 'B', 'C']

for name in standard_names:
    standard = Standard(standard_name=name)
    standard.save()

lst = [
    {'name': 'Aakarshak'},
    {'name': 'Vinit'},
    {'name': 'Yash'},
    {'name': 'Fidyan'},
    {'name': 'Fenil'},
    {'name': 'Dwij'},
    {'name': 'Gopi'},
    {'name': 'Dev'},
    {'name': 'Dhruv'},
    {'name': 'Aman'},
]

lst = [
    {'standard_name': "A"},
    {'standard_name': "B"},
    {'standard_name': "B"},
    {'standard_name': "C"},
    {'standard_name': "A"},
    {'standard_name': "B"},
    {'standard_name': "A"},
    {'standard_name': "C"},
    {'standard_name': "A"},
    {'standard_name': "C"},
]
