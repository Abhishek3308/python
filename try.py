x=int(input("enter the 1st number:"))
y=int(input("enter the 2nd number"))
def calculator(x,y):
    print("1.addition\n2.substraction\n3.mutiplication\n4.division\n5.exit\n")
    for i in range(6):
        ch=int(input("enter the choice"))
        if ch==1:
            sum=x+y
            print(sum)
        elif ch==2:
            difference=x-y
            print(difference)
        elif ch==3:
            product=x*y
            print(product)
        elif ch==4:
            if y!=0:
                division=x/y
                print(division)
            else:
                print("division is not possible")
        elif ch==5:
            exit()
        else:
            print("invalid choice")
calculator(x,y)
