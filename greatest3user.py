num1=int(input("enter any no."))
num2=int(input("enter any no."))
num3=int(input("enter any no."))
if num1!=num2 or num2!=num3 or num3!=num1:
    if num1>=num2 and num1>=num3:
        print(num1,"it is greater")
        if num2>=num1 or num2>=num3:
            print(num2,"it is greater")
            if num3>=num1 or num3>=num2:
               print(num3,"it is greater")
            else:
                print(num3,'it is smaller')
        else:
            print(num2,"it is smaller")
    else:
        print(num1,"it is smaller")
else:
    print("similar number")
