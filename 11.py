class hair:
    def gender(self):
        pass
class boy(hair):
     def gender(self):
         print("short hair")
    
class girl(hair):
     def gender(self):
         print("long hair")
         
def hairs(hair):
    print(hair.gender())
    
Boy=boy()
Girl=girl()
hairs(boy)
hairs(girl)