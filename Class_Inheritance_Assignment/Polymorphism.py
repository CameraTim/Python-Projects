#Creating the parent class
class Computer:
    comType = "Desktop"
    touchScreen = True
    monitors = 3
    RAM = "32GB"
    
    def Components(parts):
        CPU = "3700X"
        winVer = 10
        print("Your computer is a {}, with a {}, {}, and {}.".format(parts.comType,parts.RAM,CPU,winVer))
        
#Adding 
class Mac(Computer):
    comType = "Laptop"
    touchbar = False
    ports = 4

    def Components(parts):
        CPU = "M1"
        OS = "Monterey"
        print("Your computer is a {}, with a {}, {}, and {}.".format(parts.comType,parts.RAM,CPU,OS))

PC = Computer()
PC.Components()
Apple = Mac()
Apple.Components()
