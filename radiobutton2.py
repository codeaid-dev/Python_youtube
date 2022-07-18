import tkinter

items = {'りんご': 1, 'パイナップル': 2}
colors = {'赤':'red', '青':'blue', '緑':'green'}

root = tkinter.Tk()
root.title('ラジオボタン')
root.geometry('400x200')

def select():
    v = var.get()
    for item in items:
        if v == items[item]:
            result['text'] = item
    v2 = var2.get()
    for color in colors:
        if v2 == colors[color]:
            result['bg'] = colors[color]
    result.update()

item_label = tkinter.Label(root)
item_label.pack()
var = tkinter.IntVar()
var.set(items['りんご'])
for item in items:
    r = tkinter.Radiobutton(item_label, text=item, variable=var, value=items[item])
    r.pack(side=tkinter.LEFT)

color_label = tkinter.Label(root)
color_label.pack()
var2 = tkinter.StringVar()
var2.set(colors['赤'])
for color in colors:
    r = tkinter.Radiobutton(color_label, text=color, variable=var2, value=colors[color])
    r.pack(side=tkinter.LEFT)

result = tkinter.Label(root, text='結果表示', font=('Helvetica', 23), fg='yellow')
result.pack()
btn = tkinter.Button(root, text='表示', command=select)
btn.pack()

root.mainloop()