"""class laptop():
    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage
        def hp(self):
            print("storage of laptop:",self.storage)
            print("ram of laptop:",self.ram)
money=laptop(128,6)
money.hp()"""
class Laptop:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def hp(self):
        print("storage of laptop:", self.storage)
        print("ram of laptop:", self.ram)

money = Laptop(6, 128)
money.hp()
