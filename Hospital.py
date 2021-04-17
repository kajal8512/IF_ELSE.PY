day= input("enter the day")
if day == "thursday":
    print("holiday")
    disco=input("enter disco name")
    if disco=="danno":
        print("danno") 
        permision=input("take permision from disco")
        if permision=="yes":
            print("they can go")
            place=input("enter the place")
            if place=="Hospital":
                print("they want to go hospital")
                precaution=input("take precaution")
                if precaution=="yes":
                    print("sanitizer and mask")
                else:
                    print("don't have")
            else:
                print("not go")
        else:
            print("no")
    else:
        print("mehashbeen")
else:
    print("not a holiday")


