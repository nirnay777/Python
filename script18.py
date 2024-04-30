# class sports:
#     player_name = "Nirnay"
#     last_name = "Sangolkar"
    
#     def dribble(self):
#         print("i am dribbling")
        
#     def shoot(self):
#         print("i am shooting")
        
        
# nirnay = sports()
# print(nirnay.player_name)
# print(nirnay.last_name)
# nirnay.dribble()
# nirnay.shoot()

# rahul = sports()
# print(rahul.player_name)
# print(rahul.last_name)
# rahul.dribble()
# rahul.shoot()        
# rahul.player_name = "rahul"
# rahul.last_name = "arora"
# print(rahul.player_name)
# print(rahul.last_name)


class human:
    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln
    def talk(self):
        print("i love to talk")
    def walk(Self):
        print("i love to walk")
        
nirnay = human("nirnay","sangolkar")        
vedant = human("vedant","gaikwad")
               
print(nirnay.first_name)
print(nirnay.last_name)

print(vedant.first_name)
print(vedant.last_name)

vedant.city = "pune"
print(vedant.city)
nirnay.city = "nagpur"
print(nirnay.city)

            
    