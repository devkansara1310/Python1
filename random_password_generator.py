from tkinter import *
import pyperclip
import random,string
import array

root=Tk()
root.geometry('400x300')
random_password = StringVar()
len = IntVar()

def password(): 
  s1 = string.ascii_uppercase
  r1= random.choice(s1)
  s2 = string.ascii_lowercase
  r2= random.choice(s2)
  s3 = string.digits
  r3= random.choice(s3)
  s4 = string.punctuation
  r4= random.choice(s4)

  temp = r1+r2+r3+r4
  all = s1+s2
  
  for x in range(len.get()-4):
    temp = temp + random.choice(all)
    password_list = array.array('u', temp)
    random.shuffle(password_list)  
  password = ""
  for x in password_list:
    password = password + x
  random_password.set(password)

def copy():
  copy=random_password.get()
  pyperclip.copy(copy)

Label(root,text="Password Generator",font="Calibri 20 bold").pack()
Label(root,text="Enter Password Length").pack(pady=3)
Entry(root,textvariable=len).pack(pady=3)
Button(root,text="Generate Password",command=password).pack()
Entry(root,textvariable=random_password).pack(pady=3)
Button(root,text="Copy to Clipboard",command=copy).pack()
root.mainloop()
