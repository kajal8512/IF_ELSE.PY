num1=int(input("enter any no."))
num2=int(input("enter any no."))
calculator=(input("enter any symbol"))
if calculator=="+":
    print(num1+num2,"addition")
elif calculator=="-":
    print(num1-num2,"subtraction")
elif calculator=="*":
    print(num1*num2,"multiplication")
elif calculator=="/":
    print(num1/num2,"division")
elif calculator=="%":
    print(num1%num2,"modulus")
elif calculator=="**":
    print(num1**num2,"exponent")
elif calculator=="//":
    print(num1//num2,"integer or floor division")
else:
    print("nothing")