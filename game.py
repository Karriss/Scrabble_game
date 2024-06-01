import random
from tkinter import messagebox
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from random import shuffle

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(r"assets game\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("829x613")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 613,
    width = 829,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
used_this_turn = False
existing_words = []
existing_letters = {}
count_skipped_move = 0


glas = ['а','а','а','а','а','а','а','а', 'е', 'е', 'е', 'е', 'е', 'е', 'е', 'е', 'е', 'и', 'и', 'и', 'и', 'и', 'о', 'о', 'о', 'о', 'о', 'о', 'о', 'о', 'о', 'о', 'у', 'у', 'у', 'у', 'ы', 'ы', 'э', 'ю', 'я', 'я']
soglas = ['б', 'б', 'в', 'в', 'в', 'в', 'г', 'г', 'д', 'д', 'д', 'д', 'ж', 'з', 'з', 'й', 'к', 'к', 'к', 'к', 'л', 'л', 'л', 'л', 'м', 'м', 'м', 'н', 'н', 'н', 'н', 'н', 'н', 'н', 'н', 'н', 'п', 'п', 'п', 'п', 'р', 'р', 'р', 'р', 'р', 'с', 'с', 'с', 'с', 'с', 'т', 'т', 'т', 'т', 'ф', 'х', 'ч', 'ш', 'щ', 'ъ', 'ь', 'ь']
original_letters_list = ['а','а','а','а','а','а','а','а','б', 'б', 'в', 'в', 'в', 'в', 'г', 'г', 'д', 'д', 'д', 'д', 'е', 'е', 'е', 'е', 'е', 'е', 'е', 'е', 'е', 'ж', 'з', 'з', 'и', 'и', 'и', 'и', 'и', 'й', 'к', 'к', 'к', 'к', 'л', 'л', 'л', 'л', 'м', 'м', 'м', 'н', 'н', 'н', 'н', 'н', 'н', 'н', 'н', 'н', 'о', 'о', 'о', 'о', 'о', 'о', 'о', 'о', 'о', 'о', 'п', 'п', 'п', 'п', 'р', 'р', 'р', 'р', 'р', 'с', 'с', 'с', 'с', 'с', 'т', 'т', 'т', 'т', 'у', 'у', 'у', 'у', 'ф', 'х', 'ч', 'ш', 'щ', 'ы', 'ы', 'ъ', 'ь', 'ь','э', 'ю', 'я', 'я']


def random_letters():
    vowels = random.sample(glas, 3)
    consonants = random.sample(soglas, 4)
    random_letters = vowels + consonants
    return random_letters


letters_1 = random_letters()
letters_2 = random_letters()


def fill_new_letters(letters_list: list):
    if len(letters_list) < 7:
        for _ in range(7 - len(letters_list)):
            new_letter = random.choice(original_letters_list)
            letters_list.append(new_letter)


def write_letters_player1():
    canvas.create_rectangle(13, 550, 363, 600, fill="white")
    x_kv = 13
    y_kv = 550
    square_size = 50
    for i in range(len(letters_1)):
        x_k1 = x_kv + i * square_size + square_size // 2
        y_k1 = y_kv + square_size // 2
        canvas.create_text(x_k1, y_k1, text=letters_1[i], fill="black", font=("Arial", 20), tags=("kv_text_1", f"kv_lev{i}"))


def write_letters_player2():
    canvas.create_rectangle(461, 550, 811, 600, fill="white")
    square_size = 50
    x_kv = 461
    y_kv = 550
    for i in range(len(letters_2)):
        x_k11 = x_kv + i * square_size + square_size // 2
        y_k11 = y_kv + square_size // 2
        canvas.create_text(x_k11, y_k11, text=letters_2[i], fill="black", font=("Arial", 20), tags=("kv_text_2", f"kv_prav{i}"))


def toggle_letters():
    if toggle_letters.counter % 2 == 0:
        for tag in canvas.find_withtag("kv_text_1"):
            canvas.itemconfig(tag, text="*")
        write_letters_player2()
    else:
        for tag in canvas.find_withtag("kv_text_2"):
            canvas.itemconfig(tag, text="*")
        write_letters_player1()
    toggle_letters.counter += 1


toggle_letters.counter = -1


def check_letters(entry_word, current_letters):
    for letter in entry_word:
        if letter not in current_letters:
            return False
    return True

def word():
    global original_letters_list, letters_1, letters_2, existing_words, canvas, entry_1, entry_2, entry_3, entry_4, existing_letters, count_skipped_move

    entry_word_details = {}
    
    current_letters = letters_1 if toggle_letters.counter % 2 == 0 else letters_2

    with open("dic.txt", "r", encoding="utf-8") as file:
        dictionary = set(word.strip().lower() for word in file)

    entry_word = entry_1.get().lower()  
    start_row_str = entry_2.get() 
    start_column_str = entry_3.get() 
    direction = entry_4.get().lower()

    cell_width = 26
    cell_height = 26
    x_start = 397
    y_start = 47
    x_interval = 2
    y_interval = 3

    if "" in [entry_word, start_row_str, start_column_str, direction]:
        messagebox.showinfo("Предупреждение", "Заполните все поля ввода")
        return
    
    if direction not in ["вправо", "вниз"]:
        messagebox.showerror("Ошибка", "Введите направление 'вправо' или 'вниз'!")
        return
    if not (start_row_str.isdigit() and start_column_str.isdigit()):
        messagebox.showerror("Ошибка", "Строка и столбец должны быть числами!")
        return
    if entry_word not in dictionary:
        messagebox.showerror("Ошибка", f"Слова '{entry_word}' нет в словаре!")
        return
    if entry_word in existing_words:
        messagebox.showerror("Ошибка", f"Слово {entry_word} уже есть на поле!")
        return
    
    start_row = int(start_row_str)
    start_column = int(start_column_str)

    if start_row < 1 or start_row > 15 or start_column < 1 or start_column > 15:
        messagebox.showerror("Ошибка", "Строка или столбец выходит за допустимые границы!")
        return
    if not check_letters(entry_word, current_letters):
        messagebox.showerror("Ошибка", "В вашей руке нет всех введенных букв!")
        return
    
    # Проверка выхода слова за границы поля
    if direction == "вниз":  
        if start_row + len(entry_word) - 1 > 15:
            messagebox.showerror("Ошибка", f"Слово '{entry_word}' выходит за пределы поля!")
            return
    elif direction == "вправо":
        if start_column + len(entry_word) - 1 > 15:
            messagebox.showerror("Ошибка", f"Слово '{entry_word}' выходит за пределы поля!")
            return

    for i, letter in enumerate(entry_word):
        if direction == "вправо":
            row = start_row 
            column = start_column + i
        elif direction == "вниз":
            column = start_column
            row = start_row + i
        entry_word_details[(row, column)] = letter
    
    # Проверка наличия совпадающих букв и их координат
    if existing_letters:
        if not any((row, column) in existing_letters and existing_letters[(row, column)] == letter for (row, column), letter in entry_word_details.items()):
            messagebox.showerror("Ошибка", "Хотя бы одна буква должна совпадать и пересекаться с буквами на поле!")
            return
        for coords in existing_letters.keys():
            try:
                if existing_letters[coords] != entry_word_details[coords] and existing_letters[coords] not in [None, "", " "]:
                    messagebox.showerror("Ошибка", "Слова пересекаются неправильно!")
                    return
            except KeyError:
                pass

    # Проверяем, является ли текущее слово первым на поле и проходит ли оно через центральную клетку
    if not existing_words:
        if (8, 8) not in entry_word_details:
            messagebox.showerror("Ошибка", "Первое слово должно проходить через центральную клетку")
            return

    if direction == "вниз":  
        x1 = x_start + (int(entry_3.get()) - 1) * (cell_width + x_interval) + cell_width / 2
        y1 = y_start + (int(entry_2.get()) - 1) * (cell_height + y_interval) + cell_height
        x_increment = 0
        y_increment = (cell_height + y_interval)

        for letter in entry_word:
            if y1 + cell_height > y_start + 16 * (cell_height + y_interval):  
                messagebox.showerror("Ошибка", "Слово выходит за рамки!")
                return
            canvas.create_text(x1, y1 - cell_height / 2, anchor="center", text=letter, fill="#000000", font=("Kanit Regular", 16 * -1))
            y1 += y_increment

    elif direction == "вправо":
        x1 = x_start + (int(entry_3.get()) - 1) * (cell_width + x_interval)
        y1 = y_start + (int(entry_2.get()) - 1) * (cell_height + y_interval) + cell_height / 2
        x_increment = cell_width + x_interval
        y_increment = 0
    
        for letter in entry_word:
            if x1 + cell_width > x_start + 15 * (cell_width + x_interval): 
                messagebox.showerror("Ошибка", "Слово выходит за рамки!")
                return
            canvas.create_text(x1 + cell_width / 2, y1, anchor="center", text=letter, fill="#000000", font=("Kanit Regular", 16 * -1))
            x1 += x_increment

    #Добавляем слово в словарь
    for i, letter in enumerate(entry_word):
        if direction == "вниз":
            existing_letters[(start_row + i, start_column)] = letter
        elif direction == "вправо":
            existing_letters[(start_row, start_column + i)] = letter

    for letter in entry_word:
        if toggle_letters.counter % 2 == 0:
            letters_1.remove(letter)
            original_letters_list.remove(letter)
            write_letters_player1()
        else:
            letters_2.remove(letter)
            original_letters_list.remove(letter)
            write_letters_player2()

    existing_words.append(entry_word)
    count_skipped_move = -1
    calculateScore(entry_word, start_row, start_column, direction)
    

def pole():
    canvas.create_rectangle(397, 47, 815, 479, fill="white")
    cell_width = 26
    cell_height = 26
    x_start = 397
    y_start = 47
    x_interval = 2
    y_interval = 3
    tileArray = []  
    for row in range(0, 15):
        tileRow = []
        for column in  range(0, 15):
            tileArray.append(tileRow)
            x1 = x_start + row * (cell_width + x_interval)
            y1 = y_start + column * (cell_height + y_interval)
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            canvas.create_rectangle(x1, y1, x2, y2)
            tileRow=[]
    # Вычисляем индексы клетки
            cell_index = (row, column)
            tileArray.append(cell_index)

            if cell_index in [(0,0), (7,0), (14,0), (0,7), (14,7), (0,14), (7,14), (14,14)]:
                canvas.create_rectangle(x1, y1, x2, y2, fill="#D67777") # бледно-розовый 
            elif cell_index in [(3,0), (11,0), (6,2), (8,2), (0,3), (7,3), (14,3), (2,6), (6,6), (8,6), (12,6), (3,7), (11,7), (2,8), (6,8), (8,8), (12,8), (0,11), (7,11), (14,11), (6,12), (8,12)]:
                canvas.create_rectangle(x1, y1, x2, y2, fill="#19C6D1") # бирюзовый
            elif cell_index in [(5,1), (9,1), (1,5), (13,5), (1,9), (13,9), (5,13), (9,13)]:
                canvas.create_rectangle(x1, y1, x2, y2, fill="#4E6FE3") # синий
            elif cell_index in [(1,1), (2,2), (3,3), (4,4), (13,1), (12,2), (11,3), (10,4), (4,10), (3,11), (2,12), (1,13), (10,10), (11,11), (12,12), (13,13)]:
                canvas.create_rectangle(x1, y1, x2, y2, fill="#E21B1B") # красный
            elif cell_index in [(7,7)]:
                canvas.create_rectangle(x1, y1, x2, y2, fill="#F2E142")
            else:
                canvas.create_rectangle(x1, y1, x2, y2)

score_player1 = 0
score_player2 = 0

def calculateScore(word, row, col, direction):
    global score_player1, score_player2
    # синий
    TLS = [(6,2), (10,2), (2,6), (14,6), (2,10), (14,10), (6,14), (10,14)]
    # бирюзовый
    DLS = [(4,1), (12,1), (7,3), (9,3), (1,4), (8,4), (15,4), (3,7), (7,7), (9,7), (13,7), (4,8), (12,8), (3,9), (7,9), (9,9), (13,9), (1,12), (8,12), (15,12), (7,13), (9,13)]
    # бледно-розовый 
    TWS = [(1,1), (8,1), (15,1), (1,8), (15,8), (1,15), (8,15), (15,15)]
    # красный
    DWS = [(2,2), (3,3), (4,4), (5,5), (14,2), (13,3), (12,4), (11,5), (5,11), (4,12), (3,13), (2,14), (11,11), (12,12), (13,13), (14,14)]

    LETTER_VALUES = {
        "А": 1, "Б": 3, "В": 2, "Г": 3, "Д": 2, "Е": 1, "Ж": 5, "З": 5, "И": 1, "Й": 2, "К": 2,
        "Л": 2, "М": 2, "Н": 1, "О": 1, "П": 2, "Р": 2, "С": 2, "Т": 2, "У": 3, "Ф": 10, "Х": 5, "Ц": 10, "Ч": 5,
        "Ш": 10, "Щ": 10, "Ы": 5, "Ъ": 10, "Ь": 5, "Э": 10, "Ю": 10, "Я": 3
    }

    score = 0
    direction = direction.lower()
    word = word.upper()

    if direction == "вправо":
        for countColumn, letter in enumerate(word):
            checkPremiumTuple = (int(row), col + countColumn)
            if checkPremiumTuple in TLS:
                score += LETTER_VALUES[letter] * 3
            elif checkPremiumTuple in DLS:
                score += LETTER_VALUES[letter] * 2
            elif checkPremiumTuple in TWS:
                score += LETTER_VALUES[letter] * 2
            elif checkPremiumTuple in DWS:
                score += LETTER_VALUES[letter] * 3
            else:
                score += LETTER_VALUES[letter]
    
    elif direction == "вниз":
        for countRow, letter in enumerate(word):
            checkPremiumTuple = (row + countRow, int(col))
            if checkPremiumTuple in TLS:
                score += LETTER_VALUES[letter] * 3
            elif checkPremiumTuple in DLS:
                score += LETTER_VALUES[letter] * 2
            elif checkPremiumTuple in TWS:
                score += LETTER_VALUES[letter] * 2
            elif checkPremiumTuple in DWS:
                score += LETTER_VALUES[letter] * 3
            else:
                score += LETTER_VALUES[letter]

    if toggle_letters.counter % 2 == 0:
        if len(letters_1)==0:
            score_player1 += 15
        canvas.create_rectangle(177.0,29.0,226.0,66.0,fill="#E6EA13",outline="")
        score_player1 += score
        canvas.create_text(188.0, 36.0, anchor="nw", text=str(score_player1), fill="#000000", font=("Kanit Regular", 16))
    elif toggle_letters.counter % 2 == 1:
        if len(letters_2)==0:
            score_player2 += 15
        canvas.create_rectangle(177,80,226,117.0,fill="#E6EA13",outline="")
        score_player2 += score
        canvas.create_text(188.0, 86.0, anchor="nw", text=str(score_player2), fill="#000000", font=("Kanit Regular", 16))
    else:
        raise ValueError("Неверный игрок")


def clean_entry():
    entry_1.delete(0, "end")
    entry_2.delete(0, "end")
    entry_3.delete(0, "end")
    entry_4.delete(0, "end")


def end_game():
    global score_player1, score_player2
    if score_player1 > score_player2:
        messagebox.showinfo("Победитель", f"Победил Игрок 1 со счетом: {score_player1}:{score_player2}!") 
        window.destroy()
    elif score_player1 < score_player2:
        messagebox.showinfo("Победитель", f"Победил Игрок 2 со счетом: {score_player2}:{score_player1}!") 
        window.destroy()
    else:
        messagebox.showinfo("Победитель", f"Ничья со счетом {score_player1}:{score_player2}!") 
        window.destroy()


def show_message():
    messagebox.showinfo("Подсказка", "Чтобы задать направление введите 'вправо' или 'влево'")


def zaverch_hod():
    global count_skipped_move, used_this_turn
    result = messagebox.askyesno("Подтверждение", "Вы действительно хотите передать ход?")
    if not result:
        pass
    else:
        count_skipped_move += 1
        fill_new_letters(letters_1)
        fill_new_letters(letters_2)
        toggle_letters()
        clean_entry()
        used_this_turn = False
        if count_skipped_move == 4:
            end_game()  


canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(414.0,306.0,image=image_image_1)

canvas.create_rectangle(369.0,47.0,397.0,479.0,fill="#E6EA13",outline="")
canvas.create_rectangle(397.0,19.0,815.0,47.0,fill="#E6EA13",outline="")
canvas.create_text(162.0,522.0,anchor="nw",text="Игрок 1",fill="#000000",font=("Inter Bold", 16 * -1))
canvas.create_text(610.0,522.0,anchor="nw",text="Игрок 2",fill="#000000",font=("Inter Bold", 16 * -1))

button_image_1 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=zaverch_hod,relief="flat")
button_4.place(x=34.0,y=134.0,width=55.0,height=55.0)

canvas.create_rectangle(30.0,30.0,163.0,67.0,fill="#E6EA13",outline="")
canvas.create_rectangle(30.0,80.0,163.0,117.0,fill="#E6EA13",outline="")
canvas.create_rectangle(177.0,29.0,226.0,66.0,fill="#E6EA13",outline="")
canvas.create_rectangle(177.0,80.0,226.0,117.0,fill="#E6EA13",outline="")
canvas.create_text(38.0,36.0,anchor="nw",text="Игрок 1:",fill="#000000",font=("Kanit Regular", 16 * -1))
canvas.create_text(38.0,86.0,anchor="nw",text="Игрок 2:",fill="#000000",font=("Kanit Regular", 16 * -1))
canvas.create_rectangle(10.0,216.0,173.0,246.0,fill="#E6EA13",outline="")

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(257.0,231.0,image=entry_image_1)
entry_1 = Entry(bd=0,bg="#E6EA13",fg="#000716",highlightthickness=0)
entry_1.place(x=177.0,y=216.0,width=160.0,height=28.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(197.0,265.0,image=entry_image_2)
entry_2 = Entry(bd=0,bg="#E6EA13",fg="#000716",highlightthickness=0)
entry_2.place(x=177.0,y=250.0,width=40.0,height=28.0)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(197.0,299.0,image=entry_image_3)
entry_3 = Entry(bd=0,bg="#E6EA13",fg="#000716",highlightthickness=0)
entry_3.place(x=177.0,y=284.0,width=40.0,height=28.0)

canvas.create_rectangle(10.0,250.0,173.0,280.0,fill="#E6EA13",outline="")
canvas.create_rectangle(10.0,318.0,173.0,348.0,fill="#E6EA13",outline="")
canvas.create_text(14.0,325.0,anchor="nw",text="Введите направление:",fill="#000000",font=("Inter Bold", 15 * -1))

entry_4 = Entry(bd=0,bg="#E6EA13",fg="#000716",highlightthickness=0)
entry_4.place(x=177.0,y=318.0,width=90.0,height=28.0)

canvas.create_rectangle(10.0,284.0,173.0,314.0,fill="#E6EA13",outline="")
canvas.create_text(14.0,289.0,anchor="nw",text="Введите столбец:",fill="#000000",font=("Inter Bold", 16 * -1))
canvas.create_text(14.0,221.0,anchor="nw",text="Введите слово:",fill="#000000",font=("Inter Bold", 16 * -1))
canvas.create_text(14.0, 255.0, anchor="nw", text="Введите строку:", fill="#000000", font=("Inter Bold", 16 * -1))

button_image_2 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=word,relief="flat")
button_5.place(x=13.0,y=364.0,width=160.0,height=30.0)

button_7 = Button(window,text="Завершить игру",bg="#FFFF00",  fg="#000000", font=("Inter Bold", 10),  command=lambda:(window.quit, end_game()))
button_7.place(x=240,  y=33,   width=115,  height=40)

button_8 = Button(window,text="Подсказка",bg="#3FC86E",  fg="#000000", font=("Inter Bold", 12),command=show_message)
button_8.place(x=17,  y=411,   width=110,  height=40 )

# letters_1.regeneration_count = 0
# letters_2.regeneration_count = 0

def write_new_letters():
    global letters_1, letters_2, used_this_turn
    if used_this_turn:
        messagebox.showinfo("Внимание", "Буквы можно менять только 1 раз за ход")
        return
    if toggle_letters.counter % 2 == 0:
        if len(letters_1) != 7:
            return
        letters_1 = random_letters()
        write_letters_player1()
    else:
        if len(letters_2) != 7:
            return
        letters_2 = random_letters()
        write_letters_player2()
    used_this_turn = True


button_9 = Button(window,text="Смена букв",bg="#19C6D1",  fg="#000000", font=("Inter Bold", 12),  command=write_new_letters)
button_9.place(x=183,  y=364,   width=160,  height=30)

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

write_letters_player1()
write_letters_player2()
pole()
toggle_letters()
window.resizable(False, False)
window.mainloop()