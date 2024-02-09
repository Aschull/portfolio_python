from sqlalchemy import Column, Integer, String
from app.configs.db.sqlite import Base, Session

db = Session


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)
    classes = Column(String(255))

    class Config:
        orm_mode = True

    @staticmethod
    def get_students():
        return db.query(Student).all()
    
    @staticmethod
    def get_student_by_id(student_id: int):
        return db.query(Student).filter(Student.id == student_id).first()

    def crate_student(self):
        db.add(self)
        db.commit()
        db.close()

    def update_student(self, student_id: int, name: str, age: int, classes: str):
        student = db.query(Student).filter(Student.id == student_id).first()
        if student:
            student.name = name
            student.age = age
            student.classes = classes
            db.commit()


    def delete_student(self, student_id: int):
            student = db.query(Student).filter(Student.id == student_id).first()
            if student:
                db.delete(student)
                db.commit()
