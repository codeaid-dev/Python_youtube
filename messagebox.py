import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title('メッセージボックス')
root.geometry('400x200')

def popup():
    a = messagebox.showinfo('メッセージ', 'Hello World!')
    print(a)

tkinter.Button(root, text='表示', command=popup).pack()

root.mainloop()