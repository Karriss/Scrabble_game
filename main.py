from tkinter import *
from WidgetCreation import *
from GameController import *

# Этот модуль реализует интерфейс игры "Скрэббл".


# Инициализирует вводное окно в игру "Скрэббл".
class frontEndMain:

	# инициализирует окно для ознакомления с игрой в Скрэббл.
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1500x900")
        self.root.title("Scrabble")
        self.startF = Frame(self.root)
        self.introF = Frame(self.root)
        self.introF.grid(row = 0,column = 0)
        welcomeL = Label(self.introF, text = "Welcome to Scrabble")
        welcomeL.grid(row = 0, column = 0)

        instructionsB = Button(self.introF, text = "Instructions", command=lambda: frontEndMain.instructions(self))
        instructionsB.grid(row = 1, column = 0)

        startB = Button(self.introF, text = "Start Game", command=lambda: frontEndMain.getPlayerName(self))
        startB.grid(row = 2, column = 0)

        self.root.mainloop()

    # метод - появляется окно с инструкциями для игрока.
    def instructions(self):
        instructR = Toplevel()
        instructR.title('Instructions')

        strInstruct = """Instructions for Scrabble:
        You get a rack of 7 tiles to start the game. You must play words with these
        7 tiles so that each word formed vertically and horizontally is a word.

        \tNote: Whenever you play a word, make sure that it touches at least
        The game ends when there are no tiles left in the bag."""
        # Отображает этикетку с инструкциями по игре в Скрэббл.
        instrL = Label(instructR, text = strInstruct)
        instrL.grid(row = 0, column = 0)
      # Закрывает окно после нажатия кнопки.
        closeB = Button(instructR, text = "Close Instructions", command = instructR.destroy)
        closeB.grid(row = 1, column = 0)

    # Позволяет игроку вводить свои имена и сохраняет их значения.
    def getPlayerName(self):
        self.introF.grid_remove()
        self.startF.grid(row = 0, column = 0)
        p1L = Label(self.startF, text = "Enter Name of Player One")
        p1L.grid(row = 0, column = 0)
        play1E = Entry(self.startF)
        play1E.grid(row = 0, column = 1)

        p2L = Label(self.startF, text = "Enter Name of Player Two")
        p2L.grid(row = 2, column = 0)
        play2E = Entry(self.startF)
        play2E.grid(row = 2, column = 1)

        playB = Button(self.startF, text = "Let's play", command = lambda: BoardFrame.scrabbleBoard(self.root, self.startF, play1E.get(), play2E.get()))
        playB.grid(row = 3, column = 1)

	# уничтожает окно, когда игра заканчивается
    def destroyWindow(self):
        self.startF.destroy()
        self.introF.destroy()

class BoardFrame:
	# инициализирует и поддерживает игровую доску scrabble.
 # корневое окно param1, в котором выполняется игра.
 # рамка param2, содержащая различные компоненты игровой доски.
 # имя игрока param31.
 # имя игрока param422.
    def scrabbleBoard(root, frame, player1Name, player2Name):
        # Массив плиток, используемый для доступа к плиткам для их обновления.
        global tileArray
        tileArray = []

        # Скрыть сетку ввода игрока
        frame.grid_remove()
        # Сохранение имен игроков для метки хода.
        global p1Name, p2Name, turn
        p1Name = player1Name
        p2Name = player2Name

        # Создаем рамку, на которой будет проходить игра в Скрэббл.
        boardF = Frame(root)
        boardF.grid(row = 0,column = 0)
        #Создаем надписи на внешней стороне доски.
 #Создаем пустую надпись для создания интервалов.
        emptyL1 = Label(boardF, text = " ")
        emptyL1.grid(row = 0, column = 0)
        #Цикл, который создает надписи для столбцов доски.
        for col in range(1, 16):
            makeLabels(boardF, 0, col, str(col-1))
        #Цикл, который создает метки для строк на доске.
        for row in range(1, 16):
            makeLabels(boardF, row, 0, str(row-1))

      #Создаем боковую панель для игры.
 #Создаем метку хода, которая указывает, какой ход у игрока в данный момент.
        turnL = Label(boardF, text = "Player " + str(p1Name) + "'s turn")
        turnL.grid(row = 2, column = 17)
        #Создание меток для оценки игрока
        p1ScoreL = Label(boardF, text = str(p1Name) + "'s Score")
        p1ScoreL.grid(row = 3, column = 17)
        p2ScoreL = Label(boardF, text = str(p2Name) + "'s Score")
        p2ScoreL.grid(row = 3, column = 18)
      #метки для значений оценки
        p1ScoreValL = Label(boardF, text = "0")
        p1ScoreValL.grid(row = 4, column = 17)
        p2ScoreValL = Label(boardF, text = "0")
        p2ScoreValL.grid(row = 4, column = 18)
   #Кнопки для завершения хода, пропуска ходов и обмена фишками.
        endMoveB = Button(boardF, text = "End Move", command=lambda: backEnd.endMove(root, boardF, inputWordE.get(), inputRowE.get(), inputColE.get(), inputDirE.get(), inputWordSharedE.get(), labelTuple, entryTuple, tileArray, p1Name, p2Name))
        endMoveB.grid(row = 11, column = 17)
        skipTurnB = Button(boardF, text = "Skip Turn", command=lambda: backEnd.skipTurn(turnL, playerRackL))
        skipTurnB.grid(row = 11, column = 18)
        exchangeTilesB = Button(boardF, text = "Exchange Tiles", command=lambda: backEnd.exchangeTiles(inputWordExchangeE.get(), playerRackL, turnL, entryTuple, labelTuple))
        exchangeTilesB.grid(row = 11, column = 19)
      #пустая метка в качестве буфера
        emptyL2 = Label(boardF, text = " ")
        emptyL2.grid(row = 0,column = 16,rowspan = 15)
        #Метка и поля ввода для слова, строки, столбца и направления.
        playerRackL = Label(boardF, text = backEnd.player1Rack)
        playerRackL.grid(row = 5, column = 17)
        validMoveL = Label(boardF, text = "")
        validMoveL.grid(row = 6, column = 17)
        inputWordL = Label(boardF, text = "Enter word")
        inputWordL.grid(row = 7, column = 17)
        inputWordE = Entry(boardF)
        inputWordE.grid(row = 7, column = 18)
        inputWordSharedL = Label(boardF, text = "Enter Shared Letters")
        inputWordSharedL.grid(row = 7, column = 19)
        inputWordSharedE = Entry(boardF)
        inputWordSharedE.grid(row = 7, column = 20)
        inputWordExchangeL = Label(boardF, text = "Enter Tiles to Exchange")
        inputWordExchangeL.grid(row = 8, column = 19)
        inputWordExchangeE = Entry(boardF)
        inputWordExchangeE.grid(row = 8, column = 20)
        inputRowL = Label(boardF, text = "Enter row")
        inputRowL.grid(row = 8, column = 17)
        inputRowE = Entry(boardF)
        inputRowE.grid(row = 8, column = 18)
        inputColL = Label(boardF, text = "Enter column")
        inputColL.grid(row = 9, column = 17 )
        inputColE = Entry(boardF)
        inputColE.grid(row = 9, column = 18)
        inputDirL = Label(boardF, text = "Enter direction")
        inputDirL.grid(row = 10, column = 17)
        inputDirE = Entry(boardF)
        inputDirE.grid(row = 10, column = 18)
        #наборы данных, которые должны быть переданы в игровой контроллер
        labelTuple = (playerRackL, p1ScoreValL, p2ScoreValL, turnL, validMoveL)
        entryTuple = (inputWordE, inputRowE, inputColE, inputDirE, inputWordSharedE, inputWordExchangeE)

        #создание плиток
        for row in range(1, 16):
            tileRow = []
            for column in  range(1, 16):
                tile = makeButtons(boardF, "floral white", row, column, "")
                tileRow.append(tile)
            tileArray.append(tileRow)

        #настройка цвета и текста плиток
        tileArray[0][0].configure("text", "TWS")
        tileArray[0][0].configure("bg", "LightGoldenrod1")
        tileArray[0][3].configure("text", "DLS")
        tileArray[0][3].configure("bg", "Light Blue")
        tileArray[0][7].configure("text", "TWS")
        tileArray[0][7].configure("bg", "LightGoldenrod1")
        tileArray[0][11].configure("text", "DLS")
        tileArray[0][11].configure("bg", "Light Blue")
        tileArray[0][14].configure("text", "TWS")
        tileArray[0][14].configure("bg", "LightGoldenrod1")

        tileArray[1][1].configure("text", "DWS")
        tileArray[1][1].configure("bg", "Pink")
        tileArray[1][5].configure("text", "TLS")
        tileArray[1][5].configure("bg", "pale green")
        tileArray[1][9].configure("text", "TLS")
        tileArray[1][9].configure("bg", "pale green")
        tileArray[1][13].configure("text", "DWS")
        tileArray[1][13].configure("bg", "Pink")

        tileArray[2][2].configure("text", "DWS")
        tileArray[2][2].configure("bg", "Pink")
        tileArray[2][6].configure("text", "DLS")
        tileArray[2][6].configure("bg", "Light Blue")
        tileArray[2][8].configure("text", "DLS")
        tileArray[2][8].configure("bg", "Light Blue")
        tileArray[2][12].configure("text", "DWS")
        tileArray[2][12].configure("bg", "Pink")

        tileArray[3][0].configure("text", "DLS")
        tileArray[3][0].configure("bg", "Light Blue")
        tileArray[3][3].configure("text", "DWS")
        tileArray[3][3].configure("bg", "Pink")
        tileArray[3][7].configure("text", "DLS")
        tileArray[3][7].configure("bg", "Light Blue")
        tileArray[3][11].configure("text", "DWS")
        tileArray[3][11].configure("bg", "Pink")
        tileArray[3][14].configure("text", "DLS")
        tileArray[3][14].configure("bg", "Light Blue")

        tileArray[4][4].configure("text", "DWS")
        tileArray[4][4].configure("bg", "Pink")
        tileArray[4][10].configure("text", "DWS")
        tileArray[4][10].configure("bg", "Pink")

        tileArray[5][1].configure("text", "TLS")
        tileArray[5][1].configure("bg", "pale green")
        tileArray[5][5].configure("text", "TLS")
        tileArray[5][5].configure("bg", "pale green")
        tileArray[5][9].configure("text", "TLS")
        tileArray[5][9].configure("bg", "pale green")
        tileArray[5][13].configure("text", "TLS")
        tileArray[5][13].configure("bg", "pale green")

        tileArray[6][2].configure("text", "DLS")
        tileArray[6][2].configure("bg", "Light Blue")
        tileArray[6][6].configure("text", "DLS")
        tileArray[6][6].configure("bg", "Light Blue")
        tileArray[6][8].configure("text", "DLS")
        tileArray[6][8].configure("bg", "Light Blue")
        tileArray[6][12].configure("text", "DLS")
        tileArray[6][12].configure("bg", "Light Blue")

        tileArray[7][0].configure("text", "TWS")
        tileArray[7][0].configure("bg", "LightGoldenrod1")
        tileArray[7][3].configure("text", "DLS")
        tileArray[7][3].configure("bg", "Light Blue")
        tileArray[7][7].configure("text", "★")
        tileArray[7][7].configure("bg", "Pink")
        tileArray[7][11].configure("text", "DLS")
        tileArray[7][11].configure("bg", "Light Blue")
        tileArray[7][14].configure("text", "TWS")
        tileArray[7][14].configure("bg", "LightGoldenrod1")

        tileArray[8][2].configure("text", "DLS")
        tileArray[8][2].configure("bg", "Light Blue")
        tileArray[8][6].configure("text", "DLS")
        tileArray[8][6].configure("bg", "Light Blue")
        tileArray[8][8].configure("text", "DLS")
        tileArray[8][8].configure("bg", "Light Blue")
        tileArray[8][12].configure("text", "DLS")
        tileArray[8][12].configure("bg", "Light Blue")

        tileArray[9][1].configure("text", "TLS")
        tileArray[9][1].configure("bg", "pale green")
        tileArray[9][5].configure("text", "TLS")
        tileArray[9][5].configure("bg", "pale green")
        tileArray[9][9].configure("text", "TLS")
        tileArray[9][9].configure("bg", "pale green")
        tileArray[9][13].configure("text", "TLS")
        tileArray[9][13].configure("bg", "pale green")

        tileArray[10][4].configure("text", "DWS")
        tileArray[10][4].configure("bg", "Pink")
        tileArray[10][10].configure("text", "DWS")
        tileArray[10][10].configure("bg", "Pink")

        tileArray[11][0].configure("text", "DLS")
        tileArray[11][0].configure("bg", "Light Blue")
        tileArray[11][3].configure("text", "DWS")
        tileArray[11][3].configure("bg", "Pink")
        tileArray[11][7].configure("text", "DLS")
        tileArray[11][7].configure("bg", "Light Blue")
        tileArray[11][11].configure("text", "DWS")
        tileArray[11][11].configure("bg", "Pink")
        tileArray[11][14].configure("text", "DLS")
        tileArray[11][14].configure("bg", "Light Blue")

        tileArray[12][2].configure("text", "DWS")
        tileArray[12][2].configure("bg", "Pink")
        tileArray[12][6].configure("text", "DLS")
        tileArray[12][6].configure("bg", "Light Blue")
        tileArray[12][8].configure("text", "DLS")
        tileArray[12][8].configure("bg", "Light Blue")
        tileArray[12][12].configure("text", "DWS")
        tileArray[12][12].configure("bg", "Pink")

        tileArray[13][1].configure("text", "DWS")
        tileArray[13][1].configure("bg", "Pink")
        tileArray[13][5].configure("text", "TLS")
        tileArray[13][5].configure("bg", "pale green")
        tileArray[13][9].configure("text", "TLS")
        tileArray[13][9].configure("bg", "pale green")
        tileArray[13][13].configure("text", "DWS")
        tileArray[13][13].configure("bg", "Pink")

        tileArray[14][0].configure("text", "TWS")
        tileArray[14][0].configure("bg", "LightGoldenrod1")
        tileArray[14][3].configure("text", "DLS")
        tileArray[14][3].configure("bg", "Light Blue")
        tileArray[14][7].configure("text", "TWS")
        tileArray[14][7].configure("bg", "LightGoldenrod1")
        tileArray[14][11].configure("text", "DLS")
        tileArray[14][11].configure("bg", "Light Blue")
        tileArray[14][14].configure("text", "TWS")
        tileArray[14][14].configure("bg", "LightGoldenrod1")

frontEndView = frontEndMain()
gameController = backEnd()
