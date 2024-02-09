from fastapi import APIRouter
from app.DTO.student_DTO import StudentDTO
from app.services.student import StudentService

router = APIRouter()
student_service = StudentService()


@router.get("/students")
def get_students():
    return student_service.get_students()

@router.post("/students")
def create_student(student: StudentDTO):
    return student_service.create_student(student)

@router.get("/student/{id}")
def get_student(id: int):
    return student_service.get_student_by_id(id)

@router.put("/student/{id}")
def update_student(id: int, new_students: StudentDTO):
    return student_service.update_student(id, new_students)

@router.delete("/student/{id}")
def delete_student(id: int):
    return student_service.delete_student(id)
