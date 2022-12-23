import tkinter
import random

def uranau():
    result = random.randint(1,10)
    if 1 <= result <=2:
        ml2['text'] = '大吉'
        ml2['font'] = ('ヒラギノ明朝 ProN', 50)
        ml2['fg'] = 'red'
    elif 3 <= result <= 5:
        ml2['text'] = '吉'
        ml2['font'] = ('メイリオ', 32)
        ml2['fg'] = 'white'
    elif 6 <= result <= 8:
        ml2['text'] = '凶'
        ml2['font'] = ('メイリオ', 32)
        ml2['fg'] = 'white'
    else:
        ml2['text'] = '大凶'
        ml2['font'] = ('メイリオ', 32)
        ml2['fg'] = 'white'
    ml2.update()

root = tkinter.Tk()
root.geometry('600x400')
ml = tkinter.Label(root, text='下のボタンを押して占ってください', font=('メイリオ', '32'))
button = tkinter.Button(root, text='占う', font=('メイリオ', '32'), command=uranau)
ml2 = tkinter.Label(root, text='占いの結果', font=('メイリオ', '32'))
ml.pack(pady=10)
button.pack(pady=10)
ml2.pack(pady=10)

root.mainloop()