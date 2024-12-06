def calculator():
    x=int(input("enter the 1st number:"))
    y=int(input("enter the 2nd number:"))
    print("1.addition\n2.substractio\n3.multiply\n4.division\n5.exit")
    choice=int(input("enter the choice:"))
    if choice==1:
        sum=x+y
        return sum
    elif choice==2:
        difference=x-y
        return difference
    elif choice==3:
        product=x*y
        return product
    elif choice==4:
        if y!=0:
            division=x/y
            return division
        else:
            print("division is not possible")
    elif choice==5:
        exit()
    else:
        print("invalid operation")
for i in range(6):
    data=calculator()
    print(data)