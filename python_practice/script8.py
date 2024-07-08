mobile = ["samsung","apple","nokia","blackberry"]
mobile.append("realme")
print(mobile)

mobile.pop()
print(mobile)
mobile.pop(1)
print(mobile)

mobile.remove("samsung")
print(mobile)

mobile.clear()
print(mobile)

mobile.insert(0,"google")
mobile.insert(1,"motorola")
print(mobile)


midmaestro = ["xavi","iniesta"]
bestmid = ["kroos","modric","casemiro"]
bestmid.extend(midmaestro)
print(bestmid)
print(midmaestro)