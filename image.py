import tkinter
from PIL import ImageTk, Image

root = tkinter.Tk()
root.title('画像表示')
root.iconbitmap('codeaid.ico')

img = ImageTk.PhotoImage(Image.open('test.jpg'))
c = tkinter.Canvas(root, width=600, height=400)
c_img = c.create_image(300,200,image=img)
c.pack()

root.mainloop()