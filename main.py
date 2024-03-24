from tkinter import * 

root = Tk()
root.title("Calculator App")
root.configure(bg="white")
root.maxsize(325, 385)
root.minsize(325, 385)

images, imglst = ["images/1.ico","images/2.ico","images/3.ico","images/4.ico","images/5.ico","images/6.ico","images/7.ico","images/8.ico","images/9.ico","images/0.ico", "images/c.ico", "images/d.ico", 
        "images/div.ico", "images/multiply.ico", "images/plus.ico", "images/minus.ico", "images/equal.ico", "images/percent.ico", "images/dot.ico"], []

for img in images:
    image = PhotoImage(file=f"{img}")
    image = image.subsample(4, 4)
    imglst.append(image)

def onClick(digit):
    cur = t1.get("1.0", END)
    t1.delete("1.0", END)
    t1.insert("1.0", f'{cur.strip()}{digit}')

def clear():
    global first_no
    global second_no
    global operator

    first_no = 0
    second_no = 0
    operator = ''

    t1.delete("1.0", END)   
    t2.delete("1.0", END)   

def remove_d():
    cur = t1.get("1.0", END).strip()
    if cur:
        t1.delete("1.0", END)
        t2.delete("1.0", END)
        t1.insert("1.0", cur[:-1])       

def operator(opr):
    global first_no
    global operator
    operator = opr

    first_no = int(t1.get("1.0", END).strip())
    t1.delete("1.0", END)
    t1.insert("1.0", f'{first_no}{opr}')

def equal():
    global first_no
    global second_no
    global operator

    number = t1.get("1.0", END).strip()  
    number = number.split(operator)
    second_no = int(number[1])

    match operator:
        case '+':
            t2.insert("1.0", f"{first_no + second_no}")
        case '-':
            t2.insert("1.0", f"{first_no - second_no}")
        case '*':
            t2.insert("1.0", f"{first_no * second_no}")
        case '/':
            t2.insert("1.0", f"{first_no / second_no}")
        case '%':
            t2.insert("1.0", f"{first_no % second_no}")

t1 = Text(root, width=25, height=1, font=("heritage" ,18), borderwidth=0)
t1.grid(row=0, column=0, columnspan=4)

t2 = Text(root, width=15, height=1, font=("heritage" ,24), borderwidth=0)
t2.grid(row=1, column=0, columnspan=4)


button_1 = Button(root, image=imglst[0] , bg="white", borderwidth=0, width=70, height=60, command=lambda: onClick(1))
button_2 = Button(root, image=imglst[1] , bg="white", borderwidth=0, width=70, height=60, command=lambda: onClick(2))
button_3 = Button(root, image=imglst[2] , bg="white", borderwidth=0, width=70, height=60, command=lambda: onClick(3))
button_4 = Button(root, image=imglst[3] , bg="white", borderwidth=0, width=70, height=60, command=lambda: onClick(4))
button_5 = Button(root, image=imglst[4] , bg="white", borderwidth=0, width=70, height=60, command=lambda: onClick(5))
button_6 = Button(root, image=imglst[5] , bg="white", borderwidth=0, width=70, height=60, command=lambda: onClick(6))
button_7 = Button(root, image=imglst[6] , bg="white", borderwidth=0, width=70, height=60, command=lambda: onClick(7))
button_8 = Button(root, image=imglst[7] , bg="white", borderwidth=0, width=70, height=60, command=lambda: onClick(8))
button_9 = Button(root, image=imglst[8] , bg="white", borderwidth=0, width=70, height=60, command=lambda: onClick(9))
button_0 = Button(root, image=imglst[9] , bg="white", borderwidth=0, width=70, height=60, command=lambda: onClick(0))

button_D = Button(root, image=imglst[11], bg="white", borderwidth=0, width=70, height=60, command=remove_d)
button_dot = Button(root, image=imglst[18], bg="white", borderwidth=0, width=70, height=60, command=onClick)
button_add = Button(root, image=imglst[14], bg="white", borderwidth=0, width=70, height=60, command=lambda: operator('+'))
button_moud = Button(root, image=imglst[17], bg="white", borderwidth=0, width=70, height=60, command=lambda: operator('%'))
button_clear = Button(root, image=imglst[10], bg="white", borderwidth=0, width=70, height=60, command=clear)
button_equal = Button(root, image=imglst[16], bg="white", borderwidth=0, width=70, height=60, command=equal)
button_divide = Button(root, image=imglst[12], bg="white", borderwidth=0, width=70, height=60, command=lambda: operator('/'))
button_multipy = Button(root, image=imglst[13], bg="white", borderwidth=0, width=70, height=60, command=lambda: operator('*'))
button_subtract = Button(root, image=imglst[15], bg="white", borderwidth=0, width=70, height=60, command=lambda: operator('-'))

button_clear.grid(row=2, column=0)
button_divide.grid(row=2, column=1)
button_multipy.grid(row=2, column=2)
button_D.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_equal.grid(row=5, column=3, rowspan=2)

button_dot.grid(row=6, column=0)
button_0.grid(row=6, column=1)
button_moud.grid(row=6, column=2)

root.mainloop()