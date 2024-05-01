from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Карина\Desktop\Коды\assets menu\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("550x458")
window.configure(bg = "#FFFFFF")

def close_and_open_window_rules():
    window.destroy()
    subprocess.Popen(['python','rules.py'])

def close_and_open_window_game():
    window.destroy()
    subprocess.Popen(['python','game.py'])

def close_window():
    window.destroy()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 458,
    width = 550,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    275,
    229,
    image=image_image_1)

image_paths = [
    "image_2.png",
    "image_3.png",
    "image_4.png",
    "image_5.png",
    "image_6.png",
    "image_7.png",
    "image_8.png"
]
coordinates = [
    (157.0, 83.0),
    (98.0, 83.0),
    (216.0, 83.0),
    (275.0, 83.0),
    (334.0, 83.0),
    (393.0, 83.0),
    (452.0, 83.0)
]

# Выводим изображения на холсте циклом
images = []
for i, image_path in enumerate(image_paths):
    image = PhotoImage(file=relative_to_assets(image_path))
    images.append(image)  # Сохраняем изображение в переменную
    canvas.create_image(coordinates[i][0], coordinates[i][1], image=image)  # Создаем изображение на холсте

button_image_1 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=close_window,
    relief="flat"
)
button_1.place(
    x=123.0,
    y=339.0,
    width=304.0,
    height=47.0
)

def open_game():
    subprocess.Popen(['python','game.py'])
button_image_2 = PhotoImage(file=relative_to_assets("button_1.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=close_and_open_window_game,
    relief="flat"
)
button_2.place(    x=125.0,
    y=205.0,
    width=304.0,
    height=47.0
)
def open_rules():
    subprocess.Popen(['python','rules.py'])

button_image_3 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=close_and_open_window_rules,
    relief="flat"
)
button_3.place(
    x=125.0,
    y=271.0,
    width=305.0,
    height=55.0
)
window.resizable(False, False)
window.mainloop()
