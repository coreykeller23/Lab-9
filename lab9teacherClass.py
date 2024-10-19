"""
Author: Corey Keller
File Name: lab9teacherClass.py
File Creation: 4/5/2024
Purpose: Create the 'Teacher' class for Lab 9.
"""
from lab8addressClass import Address
from lab8emergencyContactClass import EmergencyContact
from lab8studentClass import Student

class Teacher(Student):
    #overwrite ID number
    IDnumb=""
    #create new properties
    facultyEmail=""
    salary=0.0

    #str return
    def __str__(self):
        return "Name: " + self.firstName + " " + self.lastName + "\n" + "University ID: " + self.IDnumb + "\n" + "Salary: $" + str(self.salary) + "\n" + "Email: " + self.facultyEmail + "\n" + "Address: " + str(self.address) + "\n" + "Emergency Contact: " + str(self.urgentContact)
    
    #setters
    def setIDnumb(self, ID):
        self.IDnumb=ID
    def setFacultyEmail(self, fe):
        self.facultyEmail=fe
    def setSalary(self, s):
        self.salary=s
    def setGPA(self, gpa):
        pass
    def setEnrollmentStatus(self, es):
        pass
    
    #getters
    def getIDnumb(self, ID):
        return self.IDnumb
    def getFacultyEmail(self, fe):
        return self.facultyEmail
    def getSalary(self, s):
        return self.salary
    def getEnrollmentStatus(self):
        pass
    def getGPA(self):
        pass

    #additional actions
    def checkGPA(self):
        pass
    def salOverUnder(self):
        if self.salary>99999.0:
            return "Over"
        else:
            return "Under"
    
