# class Calculator:
#     def addition(self,x,y):
#         print(x+y)
    
#     def addition(self,x,y,z):
#         print(x+y+z)
    
#     def addititon(self,x,y,z,a):
#         print(x+y+z+a)
        
#     def addition(self, x = None, y = None , z = None, a = None):
#         if(x != None and y !=None and z != None and a != None):
#             print(x+y+z+a)
#         elif(x != None and y != None and z != None):
#             print(x+y+z)
#         elif(x !=None and y !=None):
#             print(x+y)
            
# cal = Calculator()
# cal.addition(23,4,6,5)
# cal.addition(23,4,5)
# cal.addition(23,5)


# class Dog:
#     def talk(self):
#         print("Bhow Bhow")

# class Human:
#     def talk(self):
#         print("Hello hi")

# def call_talk(obj):
#     obj.talk()

# a = Human()
# b = Dog()

# call_talk(a)
# call_talk(b)



# class Dog:
#     def talk(self):
#         print("bhow bhow")
        
# class human:
#     def talk(self):
#         print("hello hi")

# class duck:
#     def sound(self):
#         print("quack quack")

# def call_talk(obj):
#     if hasattr(obj,'talk'):
#         obj.talk()
#     else:
#         obj.sound()

# a = human()
# b = Dog()
# c = duck()



# call_talk(a)
# call_talk(b)
# call_talk(c)    



# class Bookx:
#     def __init__(self,pages):
#         self.pages = pages
#     def __add__(self,other):
#         return self.pages + other.pages
    

    
# class Booky:
#     def __init__(self,pages):
#             self.pages = pages
#     def __add__(self,others):
#             return self.pages > others.pages
        
# ramayana = Bookx(130)
# mahabharat = Booky(150)

# print(ramayana.pages + mahabharat.pages)



# class BookA:
#     def __init__(self,pages):
#         self.pages = pages
#     def __gt__(self,others):
#         return self.pages > others.pages

# class BookB:
#     def __init__(self,pages):
#         self.pages = pages
#     def __lt__(self,others):
#         return self.pages > others.pages
    
# rajiv = BookA(100)
# priyansh = BookB(140)

# print(rajiv.pages > priyansh.pages)
# print(rajiv > priyansh)
# print(rajiv < priyansh)


# class WorkBank:
#     def loan(self):
#         print("i am loan from WB")
#     def save(self):
#         print('i am save from WB')
    
# class IDBI(WorkBank):
#     def loan(self):
#         print("i am loan from IDBI")
#         super().loan()
#     def save(self):
#         print('i am save from IDBI')
#         super().loan()

# class ICICI(WorkBank):
#     def loan(self):
#         print("i am loan from ICICI")
#         super().loan()
#     def save(self):
#         print("i am save from ICICI")
#         super().save()
        
# a = IDBI()
# a.loan()
# a.save()
    



        











    










    