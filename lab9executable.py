"""
Author: Corey Keller
File Name: lab9executable.py
File Creation: 4/6/2024
Purpose: Demonstrate class creation from class files.
"""
from lab8addressClass import Address
from lab8emergencyContactClass import EmergencyContact
from lab8studentClass import Student
from lab9teacherClass import Teacher

#create objects
student1Address=Address("1234", "Main Street","Indianapolis", "IN", "46207", True)
student1EmergencyContact=EmergencyContact("Joe", "Smith", "Cell", "123-456-7890", "thisisanemail@yahoo.com", "Father", student1Address)
student1=Student("John", "Smith", "123456789", "Full Time", student1Address, 3.9, student1EmergencyContact)
#Change one parent property value
student1.setGPA(3.2)
#Invoke one parent method
print(student1.checkGPA())

teacher1Address=Address("5678", "Not Main Street", "Indianapolis", "IN", "46207", True)
teacher1EmergencyContact=EmergencyContact("Jane", "Doe", "Work", "098-765-4321", "isthisanemail@gmail.com", "Spouse", teacher1Address)
teacher1=Teacher("Man", "Name", "987654321", "", teacher1Address, 0.0, teacher1EmergencyContact)
teacher1.setIDnumb("9876543210")
teacher1.setFacultyEmail("myteacheremail@comcast.net")
teacher1.setSalary(100000000.0)
#Change one child property value
teacher1.setFirstName("Person")
#Invoke one child method
print(teacher1.salOverUnder())

#print out objects
print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(student1)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(teacher1)