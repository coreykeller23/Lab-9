"""
Author: Corey Keller
Creation: 3/28/2024
File Name: lab8student.py
Purpose: Create the 'Student' class for Lab 8.
"""
from lab8addressClass import Address
from lab8emergencyContactClass import EmergencyContact

#Student class creation
class Student:
    firstName=""
    lastName=""
    IDnumb=""
    enrollmentStatus=""
    address=Address()
    gpa=0.0
    urgentContact=EmergencyContact()

    #constructor
    def __init__(self, fn="", ln="", ID="", es="", ad="", gpa="", uc=""):
        self.firstName=fn
        self.lastName=ln
        self.IDnumb=ID
        self.enrollmentStatus=es
        self.address=ad
        self.gpa=gpa
        self.urgentContact=uc
    
    #str return
    def __str__(self):
        return "Name: " + self.firstName + " " + self.lastName + "\n" + "Student ID: " + self.IDnumb + "\n" + "Enrollment Status: " + self.enrollmentStatus + "\n" + "GPA: " + str(self.gpa) + "\n" + "Address: " + str(self.address) + "\n" + "Emergency Contact: " + str(self.urgentContact)
    
    #setters
    def setFirstName(self, fn):
        self.firstName=fn

    def setLastName(self, ln):
        self.lastName=ln

    def setIDnumb(self, ID):
        self.IDnumb=ID

    def setEnrollmentStatus(self, es):
        self.enrollmentStatus=es

    def setAddress(self, ad):
        self.address=ad

    def setGPA(self, gpa):
        self.gpa=gpa

    def setUrgentContact(self, uc):
        self.urgentContact=uc

    #getters
    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getIDnumb(self):
        return self.IDnumb

    def getEnrollmentStatus(self):
        return self.enrollmentStatus

    def getGPA(self):
        return self.gpa
    
    #other actions
    def checkGPA(self):
        if self.gpa>4.0:
            return "Invalid GPA."
        else:
            return True