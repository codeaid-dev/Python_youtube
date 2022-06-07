import tkinter
import random

FONT = ('メイリオ',30)
questions = [
    {'Q':'images/Finland.png','A':'フィンランド'},
    {'Q':'images/Greece.png','A':'ギリシャ'},
    {'Q':'images/Hungary.png','A':'ハンガリー'},
    {'Q':'images/Italy.png','A':'イタリア'},
    {'Q':'images/Monaco.png','A':'モナコ'},
    {'Q':'images/Poland.png','A':'ポーランド'},
    {'Q':'images/Sweden.png','A':'スウェーデン'},
]
correct = None

def question():
    global correct
    correct = random.randint(0,len(questions)-1)
    q_image['image'] = questions[correct]['img']
    q_image.update()
    result['text'] = '結果表示'
    result.update()

def judge():
    seikai = questions[correct]['A']
    if answer.get() == seikai:
        result['text'] = '正解'
    else:
        result['text'] = f'不正解（正解は{seikai}）'
    result.update()

root = tkinter.Tk()
root.title('クイズ')

for img in questions:
    img['img'] = tkinter.PhotoImage(file=img['Q'])

correct = random.randint(0,len(questions)-1)
q_image = tkinter.Label(root, image=questions[correct]['img'])
q_image.pack()
result = tkinter.Label(root, text='結果表示', font=FONT)
result.pack()
answer = tkinter.Entry(root, width=15, font=FONT)
answer.pack(pady=10)
ans_btn = tkinter.Button(root, text='解答', font=FONT, command=judge)
ans_btn.pack(pady=10)
next_btn = tkinter.Button(root, text='次の問題', font=FONT, command=question)
next_btn.pack(pady=10)

root.mainloop()