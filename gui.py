import tkinter
from tkinter import *
from tkinter import ttk
from project import excel_read,validation, excel_write, make_text, timer_control
import datetime

is_reset = False
minute = 1
secondss = 0
key_strokes = []

def start():
    global is_reset
    is_reset = False
    set_start_position()
    time = validation(timer_set.get())
    if time !=ValueError:
        count_down(time)
        txt_field['state'] = 'normal'
        txt_field.delete('1.0', 'end')
        txt_field.insert(1.0, make_text(time)[0], 'left')
        txt_field['state'] = 'disabled'
        if time >0:
            button_start['state'] = 'disabled'
            button_set_time['state'] = 'disabled'
            timer_set['state'] = 'disabled'

def reset():
    global is_reset
    is_reset= True
    set_start_position()
    button_active()
    type_text_entry['state'] = 'disabled'

def set_time():
    set_start_position()
    type_text_entry['state'] = 'disabled'

root = Tk()
root.title('Typing speed test')

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

s = ttk.Style()
s.configure('Danger.TFrame', background='#A79277')

s1 = ttk.Style()
s1.configure('Marcin.TLabel', font=('Calibri', 14), background ='#A79277' )

s2 = ttk.Style()
s2.configure('button_set_time.TButton', font=('Calibri', 14), background = '#A79277')

s3 =ttk.Style()
s3.configure('Custom.Vertical.TScrollbar', troughcolor = '#A79277')

s4 = ttk.Style()
s4.configure('TEntry', background ='#D1BB9E')

mainframe = ttk.Frame(root, padding=(5, 5, 5, 5),
                      width=500,
                      height=500,
                      borderwidth=10,
                      relief='solid',
                      style='Danger.TFrame')
mainframe.grid(column=0, row=0, sticky='N, W, E, S')
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

frame_stats = ttk.Frame(mainframe, padding=(5, 5, 5, 5),
                      borderwidth=10,
                      relief='solid',
                      style='Danger.TFrame')
frame_stats.grid(column=0, row=12,columnspan=3, sticky='N, W, E, S')
frame_stats.columnconfigure(0, weight=1)
frame_stats.rowconfigure(0, weight=1)

timer_state = StringVar()
timer_state.set('01:00')

info_text = StringVar()
info_text.set('Good luck')


button_start = ttk.Button(mainframe, text='Start', command=start, style='button_set_time.TButton')
button_start.grid(row=7, column=0, sticky='W,E')

button_reset = ttk.Button(mainframe,text= 'Reset', command=reset, style='button_set_time.TButton')
button_reset.grid(row=7,column=1, columnspan=2, sticky='W,E')

ttk.Label(frame_stats,text='Category', style='Marcin.TLabel',relief='ridge', anchor='center',padding=(20,5,20,5)).grid(row=0,column=0, sticky='W,E')
ttk.Label(frame_stats,text='Time', style='Marcin.TLabel',relief='ridge',anchor='center', padding=(20,5,20,5)).grid(row=0,column=1, sticky='W,E')
ttk.Label(frame_stats,text='Current', style='Marcin.TLabel',relief='ridge',anchor='center',padding=(20,5,20,5)).grid(row=0,column=2, sticky='W,E')
ttk.Label(frame_stats,text='Best', style='Marcin.TLabel',relief='ridge',anchor='center',padding=(20,5,20,5)).grid(row=0,column=3, sticky='W,E')
ttk.Label(frame_stats,text='User', style='Marcin.TLabel',relief='ridge',anchor='center',padding=(20,5,20,5)).grid(row=0,column=4, sticky='W,E')
ttk.Label(frame_stats,text='Date', style='Marcin.TLabel',relief='ridge', anchor='center',padding=(20,5,20,5)).grid(row=0,column=5, sticky='W,E')

ttk.Label(frame_stats, text='Correct words', style='Marcin.TLabel', relief='ridge',padding=(20,5,20,5)).grid(row=1, column=0, sticky='W,E')
word_time = ttk.Label(frame_stats,text='60 sec', style='Marcin.TLabel', relief='ridge', anchor='center',padding=(20,5,20,5))
word_time.grid(row=1,column=1, sticky='W,E')
word_current = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
word_current.grid(row=1, column=2, sticky='W,E')
word_best = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
word_best.grid(row=1, column=3, sticky='W,E')
word_best_user = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
word_best_user.grid(row=1, column=4, sticky='W,E')
word_best_date = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
word_best_date.grid(row=1, column=5, sticky='W,E')

ttk.Label(frame_stats, text='Correct chars', style='Marcin.TLabel', relief='ridge',padding=(20,5,20,5)).grid(row=2, column=0, sticky='W,E')
chars_time = ttk.Label(frame_stats,text='60 sec', style='Marcin.TLabel', relief='ridge', anchor='center',padding=(20,5,20,5))
chars_time.grid(row=2,column=1, sticky='W,E')
chars_current = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
chars_current.grid(row=2, column=2, sticky='W,E')
chars_best = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
chars_best.grid(row=2, column=3, sticky='W,E')
chars_best_user = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
chars_best_user.grid(row=2, column=4, sticky='W,E')
chars_best_date = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
chars_best_date.grid(row=2, column=5, sticky='W,E')

ttk.Label(frame_stats, text='Keystrokes', style='Marcin.TLabel', relief='ridge',padding=(20,5,20,5)).grid(row=3, column=0, sticky='W,E')
keystrokes_time = ttk.Label(frame_stats,text='60 sec', style='Marcin.TLabel', relief='ridge', anchor='center',padding=(20,5,20,5))
keystrokes_time.grid(row=3,column=1, sticky='W,E')
keystrokes_current = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
keystrokes_current.grid(row=3, column=2, sticky='W,E')
keystrokes_best = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
keystrokes_best.grid(row=3, column=3, sticky='W,E')
keystrokes_best_user = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
keystrokes_best_user.grid(row=3, column=4, sticky='W,E')
keystrokes_best_date = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
keystrokes_best_date.grid(row=3, column=5, sticky='W,E')

ttk.Label(frame_stats, text='Accuracy %', style='Marcin.TLabel', relief='ridge',padding=(20,5,20,5)).grid(row=4, column=0, sticky='W,E')
accuracy_time = ttk.Label(frame_stats,text='60 sec', style='Marcin.TLabel', relief='ridge', anchor='center',padding=(20,5,20,5))
accuracy_time.grid(row=4,column=1, sticky='W,E')
accuracy_current = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
accuracy_current.grid(row=4, column=2, sticky='W,E')
accuracy_best = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
accuracy_best.grid(row=4, column=3, sticky='W,E')
accuracy_best_user = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
accuracy_best_user.grid(row=4, column=4, sticky='W,E')
accuracy_best_date = ttk.Label(frame_stats, text='0', style='Marcin.TLabel', anchor='center', relief='ridge',padding=(20,5,20,5))
accuracy_best_date.grid(row=4, column=5, sticky='W,E')
def change_color(event):
    global cursor_pos
    key_strokes.append(event.char)
    string_typed = type_text_entry.get()
    length = int(txt_field.index('end-1c').split('.')[1])
    for n in range(1,10000):
        if len(string_typed)<150:
            txt_field.yview_moveto(0.0)
        if (n+1)*150> len(string_typed) > n*150:
            txt_field.yview_moveto(130*n/length)

    for n in range(len(string_typed)):
        cursor_pos = f'1.{n}'
        if txt_field.get(1.0,'end')[n] == string_typed[n]:
            txt_field.tag_add('color_match', cursor_pos)
            txt_field.tag_config('color_match', foreground='white', background='#88AB8E')
        else:
            txt_field.tag_add('color_no_match', cursor_pos)
            txt_field.tag_config('color_no_match', foreground='#E72929', background='#FAF494')

def color_back(event):
    key_strokes.append(event.char)
    txt_field.tag_remove('color_match', cursor_pos, 'end')
    txt_field.tag_remove('color_no_match', cursor_pos, 'end')
    if len(type_text_entry.get()) ==0:
        txt_field.tag_remove('color_match', 1.0, 'end')
        txt_field.tag_remove('color_no_match', 1.0, 'end')

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

button_set_time = ttk.Button(mainframe, text='Set time', command=set_time, style='button_set_time.TButton')
button_set_time.grid(row=1, column=2, sticky='W,E', pady=0,padx=5)

ttk.Label(mainframe, style='Marcin.TLabel', text='Name', anchor='w').grid(row=0,column=0, sticky='W,E', pady=0, padx=(5,5))
user_set = ttk.Entry(mainframe, style='TEntry')
user_set.insert(0,'Your name')
user_set.configure(font=('Calibri', 14))
user_set.grid(row=1, column=0, sticky='W, E', pady=0, padx=5)
user_set.bind('<ButtonPress-1>', lambda a: user_set.delete(0, 'end'))

ttk.Label(mainframe, style='Marcin.TLabel', text='Time').grid(row=0,column=1, sticky='W,E', pady=0, padx=(0,5))
timer_set = ttk.Entry(mainframe, style="TEntry")
timer_set.insert(0, string='60')
timer_set.configure(font=('Calibri', 14))
timer_set.grid(row=1, column=1, sticky='W, E')
timer_set.bind('<ButtonPress-1>', lambda a: timer_set.delete(0, 'end'))

txt_field = Text(mainframe, font=('Calibri', 20),width=30, height=5, relief='flat', background='#EAD8C0')
txt_field.tag_configure('left', justify='left')
txt_field.tag_configure('center', justify='center')
txt_field.grid(row=5, column=0, columnspan=3, sticky='W,E', pady=(5,0), padx=(5,0))
txt_field.insert('1.0', 'You can set time (default = 60 sec).\nPress start to beat the record')
txt_field['state'] = 'disabled'

scroll = ttk.Scrollbar(mainframe, orient=VERTICAL, command=txt_field.yview, style='Custom.Vertical.TScrollbar')
scroll.grid(row=5, column=4, sticky='N,S', pady=(5,0), padx=(0,5))
txt_field.configure(yscrollcommand=scroll.set)

type_text_entry = ttk.Entry(mainframe, justify='center', font=('Calibri', 20), state='disabled', style='TEntry')
type_text_entry.grid(row=6, column=0, columnspan=3, pady=(0,20), padx=(5,0), sticky='W,E')

label_timer = ttk.Label(mainframe, textvariable=timer_state, style='Marcin.TLabel', anchor='center', font=('Verdana', 45, 'bold'), relief='ridge')
label_timer.grid(row=2, column=0, columnspan=3, sticky='W,E', padx=5, pady=(20,0))

label_info_text = ttk.Label(mainframe, textvariable=info_text, background='#88AB8E',
                            font=('Calibri', 25, 'bold'), anchor= 'center', relief='flat')
label_info_text.grid(row=3, column=0, columnspan=3, sticky='W,E', padx=5, pady=(0,20))

type_text_entry.bind('<KeyRelease>', change_color)
type_text_entry.bind('<BackSpace>', color_back)

def set_start_position():
    time = validation(timer_set.get())
    if time == ValueError:
        info_text.set('Try again')
        label_info_text.configure(background='#E72929')
        timer_state.set("Wrong time format")
    else:
        minute_text, second_text = timer_control(time)
        timer_state.set(f"{minute_text}:{second_text}")
        excel_read(time)
        info_text.set('Good luck')
        label_info_text.configure(background='#88AB8E')
        words_max,chars_max,keystrokes_max,accuracy_max= excel_read(time)
        word_time.configure(text=time)
        word_best.configure(text=words_max['word'])
        word_best_user.configure(text=f"{words_max['user']}")
        word_best_date.configure(text=f"{words_max['data'].strftime('%Y-%m-%d')}")
        chars_time.configure(text=time)
        chars_best.configure(text=chars_max['chars'])
        chars_best_user.configure(text=f"{chars_max['user']}")
        chars_best_date.configure(text=f"{chars_max['data'].strftime('%Y-%m-%d')}")
        keystrokes_time.configure(text=time)
        keystrokes_best.configure(text=keystrokes_max['keystrokes'])
        keystrokes_best_user.configure(text=f"{keystrokes_max['user']}")
        keystrokes_best_date.configure(text=f"{keystrokes_max['data'].strftime('%Y-%m-%d')}")
        accuracy_time.configure(text=time)
        accuracy_best.configure(text=accuracy_max['accuracy'])
        accuracy_best_user.configure(text=f"{accuracy_max['user']}")
        accuracy_best_date.configure(text=f"{accuracy_max['data'].strftime('%Y-%m-%d')}")
        info_text.set('Good luck')
        label_info_text.configure(background='#88AB8E')
        word_current.configure(text='0')
        chars_current.configure(text='0')
        keystrokes_current.configure(text='0')
        accuracy_current.configure(text='0')
        key_strokes.clear()
        txt_field.yview_moveto(0.0)
        txt_field.tag_remove('color_match', '1.0', tkinter.END)
        txt_field.tag_remove('color_no_match', '1.0', tkinter.END)
        type_text_entry['state'] = 'active'
        type_text_entry.delete(0, 'end')
        type_text_entry.focus()
        txt_field['state'] = 'normal'
        txt_field.delete('1.0', 'end')
        txt_field.insert('1.0', 'You can set time (default = 60 sec).\nPress start to beat the record.')
        txt_field['state'] = 'disabled'

def stats():
    l_text_typed = [n for n in type_text_entry.get()]
    l_text_inserted_txt_field =[z for z in txt_field.get(1.0,'end')]
    match = [l_text_typed[index]for index in range(len(l_text_typed)) if l_text_typed[index] == l_text_inserted_txt_field[index]  ]
    string_match = ''.join(match).strip(' ')
    list_string_match = string_match.split(' ')
    match_word = [word for word in list_string_match if word in txt_field.get(1.0, f'1.{len(type_text_entry.get())+1}').split(' ') ]
    sum_char = len(match)
    sum_word = len(match_word)
    sum_key_strokes = len(key_strokes)
    word_current.configure(text=sum_word)
    chars_current.configure(text=sum_char)
    keystrokes_current.configure(text=sum_key_strokes)
    try:
        accuracy = f"{(sum_char/ sum_key_strokes * 100):.2f}"
        if float(accuracy) > 100:
            accuracy = 100.00
    except ZeroDivisionError:
        accuracy = 0
    else:
        accuracy_current.configure(text=accuracy)
    return sum_word, sum_char, sum_key_strokes, float(accuracy)

def count_down(sec):
    value = sec
    minute_text, second_text =timer_control(value)
    timer_state.set(f"{minute_text}:{second_text}")
    if is_reset == False:
        if value > 0 :
            root.after(1000, count_down, value-1)
        if 10 <value <= round(int(validation(timer_set.get())) / 2):
            info_text.set('Less than half time')
            label_info_text.configure(background='#FAF494')
        if 0 < value <= 10:
            info_text.set('10 sec left')
            label_info_text.configure(background='#E72929')
        if value == 0:
            button_active()
            type_text_entry['state'] = 'disabled'
            label_info_text.configure(background='#E72929')
            info_text.set('Time over')
            words, chars, keystrokes, accuracy = stats()
            words_max, chars_max, keystrokes_max, accuracy_max = excel_read(validation(timer_set.get()))
            current_results = [validation(timer_set.get()),
                               words,
                               chars,
                               keystrokes,
                               accuracy,
                               datetime.date.today(),
                               user_set.get()]
            if words>words_max.iloc[1] or chars>chars_max.iloc[2] or keystrokes>keystrokes_max.iloc[3] or accuracy>accuracy_max.iloc[4]:
                excel_write(*current_results)

    else:
        set_time()
        info_text.set('Good luck')
        label_info_text.configure(background='#88AB8E')

def button_active():
    button_start['state'] = 'active'
    button_set_time['state'] = 'active'
    timer_set['state'] = 'active'




root.mainloop()