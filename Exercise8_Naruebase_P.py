price = 0
Username = input("Input your username :")
Password = input("Input your password :")
if Username == "User" and Password == "5678":
    print("Welcome", Username)
    print("Please input number to order")
    print("1.chicken price: 10 $")
    print("2.carrot price: 12 $")
    print("3.beetroot price: 5 $")
    print("4.mushroom price: 4 $")
    print("5.oat price: 8 $")
    order = input(">>")
    print("Input how many do you want.")
    numOrder = int(input(">>"))
    if numOrder >= 1:
        if order == "1":
            price = 10
            print("Total price:", price * numOrder, "$")
        elif order == "2":
            price = 12
            print("Total price:", price * numOrder, "$")
        elif order == "3":
            price = 5
            print("Total price:", price * numOrder, "$")
        elif order == "4":
            price = 4
            print("Total price:", price * numOrder, "$")
        elif order == "5":
            price = 8
            print("Total price:", price * numOrder, "$")
        else:
            print("Error this numbers not have in order")
            print("Please try again.")
    else:
        print("Error something wrong.")

else:
    print("Error your account can't sign in.")
