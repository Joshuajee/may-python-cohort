from tkinter import Button as TKButton, Tk, StringVar, Label, Entry, Text
from tkinter.ttk import Button, Style

root = Tk()

style = Style()

style.configure('W.TButton', font = ('calibri', 10, 'bold', 'underline'), foreground = 'blue')


root.title("Testing GUI")

root.geometry("500x500")


username_var = StringVar(root)
password_var = StringVar(root)

result = StringVar(root)

def test():
    username = username_var.get()
    password = password_var.get()
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



click_btn = TKButton(
    root, text="Click Me!",  bg="blue", activebackground="red", foreground="white", width=12, height=1, command=test)

click_btn_2 = Button(
    root, text="Click Me 2", style="W.TButton")



username_label.grid(row=0, column=0)
username.grid(row=0, column=1)

password_label.grid(row=1, column=0)
password.grid(row=1, column=1)
click_btn.grid(row=2, column=1, columnspan=2)

Label(root, textvariable=result).grid(row=3, column=0, columnspan=4)

click_btn_2.grid(row=4, column=0)

text = Text(root, name="my-text")
text.grid(row=5, column=0, columnspan=12)

root.mainloop()