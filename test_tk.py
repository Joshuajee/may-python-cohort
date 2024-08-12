from tkinter import Button, Misc


class CustomButton(Button):
    
    def __init__(self, master: Misc | None = None, text="", command = ""):
        super().__init__(master, text=text, bg="blue", activebackground="red", foreground="white", width=12, height=1, command=command)