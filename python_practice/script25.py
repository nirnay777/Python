# class Person:
#     fn = "nirnay"
#     ln = "sangolkar"

#     def display(self):
#         print(self.fn + self.ln)

# # nirnay = Person()
# # nirnay.display()
# rahul = Person()
# rahul.display()

# rahul.fn ="rahul"
# rahul.ln = "gandhi"
# rahul.display()

class Person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    
    def display(self):
        print(self.firstname + self.lastname)

tavish = Person("tavish","anade")
print(tavish.firstname)
print(tavish.lastname)
tavish.display()

nirnay = Person("nirnay","sangolkar")
nirnay.display()