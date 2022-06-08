import tkinter

root = tkinter.Tk()
root.title('画像表示')

FONT = ('メイリオ',30)
MODES = [
    ('縮小', -1),
    ('オリジナル', 0),
    ('拡大', 1),
]
zoom = 0

img = tkinter.PhotoImage(file='images/Panda.png')
c = tkinter.Canvas(root, width=600, height=400)
c_img = c.create_image(300,200,image=img)
c.pack()
f = tkinter.Frame(root)
f.pack(pady=10)
v = tkinter.IntVar()
v.set(0)

for text,mode in MODES:
    r = tkinter.Radiobutton(f, text=text, value=mode, variable=v, font=FONT)
    r.pack(side=tkinter.LEFT, expand=True, padx=10)

def view():
    global c_img, img, zoom
    c.delete(c_img)
    if v.get() == -1 and zoom == 0:
        img = img.subsample(2)
        zoom = -1
    elif v.get() == -1 and zoom == 1:
        img = img.subsample(4)
        zoom = -1
    elif v.get() == 0 and zoom == -1:
        img = img.zoom(2)
        zoom = 0
    elif v.get() == 0 and zoom == 1:
        img = img.subsample(2)
        zoom = 0
    elif v.get() == 1 and zoom == -1:
        img = img.zoom(4)
        zoom = 1
    elif v.get() == 1 and zoom == 0:
        img = img.zoom(2)
        zoom = 1
    c_img = c.create_image(300,200,image=img)

b = tkinter.Button(root, text='変更', font=FONT, command=view)
b.pack(pady=10)

root.mainloop()