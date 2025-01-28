class Bike:
    def __init__(self,name,cc):
        self.bikename = name
        self.bikecc = cc
    
    def myfun(self):
        print("Bike is "+self.bikename)
        print("It has ",str(self.bikecc)+" cc engine")

x=Bike("bullet",350)
y=Bike("KTM",390)

x.myfun()
y.myfun()