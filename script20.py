
# class greekgod:
    
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
        
#     def displayName(self):
#         print(self.firstName + self.lastName)
            
#     def updateName(self,ln):
#         self.lastName = ln
                     
                     
# alex = greekgod("alex"," eubank")
# print(alex.firstName)
# print(alex.lastName)
# alex.displayName()
# alex.updateName("laid")



# class earth:
    
#     country = "india"
    
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
     
#     def updateName(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
            
#     @classmethod
#     def updateCountry(cls,cnty):
#         cls.country = cnty

# h = earth("sara","saffari")
# print(h.firstName)
# print(h.lastName)
# print(h.country)
# h.country = "hindustan"
# h2=earth("anabelle","lucinda")
# print(h2.country)
# earth.updateCountry('india B')
# print(h.country)
# print(h2.country)    



# class PersonE:
#     count = 0 
#     country = "bharat"
    
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
#         PersonE.count = PersonE.count + 1
        
#     def displayName(self):
#         print(self.firstName+self.lastName)
        
#     @classmethod
#     def updateCountry(cls,cnty):
#         cls.country = cnty
#     @staticmethod
#     def countObj():
#         return PersonE.count
    
# raj = PersonE("raj ","kundra")      
# rohit = PersonE("Rohit","sharma")
# a = PersonE.countObj()
# print(a)













                  