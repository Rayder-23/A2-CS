# self is a placeholder for the object name
# self is used mostly to call the variables
class Student:  # type for objects
    def __init__(self,namep,agep,idp): # constructor, inits the object
        self.__Stname = namep   # "self.__var" makes it private
        self.Stage = agep
        self.Stid = idp

    def setname(self,name): # method for renaming
        self.__Stname = name

    def getname(self):  # method for getting the name
        return self.__Stname

abc = Student("Basil",12,123)
# print(abc.__Stname)  # would only work if all the variables are public, they should be private

print(abc.getname())   # Basil
abc.setname("Haris")
print(abc.getname())   # Haris