from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets rules\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1185x613")
window.configure(bg = "#FFFFFF")

canvas = Canvas(window,bg = "#FFFFFF",height = 613,width = 1185,bd = 0,highlightthickness = 0,relief = "ridge")

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(592.0,306.0,image=image_image_1)

canvas.create_text(509.0,12.0,anchor="nw",text="Правила игры",fill="#000000",font=("IrishGrover Regular", 36 * -1))


image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(592.0,306.0,image=image_image_2)

def close_and_open_window_menu():
    window.destroy()
    subprocess.Popen(['python','menu.py'])

button_image_1 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,
    command=close_and_open_window_menu,
    relief="flat"
)
button_6.place(x=1003.0,y=12.0,width=173.0,height=29.0)
window.resizable(False, False)
window.mainloop()
