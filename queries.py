from model import Student
from ariadne import convert_kwargs_to_snake_case

students = [
    Student( 1, 'Aman', 21),
    Student( 2, 'Bayant', 13),
    Student( 3, 'Chandu', 19),
    Student( 4, 'Dhawal', 25)
]

def resolve_any_one( obj, info):
    return Student( 1, 'Mayank', 23)

@convert_kwargs_to_snake_case
def resolve_find_one_by_id( obj, info, student_id):
    for student in students:
        if student.id == student_id:
            return student
    return None

def resolve_create_using_primitives( obj, info, id, name, age):
    student = Student( id, name, age)
    students.append(student)
    return student  

def resolve_create_using_object( obj, info, student):
    students.append(student)
    return student
