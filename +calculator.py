#importing Tkinter 
#For python-3 it should be written as tkinter and for less than version-3 it should in camel case.
from tkinter import *
#root will create a GUI window.
root=Tk()
root.title('my calci')
e=Entry(root,font="Arial 25 bold",width=16,bd=5,bg='light blue',justify='right')
e.grid(row=0,column=0,columnspan=4)
#function for entry box
def add(x):
    e.insert(16,x)
#Function for calculations
def result():
    r=eval(e.get())
    e.delete(0,END)
    e.insert(16,r)
#GUI of No. button. Using Grid and also using Anonymus function lambda
#Anonymus function are functions without name

Button(root,text='7',width=5,height=2,command=lambda:add(7)).grid(row=1,column=0,sticky=N+S+E+W)
Button(root,text='8',width=5,height=2,command=lambda:add(8)).grid(row=1,column=1,sticky=N+S+E+W)
Button(root,text='9',width=5,height=2,command=lambda:add(9)).grid(row=1,column=2,sticky=N+S+E+W)
Button(root,text='+',width=5,height=2,command=lambda:add('+')).grid(row=1,column=3,sticky=N+S+E+W)
Button(root,text='4',width=5,height=2,command=lambda:add(4)).grid(row=2,column=0,sticky=N+S+E+W)
Button(root,text='5',width=5,height=2,command=lambda:add(5)).grid(row=2,column=1,sticky=N+S+E+W)
Button(root,text='6',width=5,height=2,command=lambda:add(6)).grid(row=2,column=2,sticky=N+S+E+W)
Button(root,text='-',width=5,height=2,command=lambda:add('-')).grid(row=2,column=3,sticky=N+S+E+W)
Button(root,text='1',width=5,height=2,command=lambda:add(1)).grid(row=3,column=0,sticky=N+S+E+W)
Button(root,text='2',width=5,height=2,command=lambda:add(2)).grid(row=3,column=1,sticky=N+S+E+W)
Button(root,text='3',width=5,height=2,command=lambda:add(3)).grid(row=3,column=2,sticky=N+S+E+W)
Button(root,text='*',width=5,height=2,command=lambda:add('*')).grid(row=3,column=3,sticky=N+S+E+W)
Button(root,text='0',width=5,height=2,command=lambda:add(0)).grid(row=4,column=0,sticky=N+S+E+W)
#reset Button. For reset button no need of lambda function
Button(root,text='c',width=5,height=2).grid(row=4,column=1,sticky=N+S+E+W)
Button(root,text='/',width=5,height=2,command=lambda:add('/')).grid(row=4,column=2,sticky=N+S+E+W)
Button(root,text='=',width=5,height=2,command=result).grid(row=4,column=3,sticky=N+S+E+W)

root.mainloop()
