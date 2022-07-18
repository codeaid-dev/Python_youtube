import tkinter
from tkinter import colorchooser

root=tkinter.Tk()
root.title('Color Picker')
root.geometry('500x500')

def color():
    color, code = colorchooser.askcolor()
    print(color, code)
    tkinter.Label(root, text=f'R:{color[0]} G:{color[1]} B:{color[2]} {code}',
                        font=('Helvetica',20)).pack()
    tkinter.Label(root, bg=code, width=50, height=2).pack(pady=5)

tkinter.Button(root, text='色選択', command=color).pack()

root.mainloop()