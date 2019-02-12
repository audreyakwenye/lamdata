#!/usr/bin/env python
"""Python module for Schools/Teachers/Students 
"""

from collections import defaultdict

class teacher:
    """Teacher Information 
    """
    def __init__(self, name="Class Teacher"):
        self.name = name
        self.student = defaultdict(int)

        
    def add_student(self, student_name):
        """Registers Teachers to the School
        """
        if student_name not in self.student:
            self.student[student_name] +=1
        else:
            print("Invalid Student Name.")
            
    def generate_class_list(self):
        """Create a class list and Student Number
        """
        for student, count in self.student.items():
            print(f'{student}: {count}')
        