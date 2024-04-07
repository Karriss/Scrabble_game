from tkinter import *

# Этот модуль реализует методы для создания надписей и кнопок tkinter.


class makeLabels:
    def __init__(self, frame, row, column, text):
        self.frame = frame
        self.row = row
        self.column = column
        self.text = text

        self.label = Label(self.frame, text = self.text)
        self.label.grid(row = self.row, column = self.column)

class makeButtons:
        def __init__(self, frame, colour, row, column, text):
            self.frame = frame
            self.colour = colour
            self.row = row
            self.column = column
            self.text = text

            if colour == "":
                self.button = Button(self.frame, height = 2, width = 6, state = DISABLED, text=self.text)
            else:
                self.button = Button(self.frame, height = 2, width = 6, state = DISABLED, bg = self.colour, text=self.text)
            self.button.grid(row = self.row, column = self.column)
			
		## настраивает атрибут кнопок.
 # изменяемый атрибут param1.
 # текстовый параметр param2, с помощью которого можно изменить компонент.
        def configure(self, attribute, text):
            self.button[attribute] = text
