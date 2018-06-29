from tkinter import *
from winsound import *
import math


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)


    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "raise":
            self.total = self.total ** self.current
        if self.op == "rootof":
            self.total = self.total ** (1/self.current)
        if self.op == "fact":
            self.total=int(text_box.get())
            self.total=math.factorial(self.total)
        if self.op == "ln":
            self.total = log(self.total)
        if self.op == "log":
            self.total=log(self.total,10)
        if self.op == "sine":
            self.total=math.sin(self.total)
        if self.op == "cosine":
            self.total = math.cos(self.total)
        if self.op == "tangent":
            self.total = math.tan(self.total)
        if self.op == "exp":
            self.total = math.exp(self.total)
        if self.op == "inv":
            self.total = 1/self.total
        if self.op == "rad":
            self.total=math.radians(self.total)
        if self.op == "deg":
            self.total=math.degrees(self.total)
        if self.op == "acosh":
            self.total=math.acosh(self.total)
        if self.op == "atanh":
            self.total=math.atanh(self.total)
        if self.op == "asinh":
            self.total=math.asinh(self.total)
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def clear(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_clear(self):
        self.clear()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

sum1 = Calc()
root = Tk()
calc = Frame(root,bg="black")
calc.grid()

root.title("Science Calculator")
root.geometry
text_box = Entry(calc, justify=RIGHT,width=30,font="Times 16 bold")
text_box.grid(row = 0, column = 0,columnspan = 8,padx=30, pady = 30)
text_box.insert(0, "0")
play = lambda: Playsound("click_one.wav", SND_FILENAME)


bttn_1 = Button(calc,height =2,width=4,padx=10, pady = 10,command = play, text = "1",bg="grey")
bttn_1["command"] = lambda: sum1.num_press(1)
bttn_1.grid(row = 1, column = 1,  padx=1, pady = 1)

bttn_2 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "2",bg="grey")
bttn_2["command"] = lambda: sum1.num_press(2)
bttn_2.grid(row = 1, column = 2,  padx=1, pady = 1)

bttn_3 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "3",bg="grey")
bttn_3["command"] = lambda: sum1.num_press(3)
bttn_3.grid(row = 1, column = 3,  padx=1, pady = 1)

bttn_4 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "4",bg="grey")
bttn_4["command"] = lambda: sum1.num_press(4)
bttn_4.grid(row = 2 , column = 1,  padx=1, pady = 1)

bttn_5 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "5",bg="grey")
bttn_5["command"] = lambda: sum1.num_press(5)
bttn_5.grid(row = 2 , column = 2,  padx=1, pady = 1)

bttn_6 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "6",bg="grey")
bttn_6["command"] = lambda: sum1.num_press(6)
bttn_6.grid(row = 2 , column = 3,  padx=1, pady = 1)

bttn_7 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "7",bg="grey")
bttn_7["command"] = lambda: sum1.num_press(7)
bttn_7.grid(row = 3 , column = 1,  padx=1, pady = 1)

bttn_8 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "8",bg="grey")
bttn_8["command"] = lambda: sum1.num_press(8)
bttn_8.grid(row = 3, column = 2,  padx=1, pady = 1)

bttn_9 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "9",bg="grey")
bttn_9["command"] = lambda: sum1.num_press(9)
bttn_9.grid(row = 3, column = 3,  padx=1, pady = 1)

bttn_0 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "0",bg="grey")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 2,  padx=1, pady = 1)

div = Button(calc,height =2,width=4,padx=10, pady = 10, text = "/",bg="purple")
div["command"] = lambda: sum1.operation("divide")
div.grid(row = 1, column = 4, padx=1, pady = 1)

mult = Button(calc,height =2,width=4,padx=10, pady = 10, text = "*",bg="purple")
mult["command"] = lambda: sum1.operation("times")
mult.grid(row = 2, column = 4,  padx=1, pady = 1)

minus = Button(calc,height =2,width=4,padx=10, pady = 10, text = "-",bg="purple")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 4, padx=1, pady = 1)

add = Button(calc,height =2,width=4,padx=10, pady = 10, text = "+",bg="purple")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 4,  padx=1, pady = 1)

power = Button(calc, height=2,width=4,padx=10,pady=10,text="x^y",bg="green")
power["command"] = lambda: sum1.operation("raise")
power.grid(row=2,column = 5,padx=1,pady=1)

rootof = Button(calc, height=2, width=4, padx=10, pady=10, text="y-\/x", bg = "green")
rootof["command"] = lambda: sum1.operation("rootof")
rootof.grid(row=2, column=6, padx=1, pady=1)

fact = Button(calc, height=2, width=4, padx=10, pady=10, text="!",bg="green")
fact["command"] = lambda: sum1.operation("fact")
fact.grid(row=3,column=5, padx=1, pady=1)

loge = Button(calc, height=2, width=4, padx=10, pady=10, text="ln",bg="green")
loge["command"] = lambda: sum1.operation("ln")
loge.grid(row=3, column=6, padx=1, pady=1)

log10 = Button(calc, height=2, width=4, padx=10, pady=10, text="log",bg="green")
log10["command"]= lambda: sum1.operation("log")
log10.grid(row=4, column=5, padx=1 , pady=1)

sine = Button(calc, height=2,width=4, padx=10,pady=10, text = "sin" , bg= "green")
sine["command"]=lambda: sum1.operation("sine")
sine.grid(row=5,column=1,padx=1,pady=1)


rad=Button(calc, height=2,width=4, padx=10,pady=10, text = "rad" , bg= "green")
rad["command"]=lambda: sum1.operation("rad")
rad.grid(row=1,column=0,padx=1,pady=1)

deg=Button(calc, height=2,width=4, padx=10,pady=10, text = "deg" , bg= "green")
deg["command"]=lambda: sum1.operation("deg")
deg.grid(row=2,column=0,padx=1,pady=1)

cos=Button(calc, height=2,width=4, padx=10,pady=10, text = "cos" , bg= "green")
cos["command"]=lambda: sum1.operation("cos")
cos.grid(row=5,column=2,padx=1,pady=1)

acosh = Button(calc, height=2,width=4, padx=10,pady=10, text = "acosh" , bg= "green")
acosh["command"]=lambda: sum1.operation("acosh")
acosh.grid(row=3,column=0,padx=1,pady=1)

asinh = Button(calc, height=2,width=4, padx=10,pady=10, text = "acosh" , bg= "green")
asinh["command"]=lambda: sum1.operation("asinh")
asinh.grid(row=4,column=0,padx=1,pady=1)

atanh = Button(calc, height=2,width=4, padx=10,pady=10, text = "acosh" , bg= "green")
atanh["command"]=lambda: sum1.operation("atanh")
atanh.grid(row=5,column=0,padx=1,pady=1)

tangent = Button(calc, height=2,width=4, padx=10,pady=10, text = "tan" , bg= "green")
tangent["command"]=lambda: sum1.operation("tangent")
tangent.grid(row=5,column=3,padx=1,pady=1)

exponent = Button(calc, height=2, width=4, padx=10, pady=10, text='e^x', bg="green")
exponent["command"]=lambda: sum1.operation("exp")
exponent.grid(row=5,column=4,padx=1,pady=1)

inv = Button(calc, height=2, width=4, padx=10, pady=10, text="1/x", bg="green")
inv["command"] = lambda: sum1.operation("inv")
inv.grid(row=5,column=5,padx=1,pady=1)

point = Button(calc,height =2,width=4,padx=10, pady = 10, text = ".",bg="white")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 1, padx=1, pady = 1)

neg= Button(calc,height =2,width=4,padx=10, pady = 10, text = "+/-",bg="white")
neg["command"] = sum1.sign
neg.grid(row = 4, column = 3,  padx=1, pady = 1)


clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "C",bg="white")
clear["command"] = sum1.clear
clear.grid(row = 1, column = 5,  padx=1, pady = 1)

all_clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "AC",bg="white")
all_clear["command"] = sum1.all_clear
all_clear.grid(row = 1, column = 6, padx=1, pady = 1)

equals = Button(calc,height =6,width=4,padx=10, pady = 10, text = "=",bg="green")
equals["command"] = sum1.calc_total
equals.grid(row = 4, column = 6,columnspan=1,rowspan=2,padx=1, pady = 1)

root.mainloop()
