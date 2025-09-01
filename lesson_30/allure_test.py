import allure
from students_system import Student, Course, session

@allure.feature("Student Management")
def test_create_student():
    with allure.step("Create a new student"):
        student = Student(name="Vitalii")  # age видалено
        session.add(student)
        session.commit()

    with allure.step("Verify student was added"):
        result = session.query(Student).filter_by(name="Vitalii").first()
        assert result is not None

@allure.feature("Course Enrollment")
def test_enroll_student():
    with allure.step("Create course and student"):
        course = Course(title="Python Automation")
        student = Student(name="TestUser")
        student.courses.append(course)
        session.add_all([student, course])
        session.commit()

    with allure.step("Verify enrollment"):
        enrolled = session.query(Student).filter(Student.name == "TestUser").first()
        assert any(c.title == "Python Automation" for c in enrolled.courses)