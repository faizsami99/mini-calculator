import tkinter
import tkinter.messagebox as sms
import math
v = ""

def suareroot():
    global v
    try:
        i = int(v)
        j = math.sqrt(i)
        text.set('')
        text.set(j)
        v = str(j)
    except:
        sms.showinfo("Notification", "Something went wrong")

def cmsin():
    global v
    try:
        i = int(v)
        j = math.sin(i)
        text.set('')
        text.set(j)
        v = str(j)
    except:
        sms.showinfo("Notification", "Something went wrong")

def cmcos():
    global v
    try:
        i = int(v)
        j = math.cos(i)
        text.set('')
        text.set(j)
        v = str(j)
    except:
        sms.showinfo("Notification", "Something went wrong")
def cmtan():
    global v
    i = int(v)
    j = math.tan(i)
    text.set('')
    text.set(j)
    v = str(j)


def value(num):
    global v
    v += str(num)
    text.set(v)

def clear():
    global v
    v = ''
    text.set(v)

def equal():
    global v
    try:
        r = eval(v)
        text.set('')
        text.set(r)
        v = str(r)
    except:
        sms.showinfo("Notification", "Something went wrong")


main_frame = tkinter.Tk()
main_frame.title("Calculator")
main_frame.geometry("325x365")
main_frame.resizable(False, False)
#main_frame.iconbitmap('git.ico')
main_frame.config(bg="green")

text = tkinter.StringVar()

cal_entry = tkinter.Entry(main_frame, bg="orange", font="arial 20 bold", bd="10", justify="right", textvariable=text)
cal_entry.grid(row=0, columnspan=5)

btn7 = tkinter.Button(main_frame, text="7", font="arial 20 bold", bd=5, padx=16, pady=16, command=lambda:value(7), activebackground="green", activeforeground="white", bg="powder blue")
btn7.grid(row=1, column=0)


btn8 = tkinter.Button(main_frame, text="8", font="arial 20 bold", bd=5, padx=16, pady=16, command=lambda:value(8), activebackground="green", activeforeground="white", bg="powder blue")
btn8.grid(row=1, column=1)

btn9 = tkinter.Button(main_frame, text="9", font="arial 20 bold", bd=5, padx=16, pady=16, command=lambda:value(9), activebackground="green", activeforeground="white", bg="powder blue")
btn9.grid(row=1, column=2)

btnadd = tkinter.Button(main_frame, text="+", font="arial 20 bold", bd=5, padx=16, pady=16, command=lambda:value("+"), activebackground="green", activeforeground="white", bg="powder blue")
btnadd.grid(row=1, column=3)

btn4 = tkinter.Button(main_frame, text="4", font="arial 20 bold", bd=5, padx=16, pady=16, command=lambda:value(4), activebackground="green", activeforeground="white", bg="powder blue")
btn4.grid(row=2, column=0)

btn5 = tkinter.Button(main_frame, text="5", font="arial 20 bold", bd=5, padx=16, pady=16, command=lambda:value(5), activebackground="green", activeforeground="white", bg="powder blue")
btn5.grid(row=2, column=1)

btn6 = tkinter.Button(main_frame, text="6", font="arial 20 bold", bd=5, padx=16, pady=16, command=lambda:value(6), activebackground="green", activeforeground="white", bg="powder blue")
btn6.grid(row=2, column=2)

btnsub = tkinter.Button(main_frame, text="-", font="arial 20 bold", bd=5, padx=19, pady=16, command=lambda:value("-"), activebackground="green", activeforeground="white", bg="powder blue")
btnsub.grid(row=2, column=3) 


btn1 = tkinter.Button(main_frame, text="1", font="arial 20 bold", bd=5, padx=16, pady=16, command=lambda:value(1), activebackground="green", activeforeground="white", bg="powder blue")
btn1.grid(row=3, column=0)

btn2 = tkinter.Button(main_frame, text="2", font="arial 20 bold", bd=5, padx=16, pady=16, command=lambda:value(2), activebackground="green", activeforeground="white", bg="powder blue")
btn2.grid(row=3, column=1) 

btn3 = tkinter.Button(main_frame, text="3", font="arial 20 bold", bd=5, padx=16, pady=16, command=lambda:value(3), activebackground="green", activeforeground="white", bg="powder blue")
btn3.grid(row=3, column=2)

btnmul = tkinter.Button(main_frame, text="*", font="arial 20 bold", bd=5, padx=18, pady=16, command=lambda:value("*"), activebackground="green", activeforeground="white", bg="powder blue")
btnmul.grid(row=3, column=3) 


btn0 = tkinter.Button(main_frame, text="0", font="arial 20 bold", bd=5, padx=16, pady=16, command=lambda:value(0), activebackground="green", activeforeground="white", bg="powder blue")
btn0.grid(row=4, column=0)

btnclear = tkinter.Button(main_frame, text="c", font="arial 20 bold", bd=5, padx=16, pady=16, command=clear, activebackground="green", activeforeground="white", bg="powder blue")
btnclear.grid(row=4, column=1) 

btneql = tkinter.Button(main_frame, text="=", font="arial 20 bold", bd=5, padx=16, pady=16, command=equal, activebackground="green", activeforeground="white", bg="powder blue")
btneql.grid(row=4, column=2)

btndiv = tkinter.Button(main_frame, text="/", font="arial 20 bold", bd=5, padx=19, pady=16, command=lambda:value("/"), activebackground="green", activeforeground="white", bg="powder blue")
btndiv.grid(row=4, column=3) 

btntan = tkinter.Button(main_frame, text="tan", font="arial 20 bold", bd=5, padx=8, pady=16, command=cmtan, activebackground="green", activeforeground="white", bg="powder blue")
btntan.grid(row=4, column=4)

btncmsin = tkinter.Button(main_frame, text="sin", font="arial 20 bold", bd=5, padx=8, pady=16, command=cmsin, activebackground="green", activeforeground="white", bg="powder blue")
btncmsin.grid(row=2, column=4)

btncmcos = tkinter.Button(main_frame, text="cos", font="arial 20 bold", bd=5, padx=5, pady=16, command=cmcos, activebackground="green", activeforeground="white", bg="powder blue")
btncmcos.grid(row=3, column=4)

btnsqr = tkinter.Button(main_frame, text="√", font="arial 20 bold", bd=5, padx=19, pady=16, command=suareroot, activebackground="green", activeforeground="white", bg="powder blue")
btnsqr.grid(row=1, column=4)


main_frame.mainloop()