from tkinter import *
import math

currency_all = ["BTC", "ETH", "THETA", "XRP", "BNB", "LTC", "ADA", "BCH", "USDT", "EOS", "LUNA", "CHZ", "XLM", "XMR",
                "DOGE", "THB"]
n = 0
n2 = 0


def currency_1_previous_command():
    global n
    if n == 0:
        n = n
    else:
        n -= 1
    currency_1_type = currency_all[0 + n]
    currency_1.config(text=currency_1_type)


def currency_1_next_command():
    global n
    if n == 15:
        n = n
    else:
        n += 1
    currency_1_type = currency_all[0 + n]
    currency_1.config(text=currency_1_type)


def currency_2_previous_command():
    global n2
    if n2 == 0:
        n2 = n2
    else:
        n2 -= 1
    currency_2_type = currency_all[0 + n2]
    currency_2.config(text=currency_2_type)
    if n2 == 0:
        currency_2_per_price = 1788090.30
    if n2 == 1:
        currency_2_per_price = 53496.72
    if n2 == 2:
        currency_2_per_price = 415.32
    if n2 == 3:
        currency_2_per_price = 17.45
    if n2 == 4:
        currency_2_per_price = 8289.58
    if n2 == 5:
        currency_2_per_price = 6019.68
    if n2 == 6:
        currency_2_per_price = 35.98
    if n2 == 7:
        currency_2_per_price = 16324.38
    if n2 == 8:
        currency_2_per_price = 31.04
    if n2 == 9:
        currency_2_per_price = 131.07
    if n2 == 10:
        currency_2_per_price = 575.44
    if n2 == 11:
        currency_2_per_price = 16.78
    if n2 == 12:
        currency_2_per_price = 12.53
    if n2 == 13:
        currency_2_per_price = 6970.10
    if n2 == 14:
        currency_2_per_price = 1.74
    if n2 == 15:
        currency_2_per_price = 1
    currency_2_per.config(text='ราคาต่อ 1 เหรียญ = %s บาท' % currency_2_per_price)


def currency_2_next_command():
    global n2
    if n2 == 15:
        n2 = n2
    else:
        n2 += 1
    currency_2_type = currency_all[0 + n2]
    currency_2.config(text=currency_2_type)
    if n2 == 0:
        currency_2_per_price = 1788090.30
    if n2 == 1:
        currency_2_per_price = 53496.72
    if n2 == 2:
        currency_2_per_price = 415.32
    if n2 == 3:
        currency_2_per_price = 17.45
    if n2 == 4:
        currency_2_per_price = 8289.58
    if n2 == 5:
        currency_2_per_price = 6019.68
    if n2 == 6:
        currency_2_per_price = 35.98
    if n2 == 7:
        currency_2_per_price = 16324.38
    if n2 == 8:
        currency_2_per_price = 31.04
    if n2 == 9:
        currency_2_per_price = 131.07
    if n2 == 10:
        currency_2_per_price = 575.44
    if n2 == 11:
        currency_2_per_price = 16.78
    if n2 == 12:
        currency_2_per_price = 12.53
    if n2 == 13:
        currency_2_per_price = 6970.10
    if n2 == 14:
        currency_2_per_price = 1.74
    if n2 == 15:
        currency_2_per_price = 1
    currency_2_per.config(text='ราคาต่อ 1 เหรียญ = %s บาท' % currency_2_per_price)


def currency_total():
    try:
        if n == 0:
            c_c1 = 1788090.30
        if n == 1:
            c_c1 = 53496.72
        if n == 2:
            c_c1 = 415.32
        if n == 3:
            c_c1 = 17.45
        if n == 4:
            c_c1 = 8289.58
        if n == 5:
            c_c1 = 6019.68
        if n == 6:
            c_c1 = 35.98
        if n == 7:
            c_c1 = 16324.38
        if n == 8:
            c_c1 = 31.04
        if n == 9:
            c_c1 = 131.07
        if n == 10:
            c_c1 = 575.44
        if n == 11:
            c_c1 = 16.78
        if n == 12:
            c_c1 = 12.53
        if n == 13:
            c_c1 = 6970.10
        if n == 14:
            c_c1 = 1.74
        if n == 15:
            c_c1 = 1

        if n2 == 0:
            c_c2 = 1788090.30
        if n2 == 1:
            c_c2 = 53496.72
        if n2 == 2:
            c_c2 = 415.32
        if n2 == 3:
            c_c2 = 17.45
        if n2 == 4:
            c_c2 = 8289.58
        if n2 == 5:
            c_c2 = 6019.68
        if n2 == 6:
            c_c2 = 35.98
        if n2 == 7:
            c_c2 = 16324.38
        if n2 == 8:
            c_c2 = 31.04
        if n2 == 9:
            c_c2 = 131.07
        if n2 == 10:
            c_c2 = 575.44
        if n2 == 11:
            c_c2 = 16.78
        if n2 == 12:
            c_c2 = 12.53
        if n2 == 13:
            c_c2 = 6970.10
        if n2 == 14:
            c_c2 = 1.74
        if n2 == 15:
            c_c2 = 1
        currency_input_get = int(currency_input.get())
        if currency_input_get > 0:
            currency_result = currency_input_get * c_c1 / c_c2
            currency_result = currency_result * 10000000
            currency_result = math.floor(currency_result)
            currency_result = currency_result / 10000000
            currency_total.config(text=currency_result, bg='green')
        else:
            currency_total.config(text='Error - ค่าเงินน้อยกว่าศูนย์', bg='red')
    except ValueError:
        currency_total.config(text='Error - จำนวนเงินไม่ใช่ตัวเลขจำนวนเต็ม', bg='red')


window = Tk()

window.title('แปลงสกุลเงิน Cryptocurrency')
window.minsize(1200, 700)

app_title = Label()
app_title.config(font=('PrintAble4U', 45, 'bold'), text="โปรแกรมแปลงสกุลเงิน Crypto Currency", width=32)
app_title.place(x=200, y=50)

currency_1 = Label()
currency_1.config(font=('PrintAble4U', 30, 'bold'), text='BTC', height=1, width=6)

currency_1_previous = Button()
currency_1_previous.config(font=('PrintAble4U', 15, 'bold'), text='^', command=currency_1_previous_command, height=1, width=3, activebackground="#dddddd")
currency_1_previous.place(x=230, y=150)

currency_1_next = Button()
currency_1_next.config(font=('PrintAble4U', 15, 'bold'), text='v', command=currency_1_next_command, height=1, width=3, activebackground="#dddddd")
currency_1_next.place(x=230, y=340)

currency_1.place(x=190, y=240)

currency_2 = Label()
currency_2.config(font=('PrintAble4U', 30, 'bold'), text='BTC', height=1, width=6)

currency_2_previous = Button()
currency_2_previous.config(font=('PrintAble4U', 15, 'bold'), text='^', command=currency_2_previous_command, height=1, width=3, activebackground="#dddddd")
currency_2_previous.place(x=940, y=150)

currency_2_next = Button()
currency_2_next.config(font=('PrintAble4U', 15, 'bold'), text='v', command=currency_2_next_command, height=1, width=3, activebackground="#dddddd")
currency_2_next.place(x=940, y=340)

currency_2.place(x=900, y=240)

currency_2_per = Label()
currency_2_per.config(font=('PrintAble4U', 15), text='ราคาต่อ 1 เหรียญ = 1788090.30', width=32,)
currency_2_per.place(x=800, y=300)

currency_input = Entry()
currency_input.config(font=('PrintAble4U', 20, 'bold'), text='ใส่จำนวนเต็มเท่านั้น')
currency_input.place(x=470, y=340)

currency_text = Label()
currency_text.config(font=('PrintAble4U', 20, 'bold'), text='จำนวน')
currency_text.place(x=410, y=340)

button = Button()
button.config(font=('PrintAble4U', 40, 'bold'), text='แปลงค่า', command=currency_total, bg="#96bb7c", activebackground="#184d47", activeforeground="#fffefa")
button.place(x=500, y=210)

currency_total_text = Label()
currency_total_text.config(font=('PrintAble4U', 30, 'bold'), text='ค่าเงิน Currency ที่แปลงออกมาได้คือ', width=32)
currency_total_text.place(x=300, y=470)

currency_total = Label()
currency_total.config(font=('PrintAble4U', 30, 'bold'), text='0', width=32)
currency_total.place(x=300, y=540)

currency_2_text = Label()
currency_2_text.config(font=('PrintAble4U', 15, 'bold'), text='สกุลเงิน', width=32)
currency_2_text.place(x=810, y=200)

currency_1_text = Label()
currency_1_text.config(font=('PrintAble4U', 15, 'bold'), text='สกุลเงิน', width=32)
currency_1_text.place(x=100, y=200)

ending = Label()
ending.config(font=('PrintAble4U', 15, 'bold'), text="สกุลเงินต่าง ๆ อัพเดทวันที่24/03/2021", fg="#807d75")
ending.place(x=0, y=670)

window.mainloop()
