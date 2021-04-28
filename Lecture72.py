menuList = []

def BillMenu():
    total = 0
    print("Your order".center(16, "-"))
    for i in range(len(menuList)):
        print(menuList[i][0], "ราคา", menuList[i][1], "บาท")
        total += menuList[i][1]
    print("ราคาทั้งหมดรวม", total, "บาท")

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Please Enter Price : "))
        menuList.append([menuName, menuPrice])
print(menuList)
BillMenu()

