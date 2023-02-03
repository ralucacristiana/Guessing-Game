from tkinter import *
import random

ws = Tk()
ws.title('Guessing Game')
ws.geometry('600x600')
ws.config(bg='#FFFFFF')

ranNum = random.randint(1, 64)
chance = 6
var = IntVar()
disp = StringVar()

def check_guess():
    global ranNum
    global chance
    usr_ip = var.get()
    if chance > 0:
        if usr_ip == ranNum:
            msg = f'Congratulations!'
        elif usr_ip > ranNum:
            chance -= 1
            msg = f'{usr_ip} is higher.'
        elif usr_ip < ranNum:
            chance -= 1
            msg = f'{usr_ip} is lower.'
        else:
            msg = f'Wrong input!'
    else:
        msg = f'You Lost!'

    disp.set(msg)

Label(
    ws,
    text='Guessing Game',
    font=('arial', 18),
    relief=GROOVE,
    padx=40,
    pady=40,
    bg='#209AF7'
).pack(pady=(40, 40))

Entry(
    ws,
    textvariable=var,
    font=('arial', 18)
).pack(pady=(40, 40))

Button(
    ws,
    text='Submit',
    font=('arial', 18),
    command=check_guess
).pack()

Label(
    ws,
    textvariable=disp,
    bg='#FFFFFF',
    font=('arial', 18)
).pack(pady=(40,40))

ws.mainloop()