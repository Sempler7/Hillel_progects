from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

# Налаштування ORM
Base = declarative_base()
engine = create_engine('sqlite:///students.db')
Session = sessionmaker(bind=engine)
session = Session()

# Модель даних
# Багато-до-багатьох: студенти ↔ курси
student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship('Course', secondary=student_course, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship('Student', secondary=student_course, back_populates='courses')

# Створення таблиць
Base.metadata.create_all(engine)

# Генерація тестових даних
def seed_data():
    # Створення курсів
    course_titles = ['Math', 'Physics', 'History', 'Biology', 'Programming']
    courses = [Course(title=title) for title in course_titles]
    session.add_all(courses)
    session.commit()

    # Створення студентів з рандомними курсами
    for i in range(1, 21):
        student = Student(name=f'Student {i}')
        student.courses = random.sample(courses, k=random.randint(1, 3))
        session.add(student)
    session.commit()

# Додавання студента
def add_student(name, course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if not course:
        print("❌ Курс не знайдено.")
        return
    new_student = Student(name=name)
    new_student.courses.append(course)
    session.add(new_student)
    session.commit()
    print(f"✅ Студента '{name}' додано до курсу '{course_title}'.")

# Запити
def students_in_course(course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if course:
        return [student.name for student in course.students]
    return []

def courses_of_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        return [course.title for course in student.courses]
    return []

# Оновлення та видалення
def update_student_name(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if student:
        student.name = new_name
        session.commit()
        print(f"🔄 Ім’я оновлено: {old_name} → {new_name}")
    else:
        print("❌ Студента не знайдено.")

def delete_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"🗑️ Студента '{name}' видалено.")
    else:
        print("❌ Студента не знайдено.")

# Приклади викликів
if __name__ == "__main__":
    # Запустити один раз для генерації даних
    seed_data()

    add_student("Vitalii", "Programming")

    print("📘 Курси студента 'Vitalii':", courses_of_student("Vitalii"))
    print("👨‍🎓 Студенти на курсі 'Math':", students_in_course("Math"))

    update_student_name("Vitalii", "Vitalii Pro")
    delete_student("Student 3")