from tkinter import * # type: ignore
from tkinter import ttk
from guiFunctions import btn_press, close_program, reset_scores
from guiFunctions import comp_score, ties, human_score

#Creating the root window
root = Tk()
root.geometry('480x500')
root.configure(bg='#031927')
root.resizable(False,False)
root.iconbitmap('C:/Users/mail4/Desktop/Coding-Temple/Matrix-123/Week-2/WeekendProject/CT-Week-2-WeekendProject-Fork/hand-scissors-solid.ico')
root.title('Rock    Paper    Scissors    Spock    Lizard')


#The main Frame contains all the widgets and children frames
mainframe = Frame(root , bg='#031927')
mainframe.grid(column=0, row=0, sticky=(N,S)) # type: ignore
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


hero = ttk.Label(mainframe, text='Rock, Paper, Scissors, Spock, Lizard!', font=('Arial', 18,), justify= 'center', background='#031927', foreground='#f1e9db')

#The scores Frame contains the scores
scores = Frame(mainframe, bg='#031927')
############################################
player_score = ttk.Label(scores, text=f'Player\n\n{human_score}', font=('Arial', 15), justify= 'center', background='#031927', foreground='#f1e9db')
tie_score = ttk.Label(scores, text=f'Ties\n\n{ties}', font=('Arial', 15), justify= 'center', background='#031927', foreground='#f1e9db')
computer_score = ttk.Label(scores, text=f'Computer\n\n{comp_score}', font=('Arial', 15), justify= 'center', background='#031927', foreground='#f1e9db')
############################################

results = ttk.Label(mainframe, text='Pick your choice.\n\nTest your luck!', font=('Arial', 15), justify= 'center', background='#031927', foreground='#f1e9db')

#The button frame contains all the buttons
buttons = Frame(mainframe, bg='#031927')
############################################
rock_btn = Button(buttons, text='Rock',width=13,cursor= 'hand2', activebackground="#548e6c", font=('Arial', 13, 'bold'), background= '#325440', foreground='#f1e9db',
                        command=lambda
                        m="Rock",
                        a=results,
                        b=player_score,
                        c=tie_score,
                        d=computer_score: btn_press(m,a,b,c,d))
paper_btn = Button(buttons, text='Paper',width=13,cursor= 'hand2', activebackground="#548e6c", font=('Arial', 13, 'bold'), background= '#325440', foreground='#f1e9db', 
                        command=lambda
                        m="Paper",
                        a=results,
                        b=player_score,
                        c=tie_score,
                        d=computer_score: btn_press(m,a,b,c,d))
scissors_btn = Button(buttons, text='Scissors',width=13,cursor= 'hand2', activebackground="#548e6c", font=('Arial', 13, 'bold'), background= '#325440', foreground='#f1e9db',
                        command=lambda 
                        m="Scissors",
                        a=results,
                        b=player_score,
                        c=tie_score,
                        d=computer_score: btn_press(m,a,b,c,d))
spock_btn = Button(buttons, text='Spock',width=13,cursor= 'hand2', activebackground="#548e6c", font=('Arial', 13, 'bold'), background= '#325440', foreground='#f1e9db', 
                        command=lambda
                        m="Spock",
                        a=results,
                        b=player_score,
                        c=tie_score,
                        d=computer_score: btn_press(m,a,b,c,d))
lizard_btn = Button(buttons, text='Lizard',width=13,cursor= 'hand2', activebackground="#548e6c", font=('Arial', 13, 'bold'), background= '#325440', foreground='#f1e9db',
                        command=lambda
                        m="Lizard",
                        a=results,
                        b=player_score,
                        c=tie_score,
                        d=computer_score: btn_press(m,a,b,c,d))


reset_btn = Button(buttons, text='Reset Scores',cursor= 'hand2', activebackground="#548e6c",width=13, background= '#325440', font=('Arial', 13, 'bold'), foreground='#f1e9db',
                        command=lambda
                        a=player_score ,
                        b=tie_score,
                        c=computer_score : reset_scores(a,b,c))

close_btn = Button(buttons, text='Close',cursor= 'hand2', activebackground="#548e6c", font=('Arial', 13, 'bold'), background= '#325440',foreground='#f1e9db',width=13, command=close_program)
####################################################

# Hover Affects
def on_enter(event):
    event.widget.config(background='#548e6c')

def on_leave(event):
    event.widget.config(background= '#325440')
    
rock_btn.bind('<Enter>', on_enter)
rock_btn.bind('<Leave>', on_leave)

paper_btn.bind('<Enter>', on_enter)
paper_btn.bind('<Leave>', on_leave)

scissors_btn.bind('<Enter>', on_enter)
scissors_btn.bind('<Leave>', on_leave)

spock_btn.bind('<Enter>', on_enter)
spock_btn.bind('<Leave>', on_leave)

lizard_btn.bind('<Enter>', on_enter)
lizard_btn.bind('<Leave>', on_leave)

reset_btn.bind('<Enter>', on_enter)
reset_btn.bind('<Leave>', on_leave)

close_btn.bind('<Enter>', on_enter)
close_btn.bind('<Leave>', on_leave)


#This next section is placing all the widgets in the root window
hero.grid(row=0 ,column=0, pady=20, sticky='n')


scores.grid(row=1 ,column=0, pady=10)

player_score.grid(row=0 ,column=0, padx=20)
tie_score.grid(row=0 ,column=1, padx=40)
computer_score.grid(row=0 ,column=2, padx=20)


results.grid(row=2 ,column=0, pady=20)


buttons.grid(row=3 ,column=0,pady=5)

rock_btn.grid(row=0 ,column=0,padx=8,pady=10)
paper_btn.grid(row=0 ,column=1,padx=8,pady=10, rowspan=2)
scissors_btn.grid(row=0 ,column=2,padx=8,pady=10)
spock_btn.grid(row=1 ,column=0,padx=8,pady=10)
lizard_btn.grid(row=1 ,column=2,padx=8,pady=10)
close_btn.grid(row=2 ,column=1,padx=(30,0),pady=(40,0),columnspan=2)
reset_btn.grid(row=2 ,column=0,padx=(0,30),pady=(40,0),columnspan=2)


root.mainloop()