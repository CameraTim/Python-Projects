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
        
#Adding child class
class Mac(Computer):
    comType = "Laptop"
    touchbar = False
    ports = 4

    #defining child class function
    def Components(parts):
        CPU = "M1"
        OS = "Monterey"
        print("Your computer is a {}, with a {}, {}, and {}.".format(parts.comType,parts.RAM,CPU,OS))

#Invokes methods for the parent and child classes
PC = Computer()
PC.Components()
Apple = Mac()
Apple.Components()
