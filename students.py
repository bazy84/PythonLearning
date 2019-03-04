students = []
def add_student(name, student_id=0):
    student = {"name": name, "student_id": student_id}
    students.append(student)

add_student(name="Mark", student_id=2)
add_student("John", 3)
add_student("Jane")

print(list(students))


def var_args(name, *args):
    print(name)
    print(args)


def kwargs(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])

var_args("Mark", "Loves python", None, True, "Hello")
