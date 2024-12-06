def bmi(weight,height):
    return weight/(height/100)**2
weight=int(input("enter the weight:"))
height=int(input("enter the height:"))
bmi=bmi(weight,height)
print("bmi is",bmi,"kg/m^2")