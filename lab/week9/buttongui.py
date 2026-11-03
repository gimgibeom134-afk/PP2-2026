from tkinter import *
window = Tk()

button = Button(window, text="클릭하세요!",
                bg="yellow", fg="orange", font=("궁서체", 30),
            width=100, height=2
)

button.pack()
window.mainloop()