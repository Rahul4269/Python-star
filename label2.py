from tkinter import *
r=Tk()
r.configure(background="orange")
label1=Label(r,text="mango",relief=FLAT)
label2=Label(r,text="apple",relief=GROOVE)
label3=Label(r,text="orange",relief=SUNKEN)
label4=Label(r,text="banana",relief=RIDGE)
label5=Label(r,text="pineapple",relief=RAISED)

label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
r.mainloop()