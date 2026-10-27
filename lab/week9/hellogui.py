from tkinter import*

window = tk.Tk()
window.title("Hello 김기범")
window.geometry("400x200")

label = tk.Label(window, text="Hello, tkinter!")
label.pack()

window.mainloop()