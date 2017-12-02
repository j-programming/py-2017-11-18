#!/usr/bin/env python

STUDENT_TYPES= ('undergraduate', 'postgraduate')
EMPLOYMENT_TYPES=('permanent', 'temporary')

class Person(object):
    def __init__(self,name,surname,number):
        self.name=name
        self.surname=surname
        self.number=number


class Student(Person):
    def __init__(self, student_type, *args):
        super(Student,self).__init__(*args)
        if student_type not in STUDENT_TYPES:
            raise ValueError('student_type must be one of {}'.format(STUDENT_TYPES)) 
        self.student_type=student_type
        self.classes=[]

    def enrol(self,class_):
        self.classes.append(class_)

class StaffMember(Person):
    def __init__(self, status_ ,*args, **kwargs):
        super(StaffMember,self).__init__(*args)
        if status_ not in EMPLOYMENT_TYPES:
             raise ValueError('employment_type must be one of {}'.format(EMPLOYMENT_TYPES)) 
        self.employment_type=status_

class Lecturer(StaffMember):
    def __init__(self,*args):
        super(Lecturer,self).__init__(*args)
        self.courses_taught=[]

    def assign_teaching(self,course_):
        self.courses_taught.append(course_)


person = Person('Jane', 'Smith', '123456')
print person.name, person.surname, person.number

student = Student('postgraduate', 'Jane', 'Smith', 'SMTJNX045')
print student.name, student.surname, student.number, student.student_type, student.classes

student.enrol('Math 101')
print student.classes

staff_member = StaffMember('permanent', 'Jane', 'Smith', 'SMTJNX045')
print staff_member.name, staff_member.surname, staff_member.number, staff_member.employment_type

lecturer = Lecturer('permanent', 'Bob', 'Jones', '123456789')
print lecturer.name, lecturer.surname, lecturer.number, lecturer.employment_type, lecturer.courses_taught

lecturer.assign_teaching('History 101')
print lecturer.courses_taught

#student = Student('blah', 'Jane', 'Smith', 'SMTJNX045')

lecturer = Lecturer('blah', 'Bob', 'Jones', '123456789')