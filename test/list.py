import tkinter as tk

def change_color(e):
    color = lbox.curselection()[0]
    lbl.config(background=task[color])


app = tk.Tk()
app.title("hello guys")
app.geometry("800x600")


task = ['dark cyan', 'green', 'blue', 'red', 'yellow', 'black', 'white']
items = tk.Variable(value=task)

fr = tk.Frame(app)
lbox = tk.Listbox(fr, listvariable=items, height=5, selectmode='single')
scroll = tk.Scrollbar(fr, command=lbox.yview)
lbox.config(yscrollcommand=scroll.set)
lbl = tk.Label(app, text='spisok zadach')

fr.pack()
lbox.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
lbl.pack()

lbox.bind('<<ListboxSelect>>', change_color)

app.mainloop()