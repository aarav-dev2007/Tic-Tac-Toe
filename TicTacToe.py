import tkinter as tk
import random
mode =None

turn='X'
win=[[0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]]

def computer():
            
            for i in win:
                  a,b,c=i
                  values = [buttons[a]['text'], buttons[b]['text'], buttons[c]['text']]

                  if values.count('X')==2 and values.count('Click') ==1:
                        if buttons[a]['text']=='Click':
                              buttons[a].config(text='O')
                        elif buttons[b]['text']=='Click':
                              buttons[b].config(text='O')
                        else:
                              buttons[c].config(text='O')
                        break
            else:
                empty=[]
                for j in buttons:
                    if j['text'] == 'Click':
                        empty.append(j)
                if empty:
                    ch=random.choice(empty)
                    ch.config(text='O')
            for i in win:
                        if buttons[i[0]]['text'] == buttons[i[1]]['text'] == buttons[i[2]]['text'] != 'Click':
                            label.config(text=buttons[i[0]]['text']+' Wins!')
                            for b in buttons:
                                b.config(state='disabled')
                            return

            if all(b['text']!= 'Click' for b in buttons):
                        label.config(text="It's a Draw!")
                        for b in buttons:
                              b.config(state='disabled')


def restart():
            global mode
            mode=None
            global turn
            turn='X'

            btn1.config(state='normal')
            btn2.config(state='normal')


            for b in buttons:
                b.config(text='Click', state='normal')

            label.config(text='Game Started')

def clicker(btn):
            global turn

            if mode is None:
                  label.config(text='Choose a mode first!')
                  return
            if btn['text'] != 'Click':
                return
            if mode=='computer':
                  btn.config(text='X')
            else:
                btn.config(text=turn)
            for i in win:
                if buttons[i[0]]['text'] == buttons[i[1]]['text'] == buttons[i[2]]['text'] != 'Click':
                    label.config(text=buttons[i[0]]['text']+' Wins!')
                    for b in buttons:
                        b.config(state='disabled')
                    return
                
            if all(b['text']!='Click' for b in buttons):
                label.config(text="It's a Draw!")

                for b in buttons:
                    b.config(state='disabled')
                return
            
            if mode=='computer':
                  computer()
            else:
                if turn == 'X':
                    turn = 'O'
                else:
                    turn='X'

a=tk.Tk()

def pvp():
      btn1.config(state='disabled')
      btn2.config(state='disabled')
      global mode
      mode='pvp'
      label.config(text='Player vs Player')

def vscomputer():
      btn1.config(state='disabled')
      btn2.config(state='disabled')
      global mode
      mode='computer'
      label.config(text='Vs Computer')

btn1 = tk.Button(a, text='PvP', command=pvp)
btn1.grid(row=5,column=0)
btn2= tk.Button(a, text='VS Computer', command=vscomputer)
btn2.grid(row=5,column=2)

label=tk.Label(a, text='Game Started', font=('Arial',16))
label.grid(row=3,column=0,columnspan=3)

restart_btn=tk.Button(a, text='Restart', command=restart)
restart_btn.grid(row=4,column=0,columnspan=3)

buttons=[]
for row in range(3):
            for column in range(3):
                btn_variable=tk.Button(a, text='Click', width=20, height=6)
                btn_variable.config(command= lambda b=btn_variable: clicker(b))
                btn_variable.grid(row=row, column=column)
                buttons.append(btn_variable)

a.mainloop()