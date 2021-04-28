from tkinter import *

def leftClick(event):
    print (float(textBoxWeight.get())/(float(textBoxHight.get())/100)**2)
    BMI = float(textBoxWeight.get())/(float(textBoxHight.get())/100)**2
    if BMI < 18.5:
        result.configure(text="ผอมเกินไป")
    elif BMI >= 18.5 and BMI <= 22.9:
        result.configure(text = "น้ำหนักปกติ เหมาะสม")
    elif BMI >= 23 and BMI <= 24.9:
        result.configure(text = "น้ำหนักเกิน")
    elif BMI >= 25 and BMI <= 29.9:
        result.configure(text = "อ้วน")
    elif BMI > 30:
        result.configure(text = "อ้วนมาก")

main = Tk()

labelHight = Label(main,text="ส่วนสูง(cm.)")
labelHight.grid(row = 1,column =0)
textBoxHight = Entry(main)
textBoxHight.grid(row = 1,column =1)

labelWeight= Label(main,text="น้ำหนัก(Kg.)")
labelWeight.grid(row = 0,column =0)
textBoxWeight = Entry(main)
textBoxWeight.grid(row = 0,column =1)

calculateButton = Button(main,text = "คำนวณ")
calculateButton.bind("<Button-1>",leftClick)
calculateButton.grid(row = 2)

result = Label(main,text="ผลรับ")
result.grid(row = 2,column = 1)


main.mainloop()