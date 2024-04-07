from Tile import *
from Rack import *
from Bag import *

class endTurn:

    @staticmethod
    def updateFrontBoard(word, row, col, dir):
        frontList = []
        dirLower = dir.lower()
        wordUp = word.upper()
        if dirLower == "вправо":
            countCol = int(col)
            for char in wordUp:
                configTuple = (int(row), countCol, char.upper())
                frontList.append(configTuple)
                countCol += 1
            return frontList
        elif dirLower == "вниз":
            countRow = int(row)
            for char in wordUp:
                configTuple = (countRow, int(col), char.upper())
                frontList.append(configTuple)
                countRow += 1
            return frontList
        else:
            raise ValueError("Неверное направление")

    @staticmethod
    def removeTile(word, rack):
        wordUp = word.upper()
        for letter in wordUp:
            for tile in rack.getRackArr():
                if tile.getLetter() == letter:
                    rack.removeFromRack(tile)
        rack.replenishRack()

    @staticmethod
    def calculateScore(word, row, col, dir):
        TWS = [(0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14)]
        DWS = [(1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4),  (13,13), (12, 12), (11,11), (10,10), (7,7)]
        TLS = [(1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9)]
        DLS = [(0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11)]

        LETTER_VALUES = {
            "А": 1, "Б": 3, "В": 2, "Г": 3, "Д": 2, "Е": 1, "Ж": 5, "З": 5, "И": 1, "Й": 2, "К": 2,
        "Л": 2, "М": 2, "Н": 1, "О": 1, "П": 2, "Р": 2, "С": 2, "Т": 2, "У": 3, "Ф": 10, "Х": 5, "Ц": 10, "Ч": 5,
        "Ш": 10, "Щ": 10, "Ы": 5, "Ъ": 10, "Ь": 5, "Э": 10, "Ю": 10, "Я": 3
        }


        multiplierWord = 1
        score = 0
        dirLower = dir.lower()
        wordUp = word.upper()
        if dirLower == "вправо":
            countCol = int(col)
            for char in wordUp:
                checkPremiumTuple = (int(row), countCol)
                if checkPremiumTuple in TLS:
                    score += LETTER_VALUES[char]*3
                elif checkPremiumTuple in DLS:
                    score += LETTER_VALUES[char]*2
                elif checkPremiumTuple in TWS:
                    multiplierWord *= 3
                    score += LETTER_VALUES[char]
                elif checkPremiumTuple in DWS:
                    multiplierWord *= 2
                    score += LETTER_VALUES[char]
                else:
                    score += LETTER_VALUES[char]
                countCol += 1
            score *= multiplierWord
        elif dirLower == "вниз":
            countRow = int(row)
            for char in wordUp:
                checkPremiumTuple = (int(countRow), int(col))
                if checkPremiumTuple in TLS:
                    score += LETTER_VALUES[char]*3
                elif checkPremiumTuple in DLS:
                    score += LETTER_VALUES[char]*2
                elif checkPremiumTuple in TWS:
                    multiplierWord *= 3
                    score += LETTER_VALUES[char]
                elif checkPremiumTuple in DWS:
                    multiplierWord *= 2
                    score += LETTER_VALUES[char]
                else:
                    score += LETTER_VALUES[char]
                countRow += 1
            score *= multiplierWord
        else:
            raise ValueError("Неверное направление")
        return score

    @staticmethod
    def checkWinState(rack1, rack2, bag):
        emptyRack = (rack1.getRackLength() == 0) or (rack2.getRackLength() == 0)
        if emptyRack and bag.getRemainingTiles() == 0:
            return True
        else:
            return False
