num = int(input("Input stair of pyramid : "))
for i in range(num):
    print(" "*(num-i),"*"*(((i+1)*2)-1))
