#!/usr/bin/env python
"""Python module for Schools/Teachers/Students 
"""

from collections import defaultdict

class classroom:
    """Teacher Information 
    """
    def __init__(self, name="Classroom"):
        self.name = name
        self.teacher = defaultdict(int)
        self.student = defaultdict(int)

        
    def add_teacher(self, teacher_name):
        """Registers Teachers to the School
        """
        if isinstance(teacher_name, str):
            self.teacher[teacher_name] += 1
        else:
            print("Invalid Teacher Name.")
    
    def add_student(self, student_name):
        """Registers Teachers to the School
        """
        if student_name not in self.student:
            self.student[student_name] +=1
        else:
            print("Invalid Student Name.")
            
    def generate_student_list(self):
        """Create a class list and Student Number
        """
        for student, count in self.student.items():
            print(f'{student}: {count}')
    
    def generate_teacher_list(self):
        """Create a class list and Student Number
        """
        for teacher in self.teacher.items():
            for count in self.student.items():
                print(f'{teacher}: {count}')