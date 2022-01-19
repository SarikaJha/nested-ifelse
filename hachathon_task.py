from tkinter import*
def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)


def btnClear():
    global val
    val=""
    data.set("")



def btnEqual():
    global val
    result=str(eval(val))
    data.set(result)

root=Tk()
root.title("Tkinter calcualtor")
root.geometry("362x381+500+200")
val=""
data=StringVar()

from tkinter import*
def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)


def btnClear():
    global val
    val=""
    data.set("")



def btnEqual():
    global val
    result=str(eval(val))
    data.set(result)

root=Tk()
root.title("Tkinter calcualtor")
root.geometry("362x381")
val=""
data=StringVar()

impression=Entry(root,textvariable=data,bd=45,justify="right",bg="purple",font=("arizoana",40,"bold"))
impression.grid(row=0,columnspan=4)
btn7=Button(root,text="7",padx=14,pady=14,font=("ariel",15,"italic"),bd=10,bg="yellow",height=2,width=8,command=lambda:btnclick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",padx=14,pady=14,font=("ariel",15,"italic"),bd=10,bg="yellow",height=2,width=8,command=lambda:btnclick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",padx=14,pady=14,font=("ariel",15,"italic"),bd=10,bg="yellow",height=2,width=8,command=lambda:btnclick(9))
btn9.grid(row=1,column=2)
btn4=Button(root,text="4",padx=14,pady=14,font=("ariel",15,"italic"),bd=10,bg="yellow",height=2,width=8,command=lambda:btnclick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",padx=14,pady=14,font=("ariel",15,"italic"),bd=10,bg="yellow",height=2,width=8,command=lambda:btnclick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",padx=14,pady=14,font=("ariel",15,"italic"),bd=10,bg="yellow",height=2,width=8,command=lambda:btnclick(6))
btn6.grid(row=2,column=2)
btn1=Button(root,text="1",padx=14,pady=14,font=("ariel",15,"italic"),bd=10,bg="yellow",height=2,width=8,command=lambda:btnclick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",padx=14,pady=14,font=("ariel",15,"italic"),bd=10,bg="yellow",height=2,width=8,command=lambda:btnclick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",padx=14,pady=14,font=("ariel",15,"italic"),bd=10,bg="yellow",height=2,width=8,command=lambda:btnclick(3))
btn3.grid(row=3,column=2)
btn0=Button(root,text="0",padx=14,pady=14,font=("ariel",15,"italic"),bd=10,bg="yellow",height=2,width=8,command=lambda:btnclick(0))
btn0.grid(row=4,column=0)
btn_division=Button(root,text="//",font=("ariel",20,"italic"),bd=10,bg="white",height=2,width=8,command=lambda:btnclick("//"))
btn_division.grid(row=4,column=1)
btn_Equal=Button(root,text="=",font=("ariel",20,"italic"),bd=10,bg="white",height=2,width=8,command=btnEqual)
btn_Equal.grid(row=4,column=2)
btn_add=Button(root,text="+",font=("ariel",20,"italic"),bd=10,bg="white",height=2,width=8,command=lambda:btnclick("+"))
btn_add.grid(row=1,column=3)
btn_sub=Button(root,text="-",font=("ariel",20,"italic"),bd=10,bg="white",height=2,width=8,command=lambda:btnclick("-"))
btn_sub.grid(row=2,column=3)
btn_multi=Button(root,text="*",font=("ariel",20,"italic"),bd=10,bg="white",height=2,width=8,command=lambda:btnclick("*"))
btn_multi.grid(row=3,column=3)
btn_Clear=Button(root,text="clear",font=("ariel",20,"italic"),bg="white",bd=10,height=2,width=8,command=btnClear)
btn_Clear.grid(row=4,column=3)
root.mainloop()