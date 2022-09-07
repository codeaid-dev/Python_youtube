import tkinter

root = tkinter.Tk()
root.title('プルダウンメニュー')
root.geometry('300x300')

options = ['Python','Java','C#','Ruby','PHP']

def show():
    label = tkinter.Label(root, text=selected.get())
    label.pack()

selected = tkinter.StringVar()
selected.set(options[0])

#dropdown = tkinter.OptionMenu(root, selected, 'Python','Java','C#','Ruby','PHP')
dropdown = tkinter.OptionMenu(root, selected, *options)
dropdown.pack()

btn = tkinter.Button(root, text='表示', command=show)
btn.pack()

root.mainloop()