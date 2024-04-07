import random
from Rack import *


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Карина\Desktop\Коды\assets game\frame0")


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
    135.0,
    522.0,
    anchor="nw",
    text="Игрок 1",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    572.0,
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
    command=lambda: print("button_4 clicked"),
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
    fill="#F2E142",
    outline="")

canvas.create_rectangle(
    30.0,
    80.0,
    163.0,
    117.0,
    fill="#F2E142",
    outline="")

canvas.create_rectangle(
    177.0,
    29.0,
    226.0,
    66.0,
    fill="#F2E142",
    outline="")

canvas.create_rectangle(
    177.0,
    80.0,
    226.0,
    117.0,
    fill="#F2E142",
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

canvas.create_text(
    410.0,
    28.0,
    anchor="nw",
    text="1",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    381.0,
    53.0,
    anchor="nw",
    text="1",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    380.0,
    84.0,
    anchor="nw",
    text="2",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    438.0,
    28.0,
    anchor="nw",
    text="2",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    465.0,
    28.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    381.0,
    112.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    492.0,
    28.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    381.0,
    140.0,
    anchor="nw",
    text="4",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    520.0,
    28.0,
    anchor="nw",
    text="5",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    520.0,
    28.0,
    anchor="nw",
    text="5",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    381.0,
    170.0,
    anchor="nw",
    text="5",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    578.0,
    28.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    382.0,
    229.0,
    anchor="nw",
    text="7",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    604.0,
    28.0,
    anchor="nw",
    text="8",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    381.0,
    259.0,
    anchor="nw",
    text="8",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    631.0,
    28.0,
    anchor="nw",
    text="9",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    381.0,
    289.0,
    anchor="nw",
    text="9",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    655.0,
    28.0,
    anchor="nw",
    text="10",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    372.0,
    317.0,
    anchor="nw",
    text="10",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    685.0,
    28.0,
    anchor="nw",
    text="11",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    373.0,
    345.0,
    anchor="nw",
    text="11",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    712.0,
    28.0,
    anchor="nw",
    text="12",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    372.0,
    373.0,
    anchor="nw",
    text="12",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    739.0,
    28.0,
    anchor="nw",
    text="13",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    372.0,
    404.0,
    anchor="nw",
    text="13",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    768.0,
    28.0,
    anchor="nw",
    text="14",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    372.0,
    432.0,
    anchor="nw",
    text="14",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    547.0,
    28.0,
    anchor="nw",
    text="6",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    381.0,
    201.0,
    anchor="nw",
    text="6",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    795.0,
    28.0,
    anchor="nw",
    text="15",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    372.0,
    460.0,
    anchor="nw",
    text="15",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
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
    284.0,
    173.0,
    314.0,
    fill="#E6EA13",
    outline="")

canvas.create_text(
    14.0,
    289.0,
    anchor="nw",
    text="Введите строку:",
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
    text="Введите столбец:",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=12.0,
    y=338.0,
    width=160.0,
    height=30.0
)

button_7 = Button(
    window,
    text="Завершить игру",
    bg="#FFFF00",  # желтый цвет
    fg="#000000",  # черный цвет текста
    font=("Inter Bold", 10),  
    command=window.quit  # команда при нажатии
)
button_7.place(
    x=240,  
    y=33,   
    width=115,  # ширина кнопки
    height=40   # высота кнопки
)

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


# Создаем 7 левых квадратов
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

# Создаем 7 правых квадратов
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


window.resizable(False, False)
window.mainloop()
