from tkinter import Tk, Frame, Button, Text

window = Tk()

window.title("Frame GUI")

window.geometry("500x500")

menu_frame = Frame(window, background="red", padx=10, pady=4, width=2000, height=20)

content_frame = Frame(window, background="blue", padx=10, pady=4)

menu_frame.place(x=0, y=0)

content_frame.place(x=0, y=50)



file_button = Button(menu_frame, text="File")
file_button.grid(row=0, column=0)

edit_button = Button(menu_frame, text="Edit")
edit_button.grid(row=0, column=1)

select_button = Button(menu_frame, text="Select")
select_button.grid(row=0, column=2)

view_button = Button(menu_frame, text="View")
view_button.grid(row=0, column=3)


message = Text(content_frame, width=100)
message.pack()

def create_window(index):
    window = Tk()
    window.title("Child GUI" + str(index))
    window.geometry("500x500")
    window.mainloop()


Button(content_frame, text="Close Menu", command=menu_frame.destroy).pack()

Button(content_frame, text="Create Window", command=lambda: create_window(1)).pack()
Button(content_frame, text="Create Window", command=lambda: create_window(2)).pack()
Button(content_frame, text="Create Window", command=lambda: create_window(3)).pack()
Button(content_frame, text="Create Window", command=lambda: create_window(4)).pack()

Button(content_frame, text="Close Window", command=window.destroy).pack()

window.mainloop()