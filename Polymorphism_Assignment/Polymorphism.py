#Creating the parent class
class Computer:
    comType = "Desktop"
    touchScreen = True
    monitors = 3
    RAM = "32GB"
    #defining parent class function
    def Components(parts):
        CPU = "3700X"
        winVer = 10
        print("Your computer is a {}, with a {}, {}, and {}.".format(parts.comType,parts.RAM,CPU,winVer))
        
#Adding first child class
class Mac(Computer):
    comType = "Laptop"
    touchbar = False
    ports = 4
    #defining first child class function
    def Components(parts):
        CPU = "M1"
        OS = "Monterey"
        print("Your computer is a {}, with a {}, {}, and {}.".format(parts.comType,parts.RAM,CPU,OS))

#Adding second child class
class PC(Computer):
    touchScreen = False
    ports = 8
    RAM = "16GB"
    #defining second child class function
    def Components(parts):
        CPU = "5950X"
        winVer = 11
        print("Your computer is a {}, with a {}, {}, and {}.".format(parts.comType,parts.RAM,CPU,winVer))

#Invokes methods for the parent and child classes
firstBuild = Computer()
firstBuild.Components()
Apple = Mac()
Apple.Components()
Windows = PC()
Windows.Components()
