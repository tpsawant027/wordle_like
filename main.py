import random
import tkinter as tk

import requests
from bs4 import BeautifulSoup

import word_list

word_list_local = word_list.word_list


def get_def(word_link):
    l = []
    doc = BeautifulSoup(requests.get(word_link).text, "html.parser")
    div_def = doc.find(class_='def-group').find_all('div')
    for div in div_def:
        l.append(div.text.strip())
    return l


def get_word():
    ch = random.choice(word_list_local)
    word, lnk = ch['word'], ch['link']
    return (word, lnk)


w, lnk = get_word()
def_list = get_def(lnk)


def check():
    if len(inp.get()) != 5:
        lbl_ans['text'], lbl_ans['fg'] = "Enter a five letter word", 'red'
        return 
    elif lbl['text'] == 'win' or lbl['text'] == 'lost':
        return
    elif lbl['text'] == 0:
        lbl_ans['text'], lbl_ans['fg'] = f"The answer was: {w.upper()}", 'red'
        for ele in def_list:
            lbl_def['text']+=(ele + '\n')
        lbl['text'] = 'lost'
    elif 0 < lbl['text'] <= 6:
        lbl_ans['text'] = ""
        el = [e1, e2, e3, e4, e5]
        guess = inp.get()
        lbl_words['text']+=(guess.upper() + ' ')
        for i in range(5):
            if guess[i] == w[i]:
                el[i]['text'], el[i]['bg'], el[i]['fg'] = guess[i].upper(), 'green', 'white'
            elif guess[i] in w:
                el[i]['text'], el[i]['bg'], el[i]['fg'] = guess[i].upper(), 'yellow', 'green'
            else:
                el[i]['text'], el[i]['bg'], el[i]['fg'] = guess[i].upper(), 'red', 'white'
        if guess == w:
            lbl_ans['text'], lbl_ans['fg'] = 'You Won!!!', 'green'
            lbl['text'] = 'win'
            return
        lbl['text']-=1


if __name__ == '__main__':


    window = tk.Tk()
    window.title('wordle-like')
    window.resizable(width=False, height=False)
    lbl = tk.Label(master=window,text=6 ,justify='center')
    lbl.pack(padx=5, pady=5)


    frame = tk.Frame(master=window)
    frame.pack(padx=5, pady=5)


    e1 = tk.Label(master=frame,width=5)
    e1.grid(row=0, column=0, padx=5, pady=5)
    e2 = tk.Label(master=frame, width=5)
    e2.grid(row=0, column=1, padx=5, pady=5)
    e3 = tk.Label(master=frame, width=5)
    e3.grid(row=0, column=2, padx=5, pady=5)
    e4 = tk.Label(master=frame, width=5)
    e4.grid(row=0, column=3, padx=5, pady=5)
    e5 = tk.Label(master=frame, width=5)
    e5.grid(row=0, column=4, padx=5, pady=5)

    
    frame2 = tk.Frame(master=window)
    frame2.pack(padx=5, pady=5)
    inp = tk.Entry(master=frame2)
    inp.grid(row=0, column=0, padx=5, pady=5)
    button = tk.Button(master=frame2, text='Submit', command=check)
    button.grid(row=0, column=1, padx=5, pady=5)


    lbl_words = tk.Label(master=window, text="WORDS: ", justify='center', relief=tk.SUNKEN)
    lbl_words.pack(padx=5, pady=5)

    lbl_ans = tk.Label(master=window, text="", justify='center')
    lbl_ans.pack(padx=5, pady=5)
    
    lbl_def = tk.Label(master=window, text="", justify='center')
    lbl_def.pack(padx=5, pady=5)


    window.mainloop()
