# create an Animal class
# syntax class name:

class Animal:

    #__init__ to declare class attributes
    def __init__(self): #self refers to current class
        self.alive = True
        self.spine = True


    def sleep(self):
        return "8 hours sleep is advised"


    def eat(self):
        return "eat if you like to stay alive... and eat healthy"


# create an object of the class before using it


cat = Animal()

# print(cat.sleep()) # abstracted what was created or what info available