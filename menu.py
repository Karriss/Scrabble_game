from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets menu\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("720x480")
window.configure(bg = "#FFFFFF")

def close_and_open_window_rules():
    window.destroy()
    subprocess.Popen(['python','rules.py'])

def close_and_open_window_game():
    window.destroy()
    subprocess.Popen(['python','game.py'])

def close_window():
    window.destroy()

canvas = Canvas(window,bg = "#FFFFFF",height = 480,width = 720,bd = 0,highlightthickness = 0,relief = "ridge")

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(360.0,240.00000000000006,image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(171.0,80.00000000000006,image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(236.0,81.00000000000006,image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(301.0,80.00000000000006,image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(431.0,80.00000000000006,image=image_image_5)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(496.0,80.00000000000006,image=image_image_6)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(561.0,80.00000000000006,image=image_image_7)

image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(366.0,80.00000000000006,image=image_image_8)

def open_game():
    subprocess.Popen(['python','game.py'])

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=close_and_open_window_rules,relief="flat")
button_1.place(x=188.0,y=291.00000000000006,width=356.0,height=61.0)

def open_rules():
    subprocess.Popen(['python','rules.py'])

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=close_and_open_window_game,relief="flat")
button_2.place(x=204.0,y=218.00000000000006,width=320.0,height=63.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=close_window,relief="flat")

button_3.place(x=211.0,y=364.00000000000006,width=313.0,height=52.0)
window.resizable(False, False)
window.mainloop()
