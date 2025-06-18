class Student:
    def __init__(self, name, surname, age, aver_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.aver_grade = aver_grade

    def greet(self):
        return f"Hello, my name is {self.name} and my surname is {self.surname}. My age is {self.age} years old. My grade is {self.aver_grade}"

    def change_grade(self, new_grade):
        self.aver_grade = new_grade
        return f"My new average grade is {self.aver_grade}"

student = Student("John", "Smith", "19", 18)

print(f"My old aver_grade {student.aver_grade}")
print(student.change_grade(70))
print(student.greet())
