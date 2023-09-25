from tkinter import *

root=Tk()
root.title("Shreya")
root.configure(bg="black")

eq =""
equation = StringVar()

root.configure(bg='gray69')

#Label
Label1 = Label(root, text="CALCULATOR", bg="gray69",fg="black", font= ("Arial",20),width=22)
Label1.grid(row=0,columnspan=8)

#entry box
textbox = Entry(root, relief=SUNKEN, bd=20, bg="darkseagreen3", fg="black", width=43,insertwidth=18, textvariable=equation)
textbox.grid(row=2, columnspan= 100, sticky=N, ipadx=7,ipady=7,padx=20,pady=20)
#variable

#functions 

def btnclick(num):
    global eq
    eq = eq + str(num)
    equation.set(eq)
    
def result():
    global eq
    total = str(eval(eq))
    equation.set(total)
    eq = ""
    
def clear():
    global eq
    eq = ""
    equation.set("")

#button creation

btn1 = Button(root, text="1",relief=SOLID, font=("Arial" ,12),command= lambda:btnclick(1),bg="darkorchid1",width=6, height= 2)
btn1.grid(row=4,column=1,padx=0,pady=0)
btn2 = Button(root, text="2",relief=SOLID, font=("Arial" ,12),command= lambda:btnclick(2),bg="darkorchid1",width=6, height= 2)
btn2.grid(row=4,column=2,padx=0,pady=0)
btn3 = Button(root, text="3",relief=SOLID, font=("Arial" ,12),command= lambda:btnclick(3),bg="darkorchid1",width=6, height= 2)
btn3.grid(row=4,column=3,padx=0,pady=0)
btn4 = Button(root, text="4",relief=SOLID, font=("Arial" ,12),command= lambda:btnclick(4),bg="darkorchid1",width=6, height= 2)
btn4.grid(row=5,column=1,padx=0,pady=0)
btn5 = Button(root, text="5",relief=SOLID, font=("Arial" ,12),command= lambda:btnclick(5),bg="darkorchid1",width=6, height= 2)
btn5.grid(row=5,column=2,padx=0,pady=0)
btn6 = Button(root, text="6",relief=SOLID, font=("Arial" ,12),command= lambda:btnclick(6),bg="darkorchid1",width=6, height= 2)
btn6.grid(row=5,column=3,padx=0,pady=0)
btn7 = Button(root, text="7",relief=SOLID, font=("Arial" ,12),command= lambda:btnclick(7),bg="darkorchid1",width=6, height= 2)
btn7.grid(row=6,column=1,padx=0,pady=0)
btn8 = Button(root, text="8",relief=SOLID, font=("Arial" ,12),command= lambda:btnclick(8),bg="darkorchid1",width=6, height= 2)
btn8.grid(row=6,column=2,padx=0,pady=0)
btn9 = Button(root, text="9",relief=SOLID, font=("Arial" ,12),command= lambda:btnclick(9),bg="darkorchid1",width=6, height= 2)
btn9.grid(row=6,column=3,padx=0,pady=0)
btn0 = Button(root, text="0",relief=SOLID, font=("Arial" ,12),command= lambda:btnclick(0),bg="darkorchid1",width=6, height= 2)
btn0.grid(row=7,column=2,padx=0,pady=0)

#operators

btn_plus = Button(root, text="+",relief=SOLID, command= lambda:btnclick("+"), font=("Arial" ,12),bg="hotpink2",width=6, height= 2)
btn_plus.grid(row=3,column=4,padx=10,pady=10)
btn_sub = Button(root, text="-",relief=SOLID, command= lambda:btnclick("-"),font=("Arial" ,12),bg="hotpink2",width=6, height= 2)
btn_sub.grid(row=4,column=4,padx=10,pady=10)
btn_mul = Button(root, text="*",relief=SOLID, command= lambda:btnclick("*"),font=("Arial" ,12),bg="hotpink2",width=6, height= 2)
btn_mul.grid(row=5,column=4,padx=10,pady=10)
btn_div= Button(root, text="/",relief=SOLID, command= lambda:btnclick("/"),font=("Arial" ,12),bg="hotpink2",width=6, height= 2)
btn_div.grid(row=6,column=4,padx=10,pady=10)
btn_equal = Button(root, text="=",relief=SOLID, command= result, font=("Arial" ,12),bg="cyan2",width=6, height= 2)
btn_equal.grid(row=7,column=4,padx=10,pady=10)
btn_clear = Button(root, text="AC",relief=SOLID, command= clear ,font=("Arial" ,12),bg="firebrick1",width=6, height= 2)
btn_clear.grid(row=3,column=3,padx=10,pady=10)
btn_pop = Button(root, text="Power",relief=SOLID, command=lambda:btnclick("**"),font=("Arial" ,12),bg="deepskyblue3",width=6, height= 2)
btn_pop.grid(row=3,column=2,padx=10,pady=10)
btn_dot = Button(root, text=".",relief=SOLID,command=lambda:btnclick("."), font=("Arial" ,12),bg="deepskyblue3",width=6, height= 2)
btn_dot.grid(row=3,column=1,padx=10,pady=10)
btn_parop = Button(root, text="(",relief=SOLID,command=lambda:btnclick("("), font=("Arial" ,12),bg="grey",width=6, height= 2)
btn_parop.grid(row=7,column=1,padx=10,pady=10)
btn_parclo = Button(root, text=")",relief=SOLID,command=lambda:btnclick(")"), font=("Arial" ,12),bg="grey",width=6, height= 2)
btn_parclo.grid(row=7,column=3,padx=10,pady=10)

root.mainloop()
