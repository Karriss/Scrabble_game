from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets rules\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window1 = Tk()

window1.geometry("1185x613")
window1.configure(bg = "#FFFFFF")

canvas = Canvas(window1,bg = "#FFFFFF",height = 613,width = 1185,bd = 0,highlightthickness = 0,relief = "ridge")

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(592.0,306.0,image=image_image_1)

canvas.create_text(509.0,12.0,anchor="nw",text="Правила игры",fill="#000000",font=("IrishGrover Regular", 36 * -1))
canvas.create_rectangle(0,94,1207,534,fill="#F5F5F5",outline="")

def close_and_open_window_menu():
    window1.destroy()
    subprocess.Popen(['python','menu.py'])
button_image_1 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=close_and_open_window_menu,relief="flat")

button_image_1 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=close_and_open_window_menu,relief="flat")
button_6.place(x=1003.0,y=12.0,width=173.0,height=29.0)

image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(336.0,313.0,image=image_image_9)

image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(912,249,image=image_image_10)

window1.resizable(False, False)
window1.mainloop()
