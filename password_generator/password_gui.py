#!/usr/bin/env python3

import tkinter as tk
import password_tools

default_length = 16


def get_pw_options():
    length = length_entry.get()
    numbers = numbers_var.get()
    entered_specials = specials_entry.get()
    error_messages = ''
    
    is_valid, special_error_message, special_characters, required_specials = password_tools.validate_specials(entered_specials)

    if special_error_message:
        error_messages += special_error_message

    min_length = 4
    if special_characters != '' and required_specials == '':
        min_length += 2
    else:
        min_length += len(required_specials)
    if numbers:
        min_length += 2

    if length == '':
         length = default_length

    elif not length.isdigit():
        error_messages = 'Length must be a number\n' + error_messages
        return False, error_messages, None, None, None, None, None

    elif length.isdigit():
        length = int(length)




    return is_valid, error_messages, length, numbers, special_characters, required_specials, min_length

def generate_password(keypress=None):

    is_valid, error_messages, length, numbers, special_characters, required_specials, min_length = get_pw_options()

    if not is_valid:
        status_label.config(text=error_messages, foreground='red')
        generated_pw.config(text='')
        char_counts_label.config(text='')
        return
    
    if length < min_length:
        status_label.config(text=f'Password must be at least {min_length} with current options.\n', foreground='red')
        generated_pw.config(text='')
        return
    
    password = password_tools.generate_pw(length, numbers, special_characters, required_specials)

    generated_pw.config(text=password)
    status_label.config(text='Password generated!', foreground='blue')

    counts = password_tools.criteria_counts(password)
    counts_text = ''
    for char_type, count in counts.items():
        counts_text += f'{char_type}: {count}\n'

    char_counts_label.config(text=counts_text)









def copy_password(keypress=None):
    password = generated_pw.cget('text')  
    if password == '':
        status_label.config(text='No password to copy!', foreground='red')
        return
    window.clipboard_clear()
    window.clipboard_append(password)
    status_label.config(text='Password copied to clipboard!', foreground='blue')

def show_specials_help(event=None):
    status_label.config(text="Empty = all punctuation, none = no specials, or type allowed specials like !@#", foreground='gray')
def show_password_help(event=None):
    status_label.config(text="Generated password. Click Copy or press Ctrl+C.", foreground='gray')
def show_generate_help(event=None):
    status_label.config(text='Press "Enter" at any time to generate password. \n default fields produce a unique string with 2 of each character type.', foreground='gray')
def clear_status(event=None):
    status_label.config(text="")















window = tk.Tk()
window.title('Password Generator')
window.geometry('650x400')
window.bind('<Return>', func=generate_password)
window.bind('<Control-c>', copy_password)

title_label = tk.Label(window, text='Password Generator', font=('Arial', 18))
title_label.pack(pady=20)

form_frame = tk.Frame(window, background='gray')
form_frame.pack(fill='x')

form_frame2 = tk.Frame(form_frame, background='gray')
form_frame2.pack()

form_frame3 = tk.Frame(window)
form_frame3.pack()

# -----------------GRID 1-----------------------------------------
length_label = tk.Label(form_frame2, text='Length ', background='gray', foreground='white')
length_label.grid(row=0, column=0, sticky='e')
length_entry = tk.Entry(form_frame2, width=20)
length_entry.grid(row=0, column=1, pady=10)

specials_label = tk.Label(form_frame2, text='Special characters ', background='gray', foreground='white')
specials_label.grid(row=1, column=0, sticky='e')
specials_label.bind('<Enter>', show_specials_help)
specials_label.bind('<Leave>', clear_status)
specials_entry = tk.Entry(form_frame2, width=20)
specials_entry.grid(row=1, column=1)
specials_entry.bind('<Enter>', show_specials_help)
specials_entry.bind('<Leave>', clear_status)

numbers_var = tk.BooleanVar(value=True)
numbers_label = tk.Label(form_frame2, text='Use numbers ', background='gray', foreground='white')
numbers_label.grid(row=2, column=0, sticky='e')
numbers_check = tk.Checkbutton(form_frame2, variable=numbers_var, justify='left', background='gray', highlightbackground='gray')
numbers_check.grid(row=2, column=1, sticky='w', pady=10)

generate_button = tk.Button(form_frame2, text='Generate', command=generate_password,)
generate_button.grid(row=1, column=2, sticky='e', padx=10)
generate_button.bind('<Enter>', show_generate_help)
generate_button.bind('<Leave>', clear_status)
# ----------------------------------------------------------------
# -----------------GRID 2-----------------------------------------
password_label = tk.Label(form_frame3, text='Password: ')
password_label.grid(row=0, column=0, padx=10)
password_label.bind('<Enter>', show_password_help)
password_label.bind('<Leave>', clear_status)
generated_pw = tk.Label(form_frame3, text='', width=50, background='white', font=('Arial', 12))
generated_pw.grid(row=0, column=1, columnspan=3, sticky='e',pady=20)
generated_pw.bind('<Enter>', show_password_help)
generated_pw.bind('<Leave>', clear_status)

copy_button = tk.Button(form_frame3, text='Copy', command=copy_password)
copy_button.grid(row=0, column=4, padx=10)
# ----------------------------------------------------------------
status_label = tk.Label(window, text='')
status_label.pack()

char_counts_label = tk.Label(window, text='')
char_counts_label.pack(pady=10)

window.mainloop()
