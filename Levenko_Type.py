from tkinter import *
from tkinter import ttk
from random import choice
import time
import threading

com_mode_rus = False #Глобальная переменная для обработчика языка создал их чтобы после работы они очищались
com_mode_eng = False 
com_num_val = 10 
skeep = 0 #Пропущенно слов
entry_input_list = [] #Слова написанные пользователем
error_dict = {} #Ошибки
txt_list = [] #Слова сгенерированые, которые НАДА написать
time_sec = 0
time_min = 0
time_stop = False
all_time_sec_end = 0
all_time_sec_start = 0


#INFO
def window_info(title="", geometry="", bg=""):
    window_info = Tk()
    
    window_info.title(title)
    window_info.geometry(geometry)
    window_info.configure(background=bg)
    window_info.resizable(False, False)

    def button_send_info_click():
        window_info.destroy()
        window_main("Главное окно", "1280x720", "#708090")
    
    image_info = PhotoImage(file=r"C:\Users\Nike\Desktop\Scripts\Python\Lev_Type\textinfo.png")
    label_info = Label(window_info, image=image_info)
    label_info.configure(width=700, height=700)
    label_info.place(x=0, y=0)
    
    button_send_main = Button(window_info, text= "Back", command=button_send_info_click)
    button_send_main.configure(width=15, height=3)
    button_send_main.place(x=1140, y=30)

    window_info.mainloop()


#RESULT
def window_result(title="", geometry="", bg=""):
    save_file = open(r"C:\Users\Nike\Desktop\Scripts\Python\Lev_Type\Save.txt", mode="rt", encoding="UTF-8")
    txt_save_file = save_file.read().split(" ")
    
    window_result = Tk()
    
    window_result.title(title)
    window_result.geometry(geometry)
    window_result.configure(background=bg)
    window_result.resizable(False, False)
    
    
    label_result = Label(window_result, text=" ".join(txt_save_file).lower(), wraplength=1100)
    label_result.configure(background="#A9A9A9", font="Times 18")
    label_result.place(x=10,y=10) 
    
    def button_send_info_click():
        window_result.destroy()
        window_main("Главное окно", "1280x720", "#708090")
    
    button_send_main = Button(window_result, text= "Back", command=button_send_info_click)
    button_send_main.configure(width=15, height=3)
    button_send_main.place(x=1140, y=30)

    window_result.mainloop()

#START
def window_start(title="", geometry="", bg=""):
    global combox_mode_rus, com_mode_eng, time_sec, time_min, time_stop
    
    window_start = Tk()
    
    window_start.title(title)
    window_start.geometry(geometry)
    window_start.configure(background=bg)
    window_start.resizable(False, False)
    
    
    def on_key_press(event):
        global time_sec, time_min, time_stop, all_time_sec_start
        if time_stop == False: 
            time_stop = True 
            time_sec = int(time.strftime('%S', time.localtime()))
            time_min = int(time.strftime('%M', time.localtime()))
            all_time_sec_start = time_sec + (time_min * 60)
            print(all_time_sec_start)

    window_start.bind("<Key>", on_key_press)
            
    def button_send_click():
        global com_mode_rus, com_mode_eng, txt_list
        
        com_mode_eng = False
        com_mode_rus = False
        txt_list = []
        window_start.destroy()
        window_main("Главное окно", "1280x720", "#708090")
    
    button_send_main = Button(window_start, text= "Back", command=button_send_click)
    button_send_main.configure(width=15, height=3)
    button_send_main.place(x=1140, y=30)
    
    def open_file_txt(way):
        global com_num_val, txt_list

        file_txt = open(rf"{way}", mode="rt", encoding="UTF-8")
        file_txt_read = file_txt.read().split(" ")
        for x in range(com_num_val):
            txt_list.append(choice(file_txt_read))
    
    
    if com_mode_rus == True and com_mode_eng != True:
        open_file_txt(r"C:\Users\Nike\Desktop\Scripts\Python\Lev_Type\Rus.txt")
    elif com_mode_eng == True and com_mode_rus != True:
        open_file_txt(r"C:\Users\Nike\Desktop\Scripts\Python\Lev_Type\Eng.txt")
    else:
        open_file_txt(r"C:\Users\Nike\Desktop\Scripts\Python\Lev_Type\Rus.txt")
    
    label_txt_start = Label(window_start, text=" ".join(txt_list).lower(), wraplength=1128)
    label_txt_start.configure(background="#A9A9A9", font="Times 18")
    label_txt_start.place(x=100,y=250)
    
    #Обработчик нажатия enter
    def on_enter(event):
        global txt_list, skeep, entry_input_list, time_stop
        
        time_stop = False
        pass_word = 0
        
        entry_input = entry_start.get()
        entry_input_list = entry_input.split(" ")
        
        #ВЫВОД ОКНА РЕЗУЛЬТАТОВ
        def result_start():
            global txt_list, entry_input_list, skeep, error_dict, time_sec, time_min, all_time_sec_end, all_time_sec_start

            save_file = open(r"C:\Users\Nike\Desktop\Scripts\Python\Lev_Type\Save.txt", mode="rt+", encoding="UTF-8")
                    
            window_result_start = Tk()
            
            window_result_start.title("Результат")
            window_result_start.geometry("500x500")
            window_result_start.configure(background="gray")
            window_result_start.resizable(False, False)

        
            #ПРОВЕРКА ПРОПУЩЕННЫХ СЛОВ
            if len(entry_input_list) < len(txt_list):
                skeep += len(txt_list) - len(entry_input_list)
            elif len(txt_list) < len(entry_input_list):
                skeep += len(txt_list) - len(entry_input_list)
            
            #Проверка ошибок
            if len(entry_input_list) < len(txt_list):
                for x in range(len(entry_input_list)):
                    if entry_input_list[x] != txt_list[x]:
                        error_dict[txt_list[x]] = entry_input_list[x]
            elif len(entry_input_list) > len(txt_list):
                for x in range(len(txt_list)):
                    if txt_list[x] != entry_input_list[x]:
                        error_dict[txt_list[x]] = entry_input_list[x]    
            elif len(entry_input_list) == len(txt_list):
                for x in range(len(txt_list)):
                    if txt_list[x] != entry_input_list[x]:
                        error_dict[txt_list[x]] = entry_input_list[x]  
            
            print(error_dict)
            label_info_result = Label(window_result_start, text="Пропущено слов или добавлено лишних = {} \n Допущено ошибок = {}".format(skeep, len(error_dict)))
            save_file.write("Пропущено слов или добавлено лишних = {} \n Допущено ошибок = {}".format(skeep, len(error_dict)))
            label_info_result.configure(background="#A9A9A9", font="Times 14")
            label_info_result.place(x=0, y=10)

            
            time_sec = int(time.strftime('%S', time.localtime()))
            time_min = int(time.strftime('%M', time.localtime()))
            all_time_sec_end = time_sec + (time_min * 60)
            fin_time = all_time_sec_end - all_time_sec_start
            fin_time_word = fin_time / len(entry_input_list)
            time_min = 0
            while fin_time > 60:
                fin_time -= 60
                time_min += 1
                
            
            label_time = Label(window_result_start, text=f"Полное время \nСекунд = {fin_time}, Минут = {time_min} \n Время в секундах на одно слово = {fin_time_word}")
            save_file.write(f"\nПолное время \nСекунд = {fin_time}, Минут = {time_min} \n Время в секундах на одно слово = {fin_time_word}")
            label_time.configure(background="#A9A9A9", font="Times 14")
            label_time.place(x=0, y=100)
            fin_time = 0
            time_min = 0
            time_sec = 0
            
            # Вывод пар ключ-значение
            y_position = 200
            count = 0
            for key, value in error_dict.items():
                if count < 9: 
                    error_label = Label(window_result_start, text=f"Ошибка: {value}, Правильное слово: {key}")
                    error_label.configure(background="#A9A9A9", font="Times 14")
                    error_label.place(x=0, y=y_position)
                    y_position += 30
                    count += 1
                else:
                    break
            error_dict = {}
            skeep = 0
            txt_list = []

            window_start.destroy()
            window_main("Главное окно", "1280x720", "#708090")
            window_result_start.mainloop()
            
            
        print(entry_input_list)
        print(txt_list)
        result_start()

         
        
    entry_start = Entry(window_start, font="Times 18", background="#A9A9A9")
    entry_start.place(x=100, y=450, height=40, width=1100)
    entry_start.bind('<Return>', on_enter)
    
    window_start.mainloop()

#MAIN
def window_main(title="", geometry="", bg=""):
    window_main = Tk()
    
    window_main.title(title)
    window_main.geometry(geometry)
    window_main.configure(background=bg)
    window_main.resizable(False, False)

    #ОБРАБОТЧИКИ
    def button_send_info_click():
        window_main.destroy()
        window_info("Информация", "1280x720", "white")
        
    def button_send_result_click():
        window_main.destroy()
        window_result("Результаты", "1280x720", "gray")
        
    def button_send_start_click():
        window_main.destroy()
        window_start("Старт", "1280x720", "gray")
    ###   
    
    #Генерация кнопок главного окна
    def Generate_Button(name_but, txt, cmd, confW, confH, x1, y1, bg): #button_send_info
        name_but = Button(window_main, text= txt, command=cmd, background=f"{bg}")
        name_but.configure(width=confW, height=confH)
        name_but.place(x=x1, y=y1)
    
    
    ###COMBOX
    label_combox_mode = Label(window_main, text="Выберите режим", font="Times 13", background="#708090")
    label_combox_mode.place(x=360, y=360)
    
    def com_mode(event):
        global com_mode_rus, com_mode_eng
        
        values = combox_mode.get()
        if values == "rus":
            com_mode_rus = True
            com_mode_eng = False
        elif values == "eng":
            com_mode_eng = True
            com_mode_rus = False
        else:
            com_mode_rus = True
            com_mode_eng = False
    
    def com_num(event):
        global com_num_val
        com_num_val = int(combox_num.get())
    
    launges_mode = ["rus", "eng"]
    combox_mode = ttk.Combobox(values=launges_mode)
    combox_mode.place(x=352, y=390)
    combox_mode.bind("<<ComboboxSelected>>", com_mode)
    
    label_combox_num = Label(window_main, text="Количество слов", font="Times 13", background="#708090")
    label_combox_num.place(x=800, y=360)
    
    launges_num = [5, 10, 20, 30, 40, 50]
    combox_num = ttk.Combobox(values=launges_num)
    combox_num.place(x=794, y=390)
    combox_num.bind("<<ComboboxSelected>>", com_num)
    ###
    
    label_image_logo = PhotoImage(file=r"C:\Users\Nike\Desktop\Scripts\Python\Lev_Type\lev.png")
    label_image_logo_main = Label(window_main, image=label_image_logo, background="#708090")
    label_image_logo_main.place(y=50, x=330)
        
    Generate_Button("button_send_info", "Info", button_send_info_click, 15, 3, 1140, 30, "#E0FFFF")
    Generate_Button("button_send_result", "Результаты", button_send_result_click, 15, 3, 30, 30,"#E0FFFF")
    Generate_Button("button_send_result", "Старт", button_send_start_click, 25, 5, 555, 450, "#E0FFFF")

    window_main.mainloop()

window_main("Главное окно", "1280x720", "#708090")



