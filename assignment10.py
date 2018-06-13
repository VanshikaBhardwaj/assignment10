#1
class Animal:
    def __init__(self,legs):
        self.legs=legs
    def animal_attribute(self):
        print(self.legs)
class Tiger(Animal):
    pass
t1=Tiger(4)
t1.animal_attribute()

#2
#=================================================================================
#               OUTPUT: A B
#=================================================================================
#3
class Cop:
    def __init__(self,name, age , workExp,designation):
        self.name=name
        self.age=age
        self.workExp
        self.designation=designation
    def disp(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Work Experience:",self.workExp)
        print("Designation:",self.designation)
    def update(self,name, age , workExp,designation):
        self.name=name
        self.age=age
        self.workExp
        self.designation=designation
        
class Mission(Cop):
    def __init__(self,name, age , workExp,designation,mission):
        super(Mission,self).__init__()
        self.mission=mission
    def dispMission(self):
        print("Mission:",self.mission)
        print("Mission_code:",self.code)
    def add_mission_details(self,code):
        self.code=code
cop1=Mission("Bond",25,10,"Investigator","Rescue Hostage")
cop1.add_mission_details(007)
cop1.dispMission()
cop1.disp()
#4
class shape:
    def __init__(self,Len,Bre):
        self.Len=Len
        self.Bre=Bre
    def area(self):
        return self.Len*self.Bre
class rect(shape):
    pass
class square(shape):
    pass
rect1=rect(12,45)
square1=square(5,5)
print("Area of square:",square1.area())
print("Area of Rectangle:",rect1.area())