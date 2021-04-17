sex= input("enter male or female")
age= int(input("enter age"))
if sex=="female":
    print("she can work in urban areas")
elif sex=="male":
    if age>=20 and age<40:
        print("he can work in any where")
    else:
        print("do not go any where")
elif sex=="male":
    if age>=40 and age<=60:
        print("he can work in urban areas")
    else:
        print("don't work")
else:
    print("error")


