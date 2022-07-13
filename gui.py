import tkinter

root = tkinter.Tk()
root.geometry('400x200')
hello = tkinter.Label(root, text='こんにちは', background='red', font=('メイリオ',32))
evening = tkinter.Label(root, text='こんばんは', background='blue', font=('メイリオ',32))
#hello.pack(side=tkinter.LEFT)
#evening.pack(side=tkinter.LEFT)
#hello.grid(row=0, column=0)
#evening.grid(row=1, column=1)
hello.place(x=100, y=50)
evening.place(x=100, y=150)

root.mainloop()