"""
Author: Corey Keller
Creation: 3/28/2024
File Name: lab8emergencyContact.py
Purpose: Create the 'Emergency Contact' class for Lab 8.
"""
from lab8addressClass import Address

#Contact class creation
class EmergencyContact:
    firstName=""
    lastName=""
    numberType=""
    phoneNumber=""
    email=""
    relationship=""
    address=Address()

    #constructor
    def __init__(self, fn="", ln="", nt="", pn="", e="", r="", ad=""):
        self.firstName=fn
        self.lastName=ln
        self.numberType=nt
        self.phoneNumber=pn
        self.email=e
        self.relationship=r
        self.address=ad
    
    #str return
    def __str__(self):
        return "Name: " + self.firstName + " " + self.lastName + "\n" + "Phone Number: " + self.numberType + "(" + self.phoneNumber + ")" + "\n" + "Email: " + self.email + "\n" + "Relationship: " + self.relationship
    
    #setters
    def setFirstName(self, fn):
        self.firstName=fn
    
    def setLastName(self, ln):
        self.lastName=ln

    def setNumberType(self, nt):
        self.numberType=nt
    
    def setPhoneNumber(self, pn):
        self.phoneNumber=pn

    def setEmail(self, e):
        self.email=e

    def setRelationship(self, r):
        self.relationship=r
    
    def setAddress(self, ad):
        self.address=ad
    
    #getters
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getNumberType(self):
        return self.numberType
    
    def getPhoneNumber(self):
        return self.phoneNumber
    
    def getEmail(self):
        return self.email
    
    def getRelationship(self):
        return self.relationship
    
    #other actions
    def getName(self):
        return self.firstName + " " + self.lastName