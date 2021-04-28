menuList = []
menuDic = {"แฮมเบอร์เก้อ": 40, "แฟรนฟราย": 90, "น้ำอัดลม": 45}


def BillMenu():
    total = 0
    print("Your order".center(16, "-"))
    for i in range(len(menuList)):
        print(menuList[i][0], menuList[i][1], )
        total += menuList[i][1]
    print("ราคาทั้งหมดรวม", total, "บาท")

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName, menuDic[menuName]])
print(menuList)
BillMenu()

