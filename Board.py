#  Этот метод реализует базовую модель доски для игры в Скрэббл.

class Board:
	# инициализирует объект board.
    def __init__(self):
        self.backBoard = [["0" for col in range(0, 15)] for row in range(0, 15)]

	## Этот метод возвращает объект доски backBoard.
    def getBoard(self):
        return self.backBoard

    # param1 целое число, представляющее строку начальной плитки.
 # param2 целое число, представляющее столбец начальной плитки.
 # param3 строка, представляющая направление слова, размещенного на доске.
 # param4 строка, представляющая слово, размещаемое на доске.
 # exceptions ValueError, если слово не соответствует ограничениям доски.
    def updateBackBoard(self, word, row, col, dir):
        dirLower = dir.lower()
        wordUp = word.upper()
        row = int(row)
        col = int(col)
        if row > 14 or col > 14 or len(word) > 14:
            raise ValueError("Слово выходит за рамки")
        if(dirLower == "right"): # символы слова последовательно размещаются вдоль строки, начиная с указанного столбца col.
            countCol = int(col)
            for char in wordUp:
                char = char.upper()
                self.backBoard[int(row)][int(countCol)] = char
                countCol += 1
        elif(dirLower == "down"): # символы слова последовательно размещаются вдоль столбца, начиная с указанной строки row
            countRow = int(row)
            for char in word:
                char = char.upper()
                self.backBoard[int(countRow)][int(col)] = char
                countRow += 1
        else:
            raise ValueError("Неверное направление")
