"""GUI"""

# -*- coding: utf-8 -*-
import sys
import os
import tkinter as tk


def list_win_gui():
    win_list = tk.Toplevel(win)
    win_list.title("Ancet Loop")
    win_list.iconbitmap('sub--basics_of_programming/another/gui/cfg/icon.ico')
    win_list.geometry("350x400+400+150")
    win_list.resizable(False, False)

    frame3 = tk.Frame(win_list, width=350, height=400)
    btn_accept = tk.Button(frame3, text = "Принять ученика", font = ("Calibri", 12, "bold"),
                           bg='green', fg = 'white', command = donothing)
    btn_not_accept = tk.Button(frame3, text = "Не принимать", font = ("Calibri", 12, "bold"),
                           bg='red', fg = 'white', command = donothing)
    text_info = tk.Text(frame3)

    frame3.pack()
    btn_accept.place(x=190, y=360, height=30, width=150)
    btn_not_accept.place(x=10, y=360, height=30, width=150)
    text_info.place(x=10, y=10, height=340, width=330)



def donothing():
    print('Done')


def show_info_about_programm():
    tk.messagebox.showinfo("О программе", "Программа еще находится в разработке (70%)")


def openreadme(): 
    filename = 'sub--basics_of_programming/another/gui/cfg/guide.txt'
    os.system("start " + filename)


def quit_from_programm():
    sys.exit()


def open_change_win():
    if st_name == 0:
        tk.messagebox.showerror("Ошибка!", "Для изменения необходимо выбрать ученика")
    else:
        win_change = tk.Toplevel(win)
        win_change.title("INFO Change")
        win_change.iconbitmap('sub--basics_of_programming/another/gui/cfg/icon.ico')
        win_change.geometry("350x400+400+150")
        win_change.resizable(False,False)

        frame2 = tk.Frame(win_change, width=350, height=400)
        label2_1 = tk.Label(frame2, text = "Ученик", justify = 'left', font = ("Calibri", 14, "bold"))
        label2_2 = tk.Label(frame2, text = "Родитель", justify = 'left', font = ("Calibri", 14, "bold"))

        btnApply = tk.Button(frame2, text = "Применить изменения", font = ("Calibri", 12, "bold"), 
                      command = donothing)

        st_ent2_1 = tk.Entry(frame2, textvariable = 1)
        st_ent2_2 = tk.Entry(frame2, textvariable = 1)
        st_ent2_3 = tk.Entry(frame2, textvariable = 1)
        pr_ent2_1 = tk.Entry(frame2, textvariable = 1)
        pr_ent2_2 = tk.Entry(frame2, textvariable = 1)
        pr_ent2_3 = tk.Entry(frame2, textvariable = 1)

        frame2.pack()
        label2_1.place(x=10, y=0, height=25, width=100)
        st_ent2_1.place(x=10, y=30, height=20, width=330)
        st_ent2_2.place(x=10, y=55, height=20, width=330)
        st_ent2_3.place(x=10, y=80, height=20, width=330)
        label2_2.place(x=10, y=110, height=25, width=100)
        pr_ent2_1.place(x=10, y=140, height=20, width=330)
        pr_ent2_2.place(x=10, y=165, height=20, width=330)
        pr_ent2_3.place(x=10, y=190, height=20, width=330)
        btnApply.place(x=20, y=360, height=30, width=310)


# НАСТРОЙКА ОКНА
win = tk.Tk()
win.title("AutoAirplane")
win.iconbitmap('sub--basics_of_programming/another/gui/cfg/icon.ico')
win.geometry("700x420+400+150")
win.resizable(False, False)
win.minsize(300, 350)

# МЕНЮ ПРОГРАММЫ
menuTop = tk.Menu(win)
win.config(menu = menuTop)

submenuDown = tk.Menu(menuTop, tearoff = 0)
menuTop.add_cascade(label = 'Действие', menu = submenuDown)
submenuDown.add_command(label = 'Выбрать самолет', command = donothing)
submenuDown.add_command(label = 'Добавить новый самолет', command = donothing)
submenuDown.add_separator()
submenuDown.add_command(label = 'Выход из программы', command = quit_from_programm)

helpMenu = tk.Menu(menuTop, tearoff = 0)
menuTop.add_cascade(label = 'Справка', menu = helpMenu)
helpMenu.add_command(label = 'Иснтрукция по использованию', command = openreadme)
helpMenu.add_separator()
helpMenu.add_command(label = 'О программе', command = show_info_about_programm)

# ТЕЛО ПРОГРАММЫ
cnt_ancets = 0
st_name = 0
s_name = 1
s_surname = 1

frame = tk.Frame(win, width=700, height=400)
label1 = tk.Label(frame, text = "", font = ("Calibri", 15, "bold"))
label2 = tk.Label(frame, text = "Фамилия ученика", font = ("Calibri", 15, "bold"))
label4 = tk.Label(frame, text = "Информация", font = ("Calibri", 15, "bold"))
ent1 = tk.Entry(frame, textvariable = s_name)
ent2 = tk.Entry(frame, textvariable = s_surname)
textbox = tk.Text(frame)
btnSearch = tk.Button(frame, text = "Найти", font = ("Calibri", 12, "bold"), command = donothing)
btnContract = tk.Button(frame, text = "Сформировать договор", font = ("Calibri", 12, "bold"),
                        command = donothing)
btnDelete = tk.Button(frame, text = "Удалить ученика", font = ("Calibri", 12, "bold"),
                      command = donothing)
btnChange = tk.Button(frame, text = "Изменить информацию", font = ("Calibri", 12, "bold"),
                      command = open_change_win)

frame.pack()
label1.place(x=375, y=5, height=30, width=300)
label2.place(x=375, y=80, height=30, width=300)
label4.place(x=10, y=5, height=30, width=150)
ent1.place(x=375, y=40, height=30, width=300)
ent2.place(x=375, y=115 ,height=30, width=300)
textbox.place(x=10, y=35, height=330, width=330)
btnSearch.place(x=375, y=170, height=30, width=300)
btnContract.place(x=375, y=210, height=30, width=300)
btnChange.place(x=375, y=315, height=30, width=300)
btnDelete.place(x=375, y=355, height=30, width=300)

win.mainloop()
