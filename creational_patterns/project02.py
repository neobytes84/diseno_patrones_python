# Creational patterns - Factory Method in Python - Example 01
# Developed by Neobytes.io

import random
import calendar

class CollegeLongCourseFactory:
    
    def __init__(self):
        self.courses = {"Mathematics": "Mathematics", "Physics": "Physics", "Chemistry": "Chemistry", "Biology": "Biology", "English": "English", "Computer Science": "Computer Science"}
    
    def create_course(self, inscribed_students):
        course_name = random.choice(list(self.courses.keys()))
        course_duration = random.randint(6, 12)
        course_instructor = random.choice(list(self.courses.values()))
        course_schedule = self.generate_schedule(course_duration)
        
        return {
            "course_name": course_name,
            "course_duration": course_duration,
            "course_instructor": course_instructor,
            "course_schedule": course_schedule,
            "inscribed_students": inscribed_students
        }
    
    def generate_schedule(self, course_duration):
        weekdays = [day for day in calendar.day_name if day != "Saturday" and day != "Sunday"]
        schedule = []
        
        for day in weekdays:
            start_time = random.randint(8, 18)
            end_time = start_time + course_duration
            
            schedule.append(f"{day}: {start_time}-{end_time}")
        
        return schedule
    
    def generate_student_list(self, total_students):
        return [f"Student {i+1}" for i in range(total_students)]
    
    def price_course(self, course_duration):
        return 500 * course_duration
    
    def get_inscribed_students(self, course_duration):
        return random.randint(10, 50) * course_duration
    
    def get_courses(self):
        return self.courses
    
    def get_course_details(self, course_name):  
        return self.courses.get(course_name, "Course not found")
    
    def generate_report(self, courses):
        report = "Course Report:\n"
        
        for course in courses:
            report += f"Course Name: {course['course_name']}\n"
            report += f"Course Duration: {course['course_duration']} weeks\n"
            report += f"Course Instructor: {course['course_instructor']}\n"
            report += f"Course Schedule: {', '.join(course['course_schedule'])}\n"
            report += f"Inscribed Students: {course['inscribed_students']}\n"
            report += f"Price: ${self.price_course(course['course_duration'])}\n\n"
        
        return report

# Example usage:

factory = CollegeLongCourseFactory()

total_students = 100
total_courses = 5

student_list = factory.generate_student_list(total_students)

courses = []

for _ in range(total_courses):
    course = factory.create_course(student_list)
    courses.append(course)
    student_list = [student for student in student_list if student not in course["inscribed_students"]]
    total_students -= len(course["inscribed_students"])
    print(f"Course created: {course['course_name']}")
    print(f"Inscribed Students: {', '.join(course['inscribed_students'])}")
    print()
    print(f"Course Schedule: {', '.join(course['course_schedule'])}")
    print()
    print(f"Price: ${factory.price_course(course['course_duration'])}")
    print()
    print(f"Inscribed Students: {course['inscribed_students']}")
    print()
    print("---")
    
