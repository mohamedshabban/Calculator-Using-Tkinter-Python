from tkinter import *

# entry=textbox
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=50, borderwidth=5)
# number of buttons in each row =3
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number) )
def button_clear():
    e.delete(0,END)



def button_add():
    first_number=e.get()
    e.delete(0,END)
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)
def button_subtract():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math="subtractaction"
    f_num = int(first_number)
    e.delete(0, END)
def button_multiply():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math="multiplying"
    f_num = int(first_number)
    e.delete(0, END)
def button_division():
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global math
    math="division"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(second_number))
    elif math=="subtractaction":
        e.insert(0,f_num-int(second_number))
    elif math=="multiplying":
        e.insert(0,f_num*int(second_number))
    else:
        e.insert(0,f_num/int(second_number))


# Define Buttons

button_1 = Button(root, text="1", padx=20, pady=40, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=40, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=40, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=40, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=40, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=40, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=40, command=lambda :button_click(7))
button_8 = Button(root, text="8", padx=20, pady=40, command=lambda :button_click(8))
button_9 = Button(root, text="9", padx=20, pady=40, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=40, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=20, pady=40, command=button_add)
button_subtract = Button(root, text="-", padx=20, pady=40, command=button_subtract)
button_Multiply = Button(root, text="*", padx=20, pady=40, command=button_multiply)
button_div = Button(root, text="/", padx=20, pady=40, command=button_division)

button_clear = Button(root, text="Clear", padx=91, pady=40, command=button_clear)
button_equal = Button(root, text="=", padx=79, pady=40, command=button_equal)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)


button_add.grid(row=1, column=3)
button_div.grid(row=3, column=3)
button_Multiply.grid(row=2, column=3)
button_clear.grid(row=4, column=1,columnspan=2)
button_equal.grid(row=5, column=1,columnspan=2)
button_subtract.grid(row=5, column=3)

# Excute program
root.mainloop()
