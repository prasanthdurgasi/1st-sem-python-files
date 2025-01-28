class a:
    def son1(self):
        print("abhinav is frist son")
    def son2(self):
        print("avinash is second ")
class b(a):
    def son3(self):
        print("babu is frist son")
    def son4(self):
        print("balaji is second ")
class c(b):
    def son5(self):
        print("charan is frist son")
    def son6(self):
        print("cherry is second ")
teja=c()
teja.son1()
teja.son2()
teja.son3()
teja.son4()
teja.son5()
teja.son6()

