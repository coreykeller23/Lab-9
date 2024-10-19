"""
Author: Corey Keller
Creation: 3/28/2024
File Name: lab8address.py
Purpose: Create the 'Address' class for Lab 8.
"""
#Address class creation
class Address:
    addressNumber=""
    streetName=""
    city=""
    state=""
    zipcode=""
    currentAddress=True
    optionalAptNumb=""

    #constructor
    def __init__(self, an="", sn="", c="", s="", zip="", ca="", op=""):
        self.addressNumber=an
        self.streetName=sn
        self.city=c
        self.state=s
        self.zipcode=zip
        self.currentAddress=ca
        self.optionalAptNumb=op
    
    #str return
    def __str__(self):
        return self.addressNumber + " " + self.streetName + self.optionalAptNumb + "\n" + self.city + "," + self.state + " " + self.zipcode + "\n" + "Current Address: " + str(self.currentAddress)
    
    #setters
    def setAddressNumber(self, an):
        self.addressNumber=an
    
    def setStreetName(self, sn):
        self.streetName=sn
    
    def setOptional(self, op):
        self.optionalAptNumb=op

    def setCity(self, c):
        self.city=c
    
    def setState(self, s):
        self.state=s

    def setZipcode(self, zip):
        self.zipcode=zip
    
    def setCurrentAddress(self, ca):
        self.currentAddress=ca
    
    #getters
    def getAddressNumber(self):
        return self.addressNumber
    
    def getStreetName(self):
        return self.streetName
    
    def getOptional(self):
        return self.optionalAptNumb
    
    def getCity(self):
        return self.city
    
    def getState(self):
        return self.state
    
    def getZipcode(self):
        return self.zipcode
    
    def getCurrentAddress(self):
        return self.currentAddress
    
    #other actions
    def inStateorOut(self):
        if self.state.upper() == "INDIANA" or self.state.upper() == "IN":
            return "The student is in state."
        else:
            return "The student is out of state."