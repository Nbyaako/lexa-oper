import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import cryptolib



app = tk.Tk()
app.title("hello guys")
def center_window(app):
    app.geometry("500x400")
    app.update_idletasks() 
    width = app.winfo_width()
    height = app.winfo_height()
    x = (app.winfo_screenwidth() // 2) - (width // 2)
    y = (app.winfo_screenheight() // 2) - (height // 2)
    app.geometry(f"{width}x{height}+{x}+{y}")
center_window(app)
app.resizable(False, False)

list_encode = ['XOR', 'AES', 'DES', 'RSA', 'Blowfish', 'Twofish', 'Serpent']


div1 = tk.Frame(app, background='#ff0000')
div2 = tk.Frame(div1, background='#0000ff')
div3 = tk.Frame(div1, background='#00ffff')
div4 = tk.Frame(div1, background='#ff00ff')
div5 = tk.Frame(div1, background='#ffff00')
div6 = tk.Frame(div2, background='#000000')
div7 = tk.Frame(div2, background='#ff6666')

def on_button_click():
    user_text = entry_comment.get()
    secret_key = entry_key.get()
    selected_value = combox.get()
    
    if user_text == 'Текст для шифрования':
        user_text = ''
    if secret_key == 'Секретный ключ':
        secret_key = ''
    
    if not user_text or not secret_key or not selected_value:
        messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
        return
    
    try:
        result = cryptolib.encrypt(selected_value, user_text, secret_key)
        entry_end.config(state='normal')
        entry_end.delete(0, tk.END)
        entry_end.insert(0, result)
        entry_end.config(state='readonly')
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

def on_button_decrypt():
    encrypted_text = entry_comment.get()
    secret_key = entry_key.get()
    selected_value = combox.get()
    
    if encrypted_text == 'Текст для шифрования':
        encrypted_text = ''
    if secret_key == 'Секретный ключ':
        secret_key = ''
    
    if not encrypted_text or not secret_key or not selected_value:
        messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
        return
    
    try:
        result = cryptolib.decrypt(selected_value, encrypted_text, secret_key)
        entry_end.config(state='normal')
        entry_end.delete(0, tk.END)
        entry_end.insert(0, result)
        entry_end.config(state='readonly')
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

btn = tk.Button(div4, text="зашифровать", command=on_button_click)
btn_decrypt = tk.Button(div4, text="дешифровать", command=on_button_decrypt)
combox = ttk.Combobox(div5, values=list_encode, height=4)
entry_comment = tk.Entry(div6, width=20, fg="#313131")
entry_key = tk.Entry(div7, width=20, fg="#313131")
entry_end = tk.Entry(div3, width=20)

def on_entry_click(event):
    if entry_comment.get() == 'Текст для шифрования':
        entry_comment.delete(0, tk.END)
        entry_comment.config(fg='black')
def on_entry_click_key(event):
    if entry_key.get() == 'Секретный ключ':
        entry_key.delete(0, tk.END)
        entry_key.config(fg='black')
def on_focus_out(event):
    if entry_comment.get() == '':
        entry_comment.insert(0, 'Текст для шифрования')
        entry_comment.config(fg='#313131')
def on_focus_out_key(event):
    if entry_key.get() == '':
        entry_key.insert(0, 'Секретный ключ')
        entry_key.config(fg='#313131')

def nastroiki():
    combox.current(0)
    entry_comment.insert(0, "Текст для шифрования")
    entry_key.insert(1, "Секретный ключ")
    entry_end.insert(1, "Результат")
    entry_end.config(state='readonly')
    combox.config(state='readonly')
nastroiki()

def otrisovka():
    div1.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)
    div2.pack(fill=tk.BOTH, expand=1, padx=5, pady=5,side=tk.LEFT)
    div3.pack(fill=tk.BOTH, expand=1, padx=5, pady=5,side=tk.RIGHT)
    div4.pack(fill=tk.BOTH, expand=1, padx=5, pady=5,side=tk.TOP)
    div5.pack(fill=tk.BOTH, expand=1, padx=5, pady=5,side=tk.BOTTOM)
    div6.pack(fill=tk.BOTH, expand=1, padx=5, pady=5,side=tk.TOP)
    div7.pack(fill=tk.BOTH, expand=1, padx=5, pady=5,side=tk.BOTTOM)
    btn.pack(side=tk.BOTTOM, pady=20)
    btn_decrypt.pack(side=tk.BOTTOM, pady=5)
    combox.pack(side=tk.TOP, ipady=5)
    entry_comment.pack(side=tk.BOTTOM, pady=5, ipadx=10)
    entry_key.pack(side=tk.TOP, pady=5, ipadx=10)
    entry_end.pack(side=tk.LEFT, pady=5, padx=5, ipadx=10)
otrisovka()

def bind():
    entry_comment.bind('<FocusIn>', on_entry_click)
    entry_comment.bind('<FocusOut>', on_focus_out)
    entry_key.bind('<FocusIn>', on_entry_click_key)
    entry_key.bind('<FocusOut>', on_focus_out_key)
bind()




app.mainloop()