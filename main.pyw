from tkinter import *
from pyttsx3 import init
from random import choice
from tkinter import messagebox

# Variables and constants
extr_numbers = []
engine = init()
bg = '#bde0fe' # Background color
fg = '#000000' # Foreground color
active_bg = '#e9c46a' # Active background color
max_numbers = 90
big_number_seconds = 1850

# Window configuration
root = Tk()
root.title('')
root.state('zoomed')
root.resizable(False, False)
root.configure(background=bg)
# Icon : "https://www.flaticon.com/free-icons/bingo" Bingo icons created by Freepik - Flaticon
p = PhotoImage(file='bingo.png')
root.iconphoto(False, p)
# Row and Col configuration
root.columnconfigure(0, weight=0)
root.rowconfigure(0, weight=0)

for x in range(1, 21):
    root.columnconfigure(x, weight=1)
    root.rowconfigure(x, weight=1)

# Functions
def check_options(btn, cmd):
    """Toggle options for buttons."""
    
    if btn['text'] == '| X |' and cmd == 'r':
        btn['text'] = '|✓|'
    elif btn['text'] == '| X |' and cmd == 'd':
        btn['text'] = '|✓|'
    elif btn['text'] == '|✓|' and cmd == 'r':
        btn['text'] = '| X |'
    elif btn['text'] == '|✓|' and cmd == 'd':
        btn['text'] = '| X |'

def draw():
    """Draw a Bingo number."""
    
    # Check if the table is full
    if len(extr_numbers) == max_numbers:
        messagebox.showinfo(title='Error', message='Table is full')
    # Extract the number
    else:
        n = choice(range(1, (max_numbers + 1)))
        while n in extr_numbers:
            n = choice(range(1, (max_numbers + 1)))
        
        extr_numbers.append(n)
        
        # Read the number (?)
        if read_btn['text'] == '|✓|':
            engine.say(n)
            engine.runAndWait()
        # Big number (?)
        if display_btn['text'] == '|✓|':
            number_window = Toplevel(root)
            number_window.title('Number:')
            number_window.state('zoomed')
            number_window.resizable(False, False)
            number_window.attributes('-topmost', 1)
            number_window.configure(background=bg)
            p = PhotoImage(file='bingo.png')
            number_window.iconphoto(False, p)

            dis_num = Label(number_window, text=f"{n}", bg=bg, fg='#ffbe0b', font=('Segoe UI Black', 104, 'bold'))
            dis_num.config(anchor=CENTER)
            dis_num.place(relx=0.5, rely=0.5, anchor=CENTER)
            number_window.after(big_number_seconds, lambda: number_window.destroy())
        
        # Set the background as active
        for j in range(1, (max_numbers + 1)):
            number = globals()['box' + str(j)]['text']
            if number == ('| ' + str(n) + ' |'):
                globals()['box' + str(j)]['background'] = active_bg

def reset_table():
    """Reset the Bingo table."""
    
    for j in range(1, (max_numbers + 1)):
        globals()['box' + str(j)]['background'] = bg
    extr_numbers.clear()

# Grid setup
x = 1
y = 1
for i in range(1, (max_numbers + 1)):
    globals()['box' + str(i)] = Label(root, text=f'| {i} |', bg=bg, fg=fg, font=('Segoe UI Black', 20, 'bold'))
    globals()['box' + str(i)].grid(row=y, column=x, pady=3, padx=3)
    if x == 10:
        x = 0
        y += 1
    x += 1

# Window buttons and widgets
ext_btn = Button(root, text='Draw', width=5, height=0, state=NORMAL, bg='#52b788', borderwidth=5,
                 font=('Helvetica', 15, 'bold'), command=draw)
ext_btn.grid(row=5, column=13, pady=0, padx=0)

res_btn = Button(root, text='Reset', width=5, height=0, state=NORMAL, bg='#e63946', borderwidth=5,
                 font=('Helvetica', 15, 'bold'), command=reset_table)
res_btn.grid(row=7, column=13, pady=0, padx=0)

read_lbl = Label(root, text='Read:', bg=bg, fg=fg, font=('Segoe UI', 11))
read_lbl.grid(row=1, column=18, pady=0, padx=0)
read_btn = Button(root, text='| X |', width=0, height=0, font=('Segoe UI', 9),
                  command=lambda: check_options(read_btn, 'r'))
read_btn.grid(row=1, column=19, pady=0, padx=0)

display_lbl = Label(root, text='Big Number:', bg=bg, fg=fg, font=('Segoe UI', 11))
display_lbl.grid(row=2, column=18, pady=0, padx=0)
display_btn = Button(root, text='| X |', width=0, height=0, font=('Segoe UI', 9),
                    command=lambda: check_options(display_btn, 'd'))
display_btn.grid(row=2, column=19, pady=0, padx=0)

root.mainloop()