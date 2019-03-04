students = []
def add_student(name, student_id=0):
    student = {"name": name, "student_id": student_id}
    students.append(student)

add_student(name="Mark", student_id=2)
add_student("John", 3)
add_student("Jane")

print(list(students))
