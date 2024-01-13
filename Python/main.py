class John():
    def __init__(self,name,add):
        self.name = name
        self.add = add
p1 = John("John Kathariya Tharu","Tilottama-15, Kotihawa")
p1.name = "John Tharu"
print(p1.name)
p1.add = "Kotihawa"
print(p1.add)

class parson():
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname = lname
    def prinname(self):
        print(self.fname+ " and "+self.lname)
p1 = parson("John Kathariya","Tharu")
p1.prinname()

class Student(parson):
    pass

p2 = Student("Hero Prasad","Tharu")
p2.prinname()


class Joey():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
class Bishal(Joey):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        print(fname+" and "+lname)

p1 = Bishal("Joey","Tharu")