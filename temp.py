from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

def selected(event):
    # получаем выделенный элемент
    selection = workers_combobox.get()
    print(selection)
    label["text"] = f"вы выбрали: {selection}"
    languages = ["Python", "C#", "Java", "JavaScriptwrffefeef"]
    workers_combobox["values"] = languages

workers_list = ["Python", "C#", "Java", "JavaScript"]
label = ttk.Label()
label.pack(anchor=NW, fill=X, padx=5, pady=5)

workers_combobox = ttk.Combobox(values=workers_list, state="readonly")
workers_combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
workers_combobox.bind("<<ComboboxSelected>>", selected)

root.mainloop()