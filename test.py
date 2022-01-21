from tkinter import *  
from tkinter import ttk  
    
window = Tk()
window.title("Илья")
#Первые цифры ширина, вторые высота.  
window.geometry('750x500')
window.resizable(width=0, height=0)
tab_control = ttk.Notebook(window)
sec = 100
n = 0

def end():
    global n, window

    edit['state'] = 'disable'
    edit1['state'] = 'disable'
    edit2['state'] = 'disable'
    edit3['state'] = 'disable'
    edit4['state'] = 'disable'
    edit5['state'] = 'disable'
    edit6['state'] = 'disable'
    edit7['state'] = 'disable'
    edit8['state'] = 'disable'  

    if n == 9:
        t2.config(text = 'Итог: ' + str(n) + '(б)' ' --- ' + 'отлично')
        t2['state'] = 'disable'
    elif n == 8 or n == 7:
        t2.config(text = 'Итог: ' + str(n) + '(б)' ' --- ' + 'хорошо')
        t2['state'] = 'disable'
    elif n == 6 or n == 5:
        t2.config(text = 'Итог: ' + str(n) + '(б)' ' --- ' + 'удовлетворительно')
        t2['state'] = 'disable'
    else:
        t2.config(text = 'Итог: ' + str(n) + '(б)' ' --- ' + 'плохо')
        t2['state'] = 'disable'


def forbut():
    global n, window
    
    edit['state'] = 'disable'
    edit1['state'] = 'disable'
    edit2['state'] = 'disable'

    login = edit.get()
    
    if login == "Москва":
        n = n + 1
    else:
        n = n + 0
        
    login1 = edit1.get()
        
    if login1 == "Вашингтон":
        n = n + 1
    else:
        n = n + 0

    login2 = edit2.get()
            
    if login2 == "Лондон":
        n = n + 1
    else:
        n = n + 0

        

def forbut_1():
    global n, window

    edit3['state'] = 'disable'
    edit4['state']='disable'
    edit5['state']='disable'

    login3 = edit3.get()
            
    if login3 == "Киев":
        n = n + 1
    else:
        n = n + 0

    login4 = edit4.get()

    if login4 == "Варшава":
        n = n + 1
    else:
        n = n + 0

    login5 = edit5.get()

    if login5 == "Пекин":
        n = n + 1
    else:
        n = n + 0


def forbut_2():
    global n, window

    edit6['state']='disable'
    edit7['state']='disable'
    edit8['state']='disable'      

    login6 = edit6.get()
            
    if login6 == "Анкара":
        n = n + 1
    else:
        n = n + 0

    login7 = edit7.get()
            
    if login7 == "Каир":
        n = n + 1
    else:
        n = n + 0

    login8 = edit8.get()

    if login8 == "Афины":
        n = n + 1
    else:
        n = n + 0


def start():
    global sec, window
    but['state']='normal'
    but2['state']='disable'
    but1['state']='normal'
    but3['state']='normal'
    but4['state']='normal'
    lbl0.config(text = '1) Столицей России является:')
    lbl1.config(text = '2) Столицей США является:')
    lbl2.config(text = '3) Столицей Англии является:')
    lbl3.config(text = '4) Столицей Украины является:')
    lbl4.config(text = '5) Столицей Польши является:')
    lbl5.config(text = '6) Столицей Китая является:')
    lbl6.config(text = '7) Столицей Турции является:')
    lbl7.config(text = '8) Столицей Египта является:')
    lbl8.config(text = '9) Столицей Греции является:')

    if sec > 0:
        sec -= 1
        t1.config(text = 'До конца времени: ' + str(sec))
        t3.config(text = 'До конца времени: ' + str(sec))
        t4.config(text = 'До конца времени: ' + str(sec))
        window.after(1000, start)
    else:
        but1['state']='disable'
        but['state']='disable'
        but3['state']='disable'
        but4['state']='disable'
        edit['state'] = 'disable'
        edit1['state'] = 'disable'
        edit2['state'] = 'disable'
        edit3['state'] = 'disable'
        edit4['state']='disable'
        edit5['state']='disable'
        edit6['state']='disable'
        edit7['state']='disable'
        edit8['state']='disable'      

tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control) 

tab_control.add(tab1, text='Стр.1')  
tab_control.add(tab2, text='Стр.2')  
tab_control.add(tab3, text='Стр.3')

lb1 = Label(tab1, text="Тест по географии:", font=("Arial Bold", 15))  
lb1.grid(column=0, row=1) 


lbl2 = Label(tab1, text="Задание №1", font=("Arial Bold", 15))  
lbl2.grid(column=0, row=2)

lbl0 = Label(tab1, text="1) ...", font=("Arial Bold", 15))  
lbl0.grid(column=0, row=3)

edit = Entry(tab1,width=10,font=("Arial Bold", 15))
edit.grid(column=2, row=4)
edit['state']='normal'

a = Label(tab1, text="Ответ:", font=("Arial Bold", 15))  
a.grid(column=0, row=4)


lbl1 = Label(tab1, text="2) ...", font=("Arial Bold", 15))  
lbl1.grid(column=0, row=5)

edit1 = Entry(tab1,width=10,font=("Arial Bold", 15))
edit1.grid(column=2, row=6)
edit1['state']='normal'

b = Label(tab1, text="Ответ:", font=("Arial Bold", 15))  
b.grid(column=0, row=6)


lbl2 = Label(tab1, text="3) ...", font=("Arial Bold", 15))  
lbl2.grid(column=0, row=7)

edit2 = Entry(tab1,width=10,font=("Arial Bold", 15))
edit2.grid(column=2, row=8)
edit2['state']='normal'

с = Label(tab1, text="Ответ:", font=("Arial Bold", 15))  
с.grid(column=0, row=8)


lbl00 = Label(tab2, text="Задание №2", font=("Arial Bold", 15))  
lbl00.grid(column=0, row=11)

lbl3 = Label(tab2, text="4) ...", font=("Arial Bold", 15))  
lbl3.grid(column=0, row=12)

edit3 = Entry(tab2,width=10,font=("Arial Bold", 15))
edit3.grid(column=2, row=13)
edit3['state']='normal'

d = Label(tab2, text="Ответ:", font=("Arial Bold", 15))  
d.grid(column=0, row=13)


lbl4 = Label(tab2, text="5) ...", font=("Arial Bold", 15))  
lbl4.grid(column=0, row=14)

edit4 = Entry(tab2,width=10,font=("Arial Bold", 15))
edit4.grid(column=2, row=15)
edit4['state']='normal'

e = Label(tab2, text="Ответ:", font=("Arial Bold", 15))  
e.grid(column=0, row=15)


lbl5 = Label(tab2, text="6) ...", font=("Arial Bold", 15))  
lbl5.grid(column=0, row=16)

edit5 = Entry(tab2,width=10,font=("Arial Bold", 15))
edit5.grid(column=2, row=17)
edit5['state']='normal'

f = Label(tab2, text="Ответ:", font=("Arial Bold", 15))  
f.grid(column=0, row=17)


lbl000 = Label(tab3, text="Задание №3", font=("Arial Bold", 15))  
lbl000.grid(column=0, row=19)


lbl6 = Label(tab3, text="7) ...", font=("Arial Bold", 15))  
lbl6.grid(column=0, row=20)

edit6 = Entry(tab3,width=10,font=("Arial Bold", 15))
edit6.grid(column=2, row=21)
edit6['state']='normal'

j = Label(tab3, text="Ответ:", font=("Arial Bold", 15))  
j.grid(column=0, row=21)


lbl7 = Label(tab3, text="8) ...", font=("Arial Bold", 15))  
lbl7.grid(column=0, row=22)

edit7 = Entry(tab3,width=10,font=("Arial Bold", 15))
edit7.grid(column=2, row=23)
edit7['state']='normal'

h = Label(tab3, text="Ответ:", font=("Arial Bold", 15))  
h.grid(column=0, row=23)


lbl8 = Label(tab3, text="9) ...", font=("Arial Bold", 15))  
lbl8.grid(column=0, row=24)

edit8 = Entry(tab3,width=10,font=("Arial Bold", 15))
edit8.grid(column=2, row=25)
edit8['state']='normal'

i = Label(tab3, text="Ответ:", font=("Arial Bold", 15))  
i.grid(column=0, row=25)


but = Button(tab1, text="1.Ввести", font=("Arial Bold", 12), command = forbut)
but.grid(column=3, row=2)
but['state']='disable'

but1 = Button(tab2, text="2.Ввести", font=("Arial Bold", 12), command = forbut_1)
but1.grid(column=3, row=11)
but1['state']='disable'

but3 = Button(tab3, text="3.Ввести", font=("Arial Bold", 12), command = forbut_2)
but3.grid(column=3, row=19)
but3['state']='disable'

but2 = Button(tab1, text = 'Начать', font=("Arial Bold", 12), command = start)
but2.grid(column=2, row=1)
but2['state']='normal'

but4 = Button(tab3, text = 'Завершить', font=("Arial Bold", 12), command = end)
but4.grid(column=3, row=26)
but4['state']='disable'


t2 = Label(tab3, text = 'Итог: ', font=("Arial Bold", 15))
t2.grid(column=4, row=26)

t1 = Label(tab1, text = 'Таймер: ', font=("Arial Bold", 15))
t1.grid(column=4, row=1)

t3 = Label(tab2, text = 'Таймер: ', font=("Arial Bold", 15))
t3.grid(column=4, row=1)

t4 = Label(tab3, text = 'Таймер: ', font=("Arial Bold", 15))
t4.grid(column=4, row=1)

tab_control.pack(expand=1, fill='both')  
window.mainloop()