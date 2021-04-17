report=input("check the report")
num=int(input("enter the no. of girls"))
if report=="yes":
    print("she can not be quarantine")
elif report=="no":
    print("she has to be quarantine")
    if num<=6:
        print("she can stay in this room")    
        bedno=int(input("enter the bed no."))
        if bedno==1:
            print("someone is there")
        elif bedno==2:
            print("It is Empty")
        elif bedno==3:
            print("someone is there")
        elif bedno==4:
            print("some one is there")
        elif bedno==5:
            print("it is empty")
        elif bedno==6:
            print("someone is there")
        else:
            print("Bed number is not avalaible")
    else:
        print("she has to go in other room")
else:
    print("nothing")