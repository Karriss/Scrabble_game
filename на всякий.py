import tkinter as tk
import random

from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Карина\Desktop\Коды\assets game\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def hide_letters_and_make_move():
    global player_turn

    player_turn = not player_turn

    if player_turn:
        for i in range(7):
            canvas.itemconfig(f"buk_lev{i}_text", text=random.choice("абвгдежзиклмнопрстуфхцчшщъыьэюя"))
            canvas.itemconfig(f"buk_prav{i}_text", text="*")
    else:
        for i in range(7):
            canvas.itemconfig(f"buk_lev{i}_text", text="*")
            canvas.itemconfig(f"buk_prav{i}_text", text=random.choice("абвгдежзиклмнопрстуфхцчшщъыьэюя"))


window = tk.Tk()

window.geometry("829x613")
window.configure(bg="#FFFFFF")

canvas = tk.Canvas(
    window,
    bg="#FFFFFF",
    height=613,
    width=829,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# Остальной ваш код...

def hide_letters_and_make_move():
    global player_turn

    player_turn = not player_turn

    if player_turn:
        for i in range(7):
            canvas.itemconfig(f"buk_lev{i}_text", text=random.choice("абвгдежзиклмнопрстуфхцчшщъыьэюя"))
            canvas.itemconfig(f"buk_prav{i}_text", text="*")
    else:
        for i in range(7):
            canvas.itemconfig(f"buk_lev{i}_text", text="*")
            canvas.itemconfig(f"buk_prav{i}_text", text=random.choice("абвгдежзиклмнопрстуфхцчшщъыьэюя"))


# Создаем кнопку для совершения хода и скрытия букв
button = tk.Button(
    window,
    text="Совершить ход и скрыть буквы",
    command=hide_letters_and_make_move
)
button.place(x=500, y=500)

window.resizable(False, False)
window.mainloop()