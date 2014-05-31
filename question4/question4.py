'''
Created on May 30, 2014

This program fetches a set of student data from a web service as json, parses it into a set of Student objects, and sorts based on ascending grade order.

@author: MRHardwick
'''

import urllib2
import json

class Student(object):
    '''Useful for storing student data.
    '''
    def __init__(self, grade, first_name, last_name):
        
        # Decode back into string literal form when storing.
        
        self.grade = grade.decode('string-escape')
        self.first_name = first_name.decode('string-escape')
        self.last_name = last_name.decode('string-escape')
        
        # Establish a year number for this student based on their grade description.
        
        self.grade_number = 0
        if (grade.lower() == 'freshman'):
            self.grade_number = 1
        elif (grade.lower() == 'sophomore'):
            self.grade_number = 2
        elif grade.lower() == 'junior':
            self.grade_number = 3
        elif grade.lower() == 'senior':
            self.grade_number = 4



def student_json_decoder(json_obj):
    '''A decoder which places attributes from a json object dictionary into a new instance of Student.
    '''
    return Student(json_obj['grade'], json_obj['first_name'], json_obj['last_name'])



def student_comparator_ascending_grade(student_one, student_two):
    '''A comparator for use in the sorted() routine.
    Compares based upon the two students grade number.
    
    @return: 0 if the grade number is identical. 1 if the first student is in the higher grade. -1 if the first student is in the lower grade.     
    '''
    
    # Are the two students in the same grade?
    
    if student_one.grade_number is student_two.grade_number:
        return 0
    
    # Is the first student in a lower grade?
    
    elif student_one.grade_number < student_two.grade_number:
        return -1
    
    # Otherwise, the first student must be in the higher grade.
    
    else:
        return 1



if __name__ == '__main__':
    '''Fetches a listing of student data from a web service, parses the data into Student objects, and sorts by ascending grade order.
    '''
    
    # Get the json from the server.
    
    raw_json = urllib2.urlopen('http://dev.dryan.net.s3.amazonaws.com/students.json').read()
    
    # Change the encoding to unicode so the json parser understands the string.
    
    raw_json = raw_json.encode('unicode-escape')
    
    # Parse the raw json into a set of Student objects.
    
    students = json.loads(raw_json, object_hook=student_json_decoder)
    
    # Sort the Student objects by grade number.
    
    students = sorted(students, cmp=student_comparator_ascending_grade)
    
    # Print the grades and names to illustrate that they are sorted.
    
    for student in students:
        print student.grade_number, student.grade, student.first_name, student.last_name