card = input("enter the card")
if card == "debit card":
    print("tranaction on process")
    language=input("Enter the language")
    if language=="English" or language=="Marathi" or language=="Gujrati" or language=="tamil":
        print("in process")
        pin=int(input("enter the pin"))
        if pin==7890:
            print("in process")
            transaction=input("choose one")
            if transaction=="withdrawal money":
                print("withdrawal")
                account=input("select your account")
                if account=="saving a/c":
                    print("saving a/c")
                    Amount=int(input("enter the amount"))
                    if Amount-10000:
                        print("collect your cash")
                    else:
                        print("try again")
                else:
                    print("current a/c")
            else:
                print("mini statment")
        else:
            print("12345")
    else:
        print("Hindi")
else:
    print("credit card")

                        








