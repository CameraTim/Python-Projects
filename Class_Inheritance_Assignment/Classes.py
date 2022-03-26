#Creating the parent class
class Computer:
    #Setting the object properties of the parent class
    def __init__(self,CPU,GPU,RAM):
        self.CPU = CPU
        self.GPU = GPU
        self.RAM = RAM
    #Printing the computer parts of the parent class when it's called
    def showCom(parts):
        print(parts.CPU,"\n",parts.GPU,"\n",parts.RAM,"\n")

#Adding first child class by inheriting the Computer class
class Mac(Computer):
    MacOS = 'Monterey'
    M1 = True

#Adding second child class
class PC(Computer):
    WinOS = 'Windows 11'
    customBuild = False



x = PC('Ryzen 7 3700X','RTX 2060','32GB 3600Mhz')
x.showCom()
