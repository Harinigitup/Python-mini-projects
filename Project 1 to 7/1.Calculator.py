from tkinter import 
root = Tk() 

input Entry (root, width-50)
input.grid(row-0,column-e,columnspan 3, padx-15, pady-15)

def click(num):
current input.get() 
input.delete(0,END) 
input.insert(0,str(current)+str(num))
return 

def add(): 
current input.get() 

def clear():
input.delete(0, END) 
return

def equal():
current input.get()
sum = int(current) 
input.delete(8,END) 
input.insert(0,stefnum sum))

button 0-Button(root, text-"0", padx-50, pady-25, command-lambda:click(0)) 
button 1 Button(root, text="1",padx=50,pady=25,command=lambda:click(1)) 
button 2-Button(root,text="2", padx-50, pady 25, command-lambda:click(2)) 
button 3-Button(root, text="3",padx=50,pady-25, command-labda:click(3)) 
button 4-Button(root,text="4", padx-50, pady-25, command Lombda:click(4))
button 5-Button(root,text="5",padx=50,pady-25, command-lambda:click(5)) 
button 6-Button(root, text="6", padx-50, pady-25, command-lambda:click(6)) 
button 7-Button(root,text-"7", padx-50,pady-25, command-lambda:click(7)) 
button 8-Button(root, text="8", padx=50,pady 25, command-lambda:click(8))
button 9-Button(root, text="9", padx-50, pady-25, command-lambda:click(9))
button add llutton(root, text="+", padx=50,pady=25,command=add) 
button clear-Button(root, text="AC", padx-50, pady-25, command-clear) 
button equal-Button(root, text="",padx-50, pady-25, command-equal)

button 7.grid(row-1.column-0)
button 8.grid(row=1.column=1)
button 9.grid(row-1,column-2)

button 4.grid(row-2,column-0)
button 5.grid(row-2,column-1)
button 6.grid(row-2,column=2)

button 1.grid(row-3,column=0) 
button_2.grid(row=3,column=1) 
button 3.grid(row-3,column-2)

button 0.grid(row-4,column-0)
button_add.grid(row=4,column-1,columnspan=2)

button_clear.grid(row-5,column-0)
button equal.grid(row-5,column-1,columnspan>2)

root.mainloop() 
