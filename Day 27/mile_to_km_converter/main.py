from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text = "New Text")

# Button

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

input = Entry()
input.pack()

window.mainloop()


