from forex_python.bitcoin import BtcConverter
import matplotlib.pyplot as plt
import statistics as st
import datetime as dt
from tkinter import *

b = BtcConverter()
btcList = []  # list ของค่าเงินของ btc ในช่วง
dayList = []  # list ของวันที่ของค่าเงินในแต่ละวัน

for x in range(29):
    day = dt.datetime.today() - dt.timedelta(days=x)
    dayList.append(day)
    if x == 0:
        result = b.get_latest_price('THB')
    else:
        result = b.convert_btc_to_cur_on(1, 'THB', day)
    btcList.append(result)

previous = dt.date.today() - dt.timedelta(days=29)  # วันท้ายสุดที่ใช้มาหาค่าเฉลี่ย
str = "ค่าเฉลี่ยตั้งแต่วันที่", dt.date.today(), "ถึง", previous  # ขอความที่นำไปใส่ใน Label

mean = st.mean(btcList)  # ค่าเฉลี่ย


# ค่าเงินของ Btc ในวันนี้
def convert_currency(event):
    convert = b.convert_btc_to_cur_on(float(text_box_btc.get()), 'THB', day)
    result_cur.configure(text=convert)

    # กราฟที่แสดงค่าเปลี่ยนเงินที่เปลี่ยนแปลงของ Btc
def graph(event):
    plt.plot(dayList, btcList, label='THB')

    plt.legend()

    plt.title("Price graph of bitcoin")
    plt.xlabel('Day')
    plt.ylabel('Bath')

    plt.tight_layout()

    plt.show()


# หน้า UI
main = Tk()

label_head_1 = Label(main, text=str)
label_head_1.grid(row=0, column=0)

result_mean = Label(main, text=mean)
result_mean.grid(row=1, column=0)

label_bath2 = Label(main, text='บาท')
label_bath2.grid(row=1, column=1)

label_head_2 = Label(main, text="หาค่าแลกเปลี่ยน Bitcoin เป็นเงิน")
label_head_2.grid(row=2, column=0)

result_cur = Label(main, text="0")
result_cur.grid(row=3, column=0)

label_bath = Label(main, text="บาท")
label_bath.grid(row=3, column=1)

text_box_btc = Entry(main)
text_box_btc.grid(row=4, column=0)

label_bath = Label(main, text='Btc')
label_bath.grid(row=4, column=1)

button_covert = Button(main, text="เปลี่ยน")
button_covert.bind("<Button-1>", convert_currency)
button_covert.grid(row=5, column=0)

button_covert = Button(main, text="แสดงกราฟ")
button_covert.bind("<Button-1>", graph)
button_covert.grid(row=5, column=1)

main.mainloop()
