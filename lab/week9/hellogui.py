from tkinter import*

window = Tk()
window.title("Hello 김기범")
window.geometry("400x200")

label = Label(window, text="Hello, tkinter!")
label.pack()

window.mainloop()