c = True

while c == True:
    try:
        n = int(input("enter a number"))
    except ValueError:
        print("please enter a valid value")
    else:
        print("You have entered a valid integer so the program will end here")
        c = False
        

