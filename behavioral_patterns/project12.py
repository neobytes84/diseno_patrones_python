# Behavioral patterns - Visitor in Python -example 01
# Developed by Neobytes.io

import pandas as pd
import random

class Courses_Programming:
    
    def __str__(self):
        return "Programming Courses"
    
    def __repr__(self):
        return(f"Courses_Programming({self.__str__()})")
    def new_course(self, id_course, price):
        print(self,"has id", id_course, "with price", price)

    def manager_course(self, manager):
        print(self," is a manager", manager)
    
    def student_course(self, student):
        print(self,"is a student", student)
    
    def qualification_course(self, qualification):
        print(self,"has qualification", qualification)

"""Concrete courses for Courses_Programming"""

class Python_Course(Courses_Programming):pass

class Java_Course(Courses_Programming):pass

class C_Course(Courses_Programming):pass

class Typescript_Course(Courses_Programming):pass

class Visitor:
    
    def __str__(self):
        return self.__class__.__name__

"""Concrete visitors for Visitor"""

class Student_Visitor(Visitor):
    def visit(self, classes):
        classes.new_course(self)
    
    def visit(self, classes):
        classes.manager_course(self)
    
    def visit(self, classes):
        classes.student_course(self)
    
    def visit(self, classes):
        classes.qualification_course()

class Manager_Visitor(Visitor):
    def visit(self, classes):
        classes.new_course(self)
    
    def visit(self, classes):
        classes.manager_course(self)
    
    def visit(self, classes):
        classes.student_course()
    
    def visit(self, classes):
        classes.qualification_course(self)

pyt = Python_Course()
jav = Java_Course()
c_lan = C_Course()
types = Typescript_Course()

"""Creating visitors"""

student_v = Student_Visitor()
manager_v = Manager_Visitor()

"""Creating courses"""

pyt.manager_course(manager_v)
jav.manager_course(manager_v)
c_lan.manager_course(manager_v)
types.manager_course(manager_v)

jav.student_course(student_v)
types.student_course(student_v)
c_lan.student_course(student_v)
pyt.student_course(student_v)

pyt.qualification_course(manager_v)

jav.qualification_course(student_v)

c_lan.qualification_course(manager_v)

types.qualification_course(student_v)

"""New courses"""
pyt.new_course("12",2550)

jav.new_course("13",3500)

c_lan.new_course("14",1500)

types.new_course("15",2000)
