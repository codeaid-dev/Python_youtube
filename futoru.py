import tkinter

items = ['甘いものが好き','ケーキは1日10個以上食べれる','紅茶やコーヒーに砂糖を入れて飲む','運動が嫌い','毎日間食をしている']
vars = []

root = tkinter.Tk()
root.title('チェックボックス')
root.geometry('400x200')

def check():
    cnt = 0
    for var in vars:
        if var.get() == True:
            cnt += 1
    rate = int(100*cnt/len(items))
    result['text'] = f'あなたが将来太る確率は{rate}%です'
    result.update()

checks = tkinter.Label(root)
checks.pack()
for i in range(len(items)):
    var = tkinter.BooleanVar()
    var.set(False)
    vars.append(var)
    c = tkinter.Checkbutton(checks, text=items[i], variable=var)
    c.pack(anchor=tkinter.W)

print(vars)
result = tkinter.Label(root, text='結果表示', font=('Helvetica', 23), fg='yellow')
result.pack()
btn = tkinter.Button(root, text='表示', command=check)
btn.pack()

root.mainloop()