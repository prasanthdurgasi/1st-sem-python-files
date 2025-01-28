class Employee:
    def __init__(self,name,age,role,salary):
        self.empname = name
        self.empage = age
        self.emprole = role
        self.empsalary = salary
    
    def myfun(self):
        print("Employee name is : "+ self.empname)
        print("The person age is : "+ str(self.empage))
        print("The role of perosn is : "+ self.emprole)
        print("The salary of person is : "+str(self.empsalary))

x=Employee("Indhu",21,"Solution Architect",710000)
y=Employee("Sitara",22,"Trainee",850000)
z=Employee("Vivek",21,"Prompt Engineer",950000)

x.myfun()
y.myfun()
z.myfun()