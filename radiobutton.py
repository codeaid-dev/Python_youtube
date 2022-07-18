import tkinter

root = tkinter.Tk()
root.title('ラジオボタン')
root.geometry('400x200')

def select():
    v = var.get()
    if v == 1:
        result['text'] = 'りんご'
    elif v == 2:
        result['text'] = 'パイナップル'
    result.update()

var = tkinter.IntVar()
var.set(1)
r1 = tkinter.Radiobutton(root, text='りんご', variable=var, value=1)
r1.pack()
r2 = tkinter.Radiobutton(root, text='パイナップル', variable=var, value=2)
r2.pack()

result = tkinter.Label(root, text='結果表示', font=('Helvetica', 23), fg='yellow')
result.pack()
btn = tkinter.Button(root, text='表示', command=select)
btn.pack()

root.mainloop()