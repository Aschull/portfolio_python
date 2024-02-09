from app.models.student import Student
from app.DTO.student_DTO import StudentDTO

class StudentService:

    def get_students(self):
        return Student().get_students()
    
    def get_student_by_id(self, student_id: int):
        return Student.get_student_by_id(student_id=student_id)

    def create_student(self, student_dto: StudentDTO):
        student = Student(
            name=student_dto.name, 
            age=student_dto.age, 
            classes=student_dto.classes
        )
        student.crate_student()
        return student
    
    def update_student(self, student_id: int, student_dto: StudentDTO):
        student = Student.get_student_by_id(student_id=student_id)
        if student:
            student.update_student(student_id=student_id, name=student_dto.name, age=student_dto.age, classes=student_dto.classes)

    def delete_student(self, student_id: int):
        student = Student.get_student_by_id(student_id=student_id)
        if student:
            student.delete_student(student_id=student_id)


