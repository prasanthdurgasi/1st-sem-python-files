class A:
    def name1(self):
        print("abhi is first")
        
    def name2(self):
        print("avi is second")
        
class B(A):
    def name3(self):
        print("balu is third")
      
    def name4(self):
        print("babu is forth")
class c(B):
    def name5(self):
         print("charan is frist")
    def name6(self):
         print("cherry is frist")
son = A()
son.name1()
son.name2()
child = B()
child.name3()

child.name4()
teja=c()
teja.name2()
