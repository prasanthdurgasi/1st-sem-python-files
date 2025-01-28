class hair:
    def gender(self):
        pass

class boy(hair):
     def gender(self):
         return "short hair"
    
class girl(hair):
     def gender(self):
         return "long hair"
         
def hairs(hair):
    print(hair.gender())    
b = boy()
g = girl()
hairs(b)
hairs(g)

