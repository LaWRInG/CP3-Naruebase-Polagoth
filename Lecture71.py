priceList = []
menuList = []

def BillMenu():
    total = 0
    print("Your order".center(12, "-"))
    for i in range(len(menuList)):
        print(menuList[i], priceList[i])
        total += priceList[i]
    print(total)

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Please Enter Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
BillMenu()

