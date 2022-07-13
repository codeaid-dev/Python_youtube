import tkinter

root = tkinter.Tk()
root.title('チェックボックス')
root.geometry('400x200')

def check():
    if var.get() == True:
        result['text'] = 'チェックしています'
    else:
        result['text'] = 'チェックしていません'
    result.update()

var = tkinter.BooleanVar()
var.set(True)

c = tkinter.Checkbutton(root, text='チェックボックス', variable=var)
c.pack()
result = tkinter.Label(root, text='結果表示')
result.pack()
btn = tkinter.Button(root, text='表示', command=check)
btn.pack()

root.mainloop()