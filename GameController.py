from tkinter import *
from Board import *
from Bag import *
from Player import *
from Rack import *
from Tile import *
from BoardChecks import *
from WordChecks import *
from EndTurn import *

# Этот модуль реализует внутреннюю логику игры Scrabble.

turn = 1
roundCount = 0
player1Rack = ""
player2Rack = ""

class backEnd:
    mainBoard = Board()
    mainBag = Bag()
    checkBoardRight = CheckBoard.rightCheck(word, row, col, board, count)
    checkBoardDown = CheckBoard.downCheck(word, row, col, board, count)
    endTurn = endTurn()
    player1 = Player(mainBag)
    player2 = Player(mainBag)
    player1Rack = player1.rack.getRackStr()
    player2Rack = player2.rack.getRackStr()

	# обновляет данные интерфейса.
    def updateGUI(updateList, tileArray): #updateList - список кнопок интерфейса, tileArray - массив букв введенного слова
        for tuple in updateList:
            tileArray[tuple[0]][tuple[1]].configure("text", str(tuple[2]))

    '''
    tuple[0] представляет индекс строки плитки в игровом поле.
    tuple[1] представляет индекс столбца плитки в игровом поле.
    tuple[2] представляет новый текст, который нужно отобразить на этой плитке.
    ''' 
    # очищает поля ввода.
    def clearEntry(entryBoxes):
        entryBoxes[0].delete(0, "end")
        entryBoxes[1].delete(0, "end")
        entryBoxes[2].delete(0, "end")

	# пропускает ход пользователя.
    def skipTurn(turnLabel, rackLabel):
        global turn, roundCount
        if roundCount != 0: #проверка началась ли игра
            if turn == 1: # ходит игрок 1
                player2Rack = backEnd.player2.rack.getRackStr()
                rackLabel.configure(text=player2Rack)
                turn = 2
            elif turn == 2:
                player1Rack = backEnd.player1.rack.getRackStr()
                rackLabel.configure(text=player1Rack)
                turn = 1
            roundCount += 1

	# обменивает определенные фишки из стойки на случайные буквы из пакета.
 # param1 строка букв для обмена.
 # param2 метка tkinter для стойки.
 # param3 метка tkinter для текущего хода игроков.
 # param4 кортеж полей ввода в игровом окне.
 # param5 кортеж строк с метками компонентов игрового окна.
    
    def exchangeTiles(exchangedTiles, label, turnLabel, entryBoxes, labels):
        global turn, roundCount
        validMoveL = labels[4] # как-то убрать
        validMove = True
        exchangedTiles = exchangedTiles.upper()
        if turn == 1:
            player1Rack = backEnd.player1.rack.getRackStr()
            for char in exchangedTiles:
                if char not in player1Rack:
                    validMoveL.configure(text="Плитка для обмена отсутствует в стойке")
                    validMove = validMove and False
            if validMove:
                validMoveL.configure(text="")
                endTurn.exchangeTile(exchangedTiles, backEnd.player1.rack)
                player2Rack = backEnd.player2.rack.getRackStr()
                label.configure(text=player2Rack)
                turn = 2
        else:
            player2Rack = backEnd.player2.rack.getRackStr()
            for char in exchangedTiles:
                if char not in player2Rack:
                    validMoveL.configure(text="Плитка для обмена отсутствует в стойке")
                    validMove = validMove and False
            if validMove:
                validMoveL.configure(text="")
                endTurn.exchangeTile(exchangedTiles, backEnd.player2.rack)
                player1Rack = backEnd.player1.rack.getRackStr()
                label.configure(text=player1Rack)
                turn = 1
        backEnd.clearEntry(entryBoxes)
        #roundCount += 1

	# отображает табло.
 
    def scoreBoard(root, frame, score1Label, score2Label):
        winnerStr = ""
        if int(score1Label['text']) > int(score2Label['text']):
            winnerStr = "Победил игрок 1!"
            #winnerL.configure(text="Победил игрок 1!")
        else:
            winnerStr = "Победил игрок 2!"
            #winnerL.configure(text="Победил игрок 2!")
        frame.destroy()
        root.destroy()
        scoreBoardR = Tk()
        scoreBoardR.title('Score Board')
        winnerL = Label(scoreBoardR, text="")
        winnerL.grid(row=0, column=0)
        #winnerL.configure(text=winnerStr)
        #closeB = Button(scoreBoardR, text="Close Score Board", command=scoreBoardR.destroy)
        #closeB.grid(row=1, column=0)
        
        scoreBoardRoot.mainloop()


	# завершает поворот.
 # param1 окно tkinter.
 # param2 рамка tkinter
 # param3 кортеж строк.
 # param4 кортеж объектов меток tkinter.
 # param5 кортеж объектов полей ввода.
 # param6 Объект игрока для текущего игрока.
 # param7 Массив кнопок, представляющих плитки.
    def completeTurn(root, frame, playerMove, label, entryBoxes, player, tileArray):
        global turn, roundCount
        winState = False
        winState = endTurn.checkWinState(backEnd.player1.rack, backEnd.player2.rack, backEnd.mainBag)
        if winState:
            score1Label = label[1] # отображение счета
            score2Label = label[2]
            backEnd.scoreBoard(root, frame, score1Label, score2Label)
        else:
            dirLower = playerMove[3].lower()
            wordUp = playerMove[0].upper()
            sharedLetters = playerMove[4]
            row = playerMove[1]
            col = playerMove[2]
            validMoveL = label[4]
            turnLabel = label[3]
            rackLabel = label[0]
            score1Label = label[1]
            score2Label = label[2]
            score = endTurn.calculateScore(wordUp, row, col, dirLower)
            player.increaseScore(score)
            frontList = endTurn.updateFrontBoard(wordUp, row, col, dirLower)
            backEnd.mainBoard.updateBackBoard(wordUp, row, col, dirLower)
            backEnd.updateGUI(frontList, tileArray)
            endTurn.removeTile(wordUp, player.rack)
            validMoveL.configure(text="")
            backEnd.clearEntry(entryBoxes)
            roundCount += 1
            
            # Определение, чей сейчас ход, и соответствующее обновление метки rackLabel
            if turn == 1:
                player2Rack = backEnd.player2.rack.getRackStr()
                player1Rack = '*' * len(backEnd.player1.rack.getRackStr())  # Звездочки для скрытия фишек первого игрока
                rackLabel.configure(text=player1Rack)
                turn = 2
            elif turn == 2:
                player1Rack = backEnd.player1.rack.getRackStr()
                player2Rack = '*' * len(backEnd.player2.rack.getRackStr())  # Звездочки для скрытия фишек второго игрока
                rackLabel.configure(text=player2Rack)
                turn = 1

	# проверяет, является ли введенный ход допустимым.
 # окно tkinter.
 # рамка tkinter
 # кортеж строк.
 # кортеж объектов меток tkinter.
 # кортеж объектов полей ввода.
 # Объект игрока для текущего игрока.
 # Массив кнопок, представляющих плитки.
    def endChecks(root, frame, playerMove, labels, entryBoxes, player, tileArray):
        global roundCount
        dirLower = playerMove[3].lower()
        wordUp = playerMove[0].upper()
        sharedLetters = playerMove[4]
        row = playerMove[1]
        col = playerMove[2]
        validMoveL = labels[4]
        validTurn = False
        if sharedLetters == "":
            validTurn = checkRack(wordUp, player.rack.getRackStr())
            validTurn = validTurn and checkInDict(wordUp)
        else:
            rackWord = wordUp
            for char in sharedLetters:
                rackWord = rackWord.replace(char, "")
            validTurn = checkRack(rackWord, player.rack.getRackStr())
            validTurn = validTurn and checkInDict(wordUp)
        backEnd.clearEntry(entryBoxes)
        if validTurn:
            if dirLower == "down":
                validTurn = checkBoardDown.downCheck(wordUp, row, col, backEnd.mainBoard.getBoard(), roundCount)
                if validTurn:
                    backEnd.completeTurn(root, frame, playerMove, labels, entryBoxes, player, tileArray)
                else:
                    validMoveL.configure(text="Неверный ход, пожалуйста, повторите попытку")
            elif dirLower == "right":
                validTurn = checkBoardRight.rightCheck(wordUp, row, col, backEnd.mainBoard.getBoard(), roundCount)
                if validTurn:
                    backEnd.completeTurn(root, frame, playerMove, labels, entryBoxes, player, tileArray)
                else:
                    validMoveL.configure(text="Неверный ход, пожалуйста, повторите попытку")
            else:
                validMoveL.configure(text="Неверный ход, пожалуйста, повторите попытку")
        else:
            validMoveL.configure(text="Неверный ход, пожалуйста, повторите попытку")

	# принимает введенный пользователем ход.
    def endMove(root, frame, word, row, col, dir, sharedLetters, labels, entryBoxes, tileArray):
        global turn
        playerMove = (word, row, col, dir, sharedLetters)
        if turn == 1:
            backEnd.endChecks(root, frame, playerMove, labels, entryBoxes, backEnd.player1, tileArray)
        elif turn == 2:
            backEnd.endChecks(root, frame, playerMove, labels, entryBoxes, backEnd.player2, tileArray)
