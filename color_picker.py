import tkinter
from tkinter import colorchooser

root=tkinter.Tk()
root.title('Color Picker')
root.geometry('500x500')

def color():
    color = colorchooser.askcolor()
    tkinter.Label(root, text=f'R:{color[0][0]} G:{color[0][1]} B:{color[0][2]} {color[1]}',
                        font=('Helvetica',20)).pack()
    tkinter.Label(root, bg=color[1], width=50, height=2).pack(pady=5)

tkinter.Button(root, text='色選択', command=color).pack()

root.mainloop()