from WordChecks import *
from Board import *
import copy

# Этот метод реализует проверку того, может ли данное слово быть введено на доску.
class CheckBoard:

    # Проверяет, занята ли ячейка в выбранном месте размещения слова.
    @staticmethod
    # возвращает логическое значение, указывающее, есть ли на доске плитки, занимающие выбранное расположение слов.
    def occupiedTile(word, row, col, board, direction):
        row = int(row)
        colcount = int(col)
        wordUp = word.upper()
        matchesTile = False
        if direction == "right":
            # Проверка для горизонтального размещения
            for char in wordUp:
                if board[row][colcount] == "0":
                    colcount += 1
                elif board[row][colcount] == char: #соответствует символу
                    colcount += 1
                    matchesTile = True
                else:
                    return False
        elif direction == "down":
            # Проверка для вертикального размещения
            rowcount = int(row)
            col = int(col)
            for char in wordUp:
                if board[rowcount][col] == "0":
                    rowcount += 1
                elif board[rowcount][col] == char:
                    rowcount += 1
                    matchesTile = True
                else:
                    return False
        return matchesTile and True

    # Обновляет текущий объект доски.
    @staticmethod
    def updateArray(word, row, col, adjBoard, direction):
        countRow = int(row)
        countCol = int(col)
        for char in word:
            char = char.upper()
            if direction == "вправо":
                # Обновление доски для горизонтального размещения
                adjBoard[int(row)][countCol] = char
                countCol += 1
            elif direction == "вниз":
                # Обновление доски для вертикального размещения
                adjBoard[countRow][int(col)] = char
                countRow += 1
        return adjBoard

    # Проверяет, образует ли введенное слово дополнительные слова из смежно существующих слов.
    # возвращает логическое значение, указывающее, что из смежно существующих слов может быть сформировано больше слов.
    @staticmethod
    def adjWordCheck(word, row, col, board, direction):
        colCount = int(col)
        rowCount = int(row)
        corrWords = True
        findWord = ""
        #создайте копию доски для проверки размещения
        adjBoard = copy.deepcopy(board)
        adjBoard = CheckBoard.updateArray(word, row, col, adjBoard, direction)
        
        if direction == "вправо":
            # Проверка для горизонтального размещения
            for char in word:
                if adjBoard[int(row)-1][colCount] == "0" and adjBoard[int(row) + 1][colCount] == "0":
                    colCount += 1
                else:
                    findWord = ""
                    while adjBoard[rowCount][colCount] != "0":
                        rowCount += 1
                    end = rowCount
                    rowCount = int(row)
                    while adjBoard[rowCount][colCount] != "0":
                        rowCount -= 1
                    rowCount += 1
                    begin = rowCount
                    for rown in range(begin, end):
                        findWord = findWord + adjBoard[rown][colCount]
                    wordExists = checkInDict(findWord)
                    corrWords = corrWords and wordExists
                    colCount += 1
        elif direction == "вниз":
            # Проверка для вертикального размещения
            for char in word:
                if adjBoard[rowCount][int(col)-1] == "0" and adjBoard[rowCount][int(col)+1] == "0":
                    rowCount += 1
                else:
                    findWord = ""
                    while adjBoard[rowCount][colCount] != "0":
                        colCount += 1
                    end = colCount
                    colCount = int(col)
                    while adjBoard[rowCount][colCount] != "0":
                        colCount -= 1
                    colCount += 1
                    begin = colCount
                    for coln in range(begin, end):
                        findWord = findWord + adjBoard[rowCount][coln]
                    wordExists = checkInDict(findWord)
                    corrWords = corrWords and wordExists
                    rowCount += 1
        return corrWords

    # Проверяет, не выходит ли введенное слово за пределы игрового поля.
    @staticmethod
    # возвращает логическое значение, указывающее, что размещение слов находится в пределах доски.
    def outOfBounds(word, row, col, board):
        col = int(col)
        row = int(row)
        return (col <= 14 and row <= 14 and row + len(word) <= 14)

    # Выполняет проверку размещения, используя описанные выше функции.
    @staticmethod
    # возвращает логическое значение, указывающее допустимое размещение слов в текущем состоянии доски.
    def placementCheck(word, row, col, board, count, direction):
        if direction == "вправо":
            # Проверка для горизонтального размещения
            colcount = int(col)
            wordUp = word.upper()
            if int(count) == 0:
                return (int(row) == 7) and (int(col) == 7)
            else:
                return CheckBoard.occupiedTile(word, row, col, board, direction)
        elif direction == "вниз":
            # Проверка для вертикального размещения
            rowCount = int(row)
            colCount = int(col)
            wordUp = word.upper()
            if int(count) == 0:
                return (int(row) == 7) and (int(col) == 7)
            else:
                return CheckBoard.occupiedTile(word, row, col, board, direction)

    # Краткая заключительная проверка слова, введенного в горизонтальном направлении.
    @staticmethod
    # возвращает логическое значение, указывающее, может ли слово быть размещено в правильном направлении или нет.
    def rightCheck(word, row, col, board, count):
        return CheckBoard.outOfBounds(word, row, col, board) and CheckBoard.placementCheck(word, row, col, board, count, "вправо") and CheckBoard.adjWordCheck(word, row, col, board, "вправо")
# outOfBounds - метод проверяет, находится ли слово word в пределах границ игрового поля, заданных его размерами row и col, представленных в board.
# adjWordCheck - метод проверяет, что после размещения слова word вправо на игровом поле board нет перекрывающихся слов.
    
    # Краткая заключительная проверка слова, введенного в вертикальном направлении.
    @staticmethod
    # возвращает логическое значение, указывающее, может ли слово быть размещено в правильном направлении или нет.
    def downCheck(word, row, col, board, count):
        return CheckBoard.outOfBounds(word, row, col, board) and CheckBoard.placementCheck(word, row, col, board, count, "вниз") and CheckBoard.adjWordCheck(word, row, col, board, "вниз")
