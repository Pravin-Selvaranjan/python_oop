# Inherit everything from Animal into reptile

from animal import Animal

# create a reptile class

class Reptile(Animal): # write the name of the class in (parent - class) to inherit # parent class - base class

    def __init__(self):
        # to let it know to inherit everything from parent class
        super().__init__() # super is used to inherit everything from base class
        self.cold_blooded = True
        self.heart_chambers = [3, 4]



    def seek_heat(self):
        return "looking for the sun shine "

    def hunt(self):
        return "working hard to catch a next meal"


# create an object of reptile class

reptile_object = Reptile()

# print(reptile_object.eat())
# print(reptile_object.hunt())