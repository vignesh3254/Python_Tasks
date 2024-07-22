#7.
"""
Write a  Python class named Student with two attributes student_name,
marks. Modify the attribute values of the said class and
print the original and modified values of the said attributes.
"""

class Student:
    def __init__(self):
        self.student_name="Anbu"
        self.student_mark=90
    def display(self):
        print("Student Name:",self.student_name)
        print("Student Mark:",self.student_mark)

obj=Student()

obj.display()

obj.student_name="Maari"
obj.student_mark=80

obj.display()
