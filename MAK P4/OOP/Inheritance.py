# Inheritance
# Allows the children to use any public variables from it's parent

class Makcs:
    def __init__(self,idp):
        self.stid = idp
    def setid(self,id):
        self.stid = id
    def getid(self):
        return self.stid
    
# to make a child class, use "class childName(parentName)"

class Student(Makcs):   # Child(Student) of Parent(Makcs)
    def __init__(self,name,id):
        Makcs.__init__(self,id)
        self.__stname = name
    def getname(self):
        return self.__stname
    
st1 = Student("Shaheer",2002)
print(st1.getid())  # getid() is not from Student, it's from Makcs, this is an inherited method and var