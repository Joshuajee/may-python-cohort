from tkinter import Button, Tk, StringVar, Label, Entry

root = Tk()

root.title("Login GUI")

root.geometry("500x500")


username_var = StringVar(root)
password_var = StringVar(root)

result = StringVar(root)

def login():
    username = username_var.get()
    password = password_var.get()
    print(username)
    print(password)
    if (password == "12345678"):
        result.set("Password is correct")
    else:
        result.set("Password is incorrect")
        
def login(username, password):
    print(username)
    print(password)
    if (password == "12345678"):
        result.set("Password is correct")
    else:
        result.set("Password is incorrect")
        
      
     
username_label = Label(root, text="Username *", anchor="e")    
password_label = Label(root, text="Password *")  

username = Entry(root, textvariable=username_var)
password = Entry(root, textvariable=password_var)

username.delete(0, len(username.get())- 1)


click_btn = Button(
    root, text="Click Me!",  bg="blue", activebackground="red", foreground="white", width=12, height=1, command=login)


click_btn_2 = Button(
    root, text="Click Me!",  bg="blue", activebackground="red", foreground="white", width=12, height=1, command=lambda: login(username.get(), password.get()))


username_label.grid(row=0, column=0)
username.grid(row=0, column=1)

password_label.grid(row=1, column=0)
password.grid(row=1, column=1)
click_btn.grid(row=2, column=1, columnspan=2)
click_btn_2.grid(row=3, column=1, columnspan=2)

Label(root, textvariable=result).grid(row=4, column=0, columnspan=4)

root.mainloop()