from tkinter import *
root = Tk()
root.title("calC")


inp = Entry(root,width=45,borderwidth=3)
#inp.grid(row=0,column=0,columnspan=3,padx=3,pady=3)
inp.place(x=0,y=0,width=300,height=25)

def key_pressed(num):
	last_entry = inp.get()
	inp.delete(0,END)
	inp.insert(0,str(last_entry)+ str(num))

def fun_add():
	try:
		expression=eval(str(inp.get()))
	except(SyntaxError):
		inp.delete(0,END)
		inp.insert(0,str(last_entry)+"+")
	else:
		inp.delete(0,END)
		inp.insert(0,str(expression)+"+")

def fun_subtract():
	try:
		expression=eval(str(inp.get()))
	except(SyntaxError):
		inp.delete(0,END)
		inp.insert(0,str(last_entry)+"-")
	else:
		inp.delete(0,END)
		inp.insert(0,str(expression)+"-")

def fun_multiply():
	try:
		expression=eval(str(inp.get()))
	except(SyntaxError):
		inp.delete(0,END)
		inp.insert(0,str(last_entry)+"*")
	else:
		inp.delete(0,END)
		inp.insert(0,str(expression)+"*")

def fun_divide():
	try:
		expression=eval(str(inp.get()))
	except(SyntaxError):
		inp.delete(0,END)
		inp.insert(0,str(last_entry)+"/")
	else:
		inp.delete(0,END)
		inp.insert(0,str(expression)+"/")

	
##########

b1 = Button(root, text="1", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b1.config(command=lambda:key_pressed(1))

b2 = Button(root, text="2", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b2.config(command=lambda:key_pressed(2))

b3 = Button(root, text="3", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b3.config(command=lambda:key_pressed(3))

b4 = Button(root, text="4", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b4.config(command=lambda:key_pressed(4))

b5 = Button(root, text="5", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b5.config(command=lambda:key_pressed(5))

b6 = Button(root, text="6", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b6.config(command=lambda:key_pressed(6))

b7 = Button(root, text="7", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b7.config(command=lambda:key_pressed(7))

b8 = Button(root, text="8", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b8.config(command=lambda:key_pressed(8))

b9 = Button(root, text="9", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b8.config(command=lambda:key_pressed(9))

b0 = Button(root, text="0", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b0.config(command=lambda:key_pressed(0))

b_multiply =  Button(root, text="*", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b_multiply.config(command=fun_multiply)

b_subtract =  Button(root, text="-", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b_subtract.config(command=fun_subtract)

b_division =  Button(root, text="/", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b_division.config(command=fun_divide)

b_add = Button(root, text="+", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b_add.config(command=fun_add)

b_equal =  Button(root, text="=", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")

b_period = Button(root, text=".", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")

b_clear = Button(root,text="Clear")
b_clear.config(command= lambda : inp.delete((END-1),END))

b_reset = Button(root, text="CE", width=10, height=2,bg="black",font=("Helvetica",15),fg="white", relief="flat")
b_reset.config(command=lambda : inp.delete(0,END))


###########
b_clear.grid(row=0,column=3) 

b7.grid(row=1 ,column=0,padx=1,pady=1)
b8.grid(row=1 ,column=1,padx=1,pady=1)
b9.grid(row=1 ,column=2,padx=1,pady=1)
b_multiply.grid(row=1 ,column=3,padx=1,pady=1)

b4.grid(row=2 ,column=0,padx=1,pady=1)
b5.grid(row=2 ,column=1,padx=1,pady=1)
b6.grid(row=2 ,column=2,padx=1,pady=1)
b_subtract.grid(row=2 ,column=3,padx=1,pady=1)

b1.grid(row=3 ,column=0,padx=1,pady=1)
b2.grid(row=3 ,column=1,padx=1,pady=1)
b3.grid(row=3 ,column=2,padx=1,pady=1)
b_add.grid(row=3,column=3,padx=1,pady=1)


b_reset.grid(row=4,column=0,padx=1,pady=1)
b0.grid(row=4, column=1,padx=1,pady=1)
b_period.grid(row=4, column=2,padx=1,pady=1)
b_equal.grid(row=4, column=3,padx=1,pady=1)

########

root.mainloop()


