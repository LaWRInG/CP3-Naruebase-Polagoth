def vatcal(x):
    return x + (x * 7/100)

price = int(input("Input price :"))
print(vatcal(price))