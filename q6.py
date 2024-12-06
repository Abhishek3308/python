def calculator():
    x=int(input("enter the 1st number:"))
    y=int(input("enter the 2nd number:"))
    print("1.addition\n2.substractio\n3.multiply\n4.division\n5.exit")
    for i in range(6):
        choice=int(input("enter the choice:"))
        if choice==1:
             sum=x+y
             print(sum)
        elif choice==2:
             difference=x-y
             print(difference)
        elif choice==3:
             product=x*y
             print(product)
        elif choice==4:
            if y!=0:
                division=x/y
                print(division)
            else:
                print("division is not possible")
        elif choice==5:
             exit()
        else:
            print("invalid operation")
calculator()
    
