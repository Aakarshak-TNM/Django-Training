from home.models import Standard
from home.models import Student
students_data = [
    {'name': 'John Doe', 'rollno': 21, 'standard': '10th',
        'course': 'Science', 'standard_name': 1},
    {'name': 'Jane Smith', 'rollno': 22, 'standard': '11th',
        'course': 'Mathematics', 'standard_name': 2},
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


students_data = [
    {"name": "John Doe", "rollno": 1, "standard": "12th",
        "course": "Science", "standard_name": "A"},
    {"name": "Alice Smith", "rollno": 2, "standard": "12th",
        "course": "Science", "standard_name": "B"},
    {"name": "Michael Johnson", "rollno": 3, "standard": "12th",
        "course": "Science", "standard_name": "C"},
    {"name": "Emily Brown", "rollno": 4, "standard": "12th",
        "course": "Science", "standard_name": "A"},
    {"name": "Daniel Wilson", "rollno": 5, "standard": "12th",
        "course": "Science", "standard_name": "B"},
    {"name": "Emma Davis", "rollno": 6, "standard": "12th",
        "course": "Science", "standard_name": "C"},
    {"name": "David Martinez", "rollno": 7, "standard": "12th",
        "course": "Science", "standard_name": "A"},
    {"name": "Olivia Jones", "rollno": 8, "standard": "12th",
        "course": "Science", "standard_name": "B"},
    {"name": "James Wilson", "rollno": 9, "standard": "12th",
        "course": "Science", "standard_name": "C"},
    {"name": "Sophia Taylor", "rollno": 10, "standard": "12th",
        "course": "Science", "standard_name": "A"},
    {"name": "Ava Lewis", "rollno": 11, "standard": "12th",
        "course": "Science", "standard_name": "B"},
    {"name": "Mia Walker", "rollno": 12, "standard": "12th",
        "course": "Science", "standard_name": "C"},
    {"name": "Benjamin King", "rollno": 13, "standard": "12th",
        "course": "Science", "standard_name": "A"},
    {"name": "Madison Wright", "rollno": 14, "standard": "12th",
        "course": "Science", "standard_name": "B"},
    {"name": "Alexander Johnson", "rollno": 15, "standard": "12th",
        "course": "Science", "standard_name": "C"},
    {"name": "Sophia Johnson", "rollno": 16, "standard": "12th",
        "course": "Science", "standard_name": "A"},
    {"name": "Daniel White", "rollno": 17, "standard": "12th",
        "course": "Science", "standard_name": "B"},
    {"name": "James Davis", "rollno": 18, "standard": "12th",
        "course": "Science", "standard_name": "C"},
    {"name": "Ava Thompson", "rollno": 19, "standard": "12th",
        "course": "Science", "standard_name": "A"},
    {"name": "Ethan Wilson", "rollno": 20, "standard": "12th",
        "course": "Science", "standard_name": "B"},
]

# Retrieve an existing Standard instance by standard_name
for i in students_data:
    standard_instance, created = Standard.objects.get_or_create(
        standard_name=i['standard_name'])
    # Create a new student instance and assign the standard
    student = Student.objects.create(
        name=i['name'],
        rollno=i['rollno'],
        standard=i['standard'],
        course=i['course'],
        standard_name=standard_instance
    )
    student.save()
    