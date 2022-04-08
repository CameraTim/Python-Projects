from abc import ABC, abstractmethod

#Creating the parent class the houses the primary function of displaying the camera data
class Camera(ABC):
    def colorSpace(self, color, model):
        print("The {} records in".format(model),color)

    #Sets the function to ask for an argument without specifying data type
    @abstractmethod
    def camModel(self, model):
        pass

#Creating the child class that can override the information in the parent class
class Fujifilm(Camera):
    def camModel(self, color, model):
        print("When you shoot in F-log, the",model,"shoots in",color)
        
cam = Fujifilm()
cam.colorSpace("Rec.2020","X-T3")
cam.camModel("Rec.2020","X-T3")

if __name__ == "__main__":
    pass
