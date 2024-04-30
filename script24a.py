from abc import ABC , abstractmethod
class WorldBank(ABC):
    @abstractmethod
    def loan(self,x):
        pass
    @abstractmethod
    def save(self,x):
        pass

# # a = WorldBank()
# class SBI(WorldBank):

#     def loan(self,x):
#         print("loan is "+ str(x))
    
#     def save(self,x):
#         print("save is "+ str(x))

#     def branchName(self):
#         print("nagpur")

# class PNB(WorldBank):
#     def loan(self,x):
#         print("loan is" + str(x))

#     def save(self,x):
#         print("save is "+ str(x))

#     def branchName(self):
#         print("nagpur")

# nagpur = SBI()
# nagpur.loan(3)
# nagpur.loan(13)
# nagpurPNB = PNB()



# from abc import ABC , absractmethod
class worldBank(ABC):
    @abstractmethod
    def loan(self):
        pass

    @abstractmethod
    def save(self):
        pass
    def country(self):
        print("India")

class SBI(worldBank):
    def loan(self):
        print("loan from SBI")
    
    def save(self):
        print("save from SBI")

class PNB(worldBank):
    def loan(self):
        print("loan from PNB")
    def save(self):
        print("save from PNB")

sbiTwo = SBI()
sbiTwo.loan()
sbiTwo.save()
sbiTwo.country()