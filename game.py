import random
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, messagebox
import tkinter as tk 

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets game\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()

window.geometry("829x613")
window.configure(bg = "#FFFFFF")

current_player = 1

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 613,
    width = 829,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

def change_1():
    # Создаем 7 левых квадратов
    global current_player
    current_player = 1
    white_rect_kv1 = canvas.create_rectangle(13, 550, 363, 600, fill="white")
    square_size = 50
    x_kv = 13
    y_kv = 550
    for i in range(7):
        x_k1 = x_kv + i * square_size
        y_k1 = y_kv
        x_k2 = x_k1 + square_size
        y_k2 = y_k1 + square_size
        canvas.create_rectangle(x_k1, y_k1, x_k2, y_k2, fill="white", tags=("kv_square_lev", f"kv_lev{i}")) #тег для квадрата
        
        start_x_buk_lev = 39
        start_y_buk_lev = 575
        
        # Выбираем случайный символ из русских букв 
        random_letter = random.choice("абвгдежзиклмнопрстуфхцчшщъыьэюя")
        
        # Размещаем букву внутри квадрата, даем тег букве
        canvas.create_text(start_x_buk_lev + i * square_size, start_y_buk_lev, text=random_letter, font=("Arial", 16), tags=f"buk_lev{i}_text") 
        
    for i in range(7):
        canvas.itemconfigure(f"buk_prav{i}_text", state="hidden")  # Скрываем буквы второго игрока
        canvas.itemconfigure(f"buk_lev{i}_text", state="normal")  # Отображаем буквы первого игрока
    current_player = 2
        
def change_2():
    global current_player
    current_player = 2
    white_rect_kv2 = canvas.create_rectangle(461, 550, 811, 600, fill="white")
    square_size = 50
    x_kv = 461
    y_kv = 550
    for i in range(7):
        x_k11 = x_kv + i * square_size
        y_k11 = y_kv
        x_k22 = x_k11 + square_size
        y_k22 = y_k11 + square_size
        canvas.create_rectangle(x_k11, y_k11, x_k22, y_k22, fill="white", tags=("kv_square_prav", f"kv_prav{i}")) 

        start_x_buk_prav = 486
        start_y_buk_prav = 575
            
        # Выбираем случайный символ из русских букв 
        random_letter = random.choice("абвгдежзиклмнопрстуфхцчшщъыьэюя")
            
        # Размещаем букву внутри квадрата
        canvas.create_text(start_x_buk_prav + i * square_size, start_y_buk_prav, text=random_letter, font=("Arial", 16), tags=f"buk_prav{i}_text")

    for i in range(7):
        canvas.itemconfigure(f"buk_lev{i}_text", state="hidden")  # Скрываем буквы первого игрока
        canvas.itemconfigure(f"buk_prav{i}_text", state="normal")  # Отображаем буквы второго игрока
    current_player = 1


def pole():
    white_rect = canvas.create_rectangle(397, 47, 815, 479, fill="white")
    cell_width = 26
    cell_height = 26
    x_start = 397
    y_start = 47
    x_end = 823
    y_end = 486
    x_interval = 2
    y_interval = 3
    tileArray = []  # Список для хранения индексов каждой клетки
    for i in range(15):
        for j in range(15):
            x1 = x_start + i * (cell_width + x_interval)
            y1 = y_start + j * (cell_height + y_interval)
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            canvas.create_rectangle(x1, y1, x2, y2)
    # Вычисляем индексы клетки
            cell_index = (i, j)
            tileArray.append(cell_index)

            if cell_index in [(0,0), (7,0), (14,0), (0,7), (14,7), (0,14), (7,14), (14,14)]:
                canvas.create_rectangle(x1, y1, x2, y2, fill="#D67777")
            elif cell_index in [(3,0), (11,0), (6,2), (8,2), (0,3), (7,3), (14,3), (2,6), (6,6), (8,6), (12,6), (3,7), (11,7), (2,8), (6,8), (8,8), (12,8), (0,11), (7,11), (14,11), (6,12), (8,12)]:
                canvas.create_rectangle(x1, y1, x2, y2, fill="#19C6D1")
            elif cell_index in [(5,1), (9,1), (1,5), (13,5), (1,9), (13,9), (5,13), (9,13)]:
                canvas.create_rectangle(x1, y1, x2, y2, fill="#4E6FE3")
            elif cell_index in [(1,1), (2,2), (3,3), (4,4), (13,1), (12,2), (11,3), (10,4), (4,10), (3,11), (2,12), (1,13), (10,10), (11,11), (12,12), (13,13)]:
                canvas.create_rectangle(x1, y1, x2, y2, fill="#E21B1B")
            elif cell_index in [(7,7)]:
                canvas.create_rectangle(x1, y1, x2, y2, fill="#F2E142")
            else:
                canvas.create_rectangle(x1, y1, x2, y2)


def word():
    entry_word = entry_1.get().lower()  # Получаем введенное слово и приводим к нижнему регистру
    start_row_str = entry_2.get()  # Получаем строку начальной строки из поля ввода
    start_column_str = entry_3.get()  # Получаем строку начального столбца из поля ввода
    direction = entry_4.get().lower()  # Получаем направление из поля ввода и приводим к нижнему регистру

    # Проверка, что все поля ввода заполнены
    if "" in [entry_word, start_row_str, start_column_str, direction]:
        messagebox.showinfo("Предупреждение", "Заполните все поля ввода")
        return

    # Преобразование начальной строки и столбца в целые числа
    start_row = int(start_row_str)
    start_column = int(start_column_str)

    # Проверка, находится ли начальная строка и столбец в допустимом диапазоне от 1 до 15
    if start_row < 1 or start_row > 15 or start_column < 1 or start_column > 15:
        messagebox.showerror("Ошибка", "Строка или столбец выходит за допустимые границы!")
        return

    # Проверка корректности направления
    if direction not in ["вниз", "вправо"]:
        messagebox.showinfo("Предупреждение", "Введите верное направление!")
        return

    cell_width = 26
    cell_height = 26
    x_start = 397
    y_start = 47
    x_interval = 2
    y_interval = 3
    
    if direction == "вниз":  
        x1 = x_start + (start_column - 1) * (cell_width + x_interval) + cell_width / 2
        y1 = y_start + (start_row - 1) * (cell_height + y_interval) + cell_height
        x_increment = 0
        y_increment = (cell_height + y_interval)
        
        # Проверяем каждую букву слова на выход за границы матрицы
        for letter in entry_word:
            if y1 + cell_height > y_start + 16 * (cell_height + y_interval):  # Проверяем, не выходит ли текущая буква за рамки матрицы по вертикали
                messagebox.showerror("Ошибка", "Слово выходит за рамки!")
                # Удаляем уже нарисованные буквы
                canvas.delete("word")
                return
            canvas.create_text(x1, y1 - cell_height / 2, anchor="center", text=letter, fill="#000000", font=("Kanit Regular", 16 * -1), tags="word")
            y1 += y_increment
            
    elif direction == "вправо":  
        x1 = x_start + (start_column - 1) * (cell_width + x_interval)
        y1 = y_start + (start_row - 1) * (cell_height + y_interval) + cell_height / 2
        x_increment = cell_width + x_interval
        y_increment = 0
        
        # Проверяем каждую букву слова на выход за границы матрицы
        for letter in entry_word:
            if x1 + cell_width > x_start + 15 * (cell_width + x_interval):  # Проверяем, не выходит ли текущая буква за рамки матрицы по горизонтали
                messagebox.showerror("Ошибка", "Слово выходит за рамки!")
                # Удаляем уже нарисованные буквы
                canvas.delete("word")
                return
            canvas.create_text(x1 + cell_width / 2, y1, anchor="center", text=letter, fill="#000000", font=("Kanit Regular", 16 * -1), tags="word")
            x1 += x_increment

'''
def check_in_dict(word_to_check):
    try:
        with open('dic.txt', 'r', encoding='utf-8') as dicfile:
            file_content = dicfile.read().splitlines()  # Читаем содержимое файла и разделяем его на строки
    except IOError:
        print("Ошибка: не удается найти файл или прочитать данные")
        return False
    else:
        word_to_check = word_to_check.lower()  # Приводим введенное слово к нижнему регистру
        if word_to_check in file_content:
            return True
        else:
            return False
'''
def сhange_player():
    global current_player
    if current_player == 1: # если ходит первый, то
        current_player = 2 # меняется на второго игрока
        change_2()
    else:
        if current_player == 2:
            current_player = 1
            change_1()
    return

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    414.0,
    306.0,
    image=image_image_1
)

canvas.create_rectangle(
    369.0,
    47.0,
    397.0,
    479.0,
    fill="#E6EA13",
    outline="")

canvas.create_rectangle(
    397.0,
    19.0,
    815.0,
    47.0,
    fill="#E6EA13",
    outline="")

canvas.create_text(
    162.0,
    522.0,
    anchor="nw",
    text="Игрок 1",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    610.0,
    522.0,
    anchor="nw",
    text="Игрок 2",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    #command=сhange_player,
    relief="flat"
)
button_4.place(
    x=34.0,
    y=134.0,
    width=55.0,
    height=55.0
)
     
canvas.create_rectangle(
    30.0,
    30.0,
    163.0,
    67.0,
    fill="#FFFF00",
    outline="")

canvas.create_rectangle(
    30.0,
    80.0,
    163.0,
    117.0,
    fill="#FFFF00",
    outline="")

canvas.create_rectangle(
    177.0,
    29.0,
    226.0,
    66.0,
    fill="#FFFF00",
    outline="")

canvas.create_rectangle(
    177.0,
    80.0,
    226.0,
    117.0,
    fill="#FFFF00",
    outline="")

canvas.create_text(
    38.0,
    36.0,
    anchor="nw",
    text="Игрок 1:",
    fill="#000000",
    font=("Kanit Regular", 16 * -1)
)

canvas.create_text(
    188.0,
    36.0,
    anchor="nw",
    text="0",
    fill="#000000",
    font=("Kanit Regular", 16 * -1)
)

canvas.create_text(
    188.0,
    86.0,
    anchor="nw",
    text="0",
    fill="#000000",
    font=("Kanit Regular", 16 * -1)
)

canvas.create_text(
    38.0,
    86.0,
    anchor="nw",
    text="Игрок 2:",
    fill="#000000",
    font=("Kanit Regular", 16 * -1)
)

canvas.create_rectangle(
    10.0,
    216.0,
    173.0,
    246.0,
    fill="#E6EA13",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    257.0,
    231.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E6EA13",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=177.0,
    y=216.0,
    width=160.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    197.0,
    265.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E6EA13",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=177.0,
    y=250.0,
    width=40.0,
    height=28.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    197.0,
    299.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#E6EA13",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=177.0,
    y=284.0,
    width=40.0,
    height=28.0
)

canvas.create_rectangle(
    10.0,
    250.0,
    173.0,
    280.0,
    fill="#E6EA13",
    outline="")

canvas.create_rectangle(
    10.0,
    318.0,
    173.0,
    348.0,
    fill="#E6EA13",
    outline="")

canvas.create_text(
    14.0,
    325.0,
    anchor="nw",
    text="Введите направление:",
    fill="#000000",
    font=("Inter Bold", 15 * -1)
)

entry_4 = Entry(
    bd=0,
    bg="#E6EA13",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=177.0,
    y=318.0,
    width=90.0,
    height=28.0
)

canvas.create_rectangle(
    10.0,
    284.0,
    173.0,
    314.0,
    fill="#E6EA13",
    outline="")

canvas.create_text(
    14.0,
    289.0,
    anchor="nw",
    text="Введите столбец:",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    14.0,
    221.0,
    anchor="nw",
    text="Введите слово:",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    14.0,
    255.0,
    anchor="nw",
    text="Введите строку:",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=word,
    relief="flat"
)
button_5.place(
    x=13.0,
    y=364.0,
    width=160.0,
    height=30.0
)

button_7 = Button(
    window,
    text="Завершить игру",
    bg="#FFFF00",  
    fg="#000000",  
    font=("Inter Bold", 10),  
    command=window.quit  
)
button_7.place(
    x=240,  
    y=33,   
    width=115,  
    height=40   
)

# Рисуем цифры на столбцы и строки
text_font = ("Inter Bold", 15)
x_start_chisla_lin = 410
y_start_chisla_lin = 35
interval_chisla_lin = 28

for i in range(1, 16):
    x = x_start_chisla_lin + (i - 1) * interval_chisla_lin
    y = y_start_chisla_lin 
    canvas.create_text(x, y, text=str(i), font=text_font)

text_font = ("Inter Bold", 15)
x_start_chisla_stolb = 384
y_start_chisla_stolb = 59
interval_chisla_stolb = 29

for i in range(1, 16):
    x = x_start_chisla_stolb
    y = y_start_chisla_stolb + (i - 1) * interval_chisla_stolb
    canvas.create_text(x, y, text=str(i), font=text_font)

#check_in_dict(word_to_check)
сhange_player()
change_2()
change_1()

pole()

window.resizable(False, False)
window.mainloop()