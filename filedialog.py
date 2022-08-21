from email.mime import image
import tkinter
from PIL import ImageTk,Image
from tkinter import filedialog

root = tkinter.Tk()
root.title('画像表示')

def open():
    global img
    root.filename = filedialog.askopenfilename(initialdir='./images', title='ファイルを選択', filetypes=(('PNGファイル','*.png'),('JPGファイル','*.jpg'),('全てのファイル','*.*')))
    img = ImageTk.PhotoImage(Image.open(root.filename))
    lbl1['text'] = root.filename
    lbl1.update()
    lbl2['image'] = img
    lbl2.update()

btn = tkinter.Button(root, text='ファイルを開く', command=open)
btn.pack()
lbl1 = tkinter.Label(root)
lbl1.pack()
lbl2 = tkinter.Label(root)
lbl2.pack()

root.mainloop()