from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Карина\Desktop\Коды\assets rules\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window1 = Tk()

window1.geometry("1207x495")
window1.configure(bg = "#FFFFFF")


canvas = Canvas(
    window1,
    bg = "#FFFFFF",
    height = 495,
    width = 1207,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    604.0,
    247.00000000000003,
    image=image_image_1
)

canvas.create_text(
    563.0,
    12.0,
    anchor="nw",
    text="Правила игры",
    fill="#000000",
    font=("IrishGrover Regular", 24 * -1)
)

canvas.create_rectangle(
    12.0,
    49.0,
    1207.0,
    474.0,
    fill="#F5F5F5",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_2 = canvas.create_image(
    338.0,
    260.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_3 = canvas.create_image(
    944.0,
    261.0,
    image=image_image_3
)
def close_and_open_window_menu():
    window1.destroy()
    subprocess.Popen(['python','menu.py'])
button_image_1 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=close_and_open_window_menu,
    relief="flat"
)
button_1.place(
    x=1003.0,
    y=12.0,
    width=173.0,
    height=29.0
)
window1.resizable(False, False)
window1.mainloop()
