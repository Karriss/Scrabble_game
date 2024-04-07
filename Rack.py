class Rack:
    
    def __init__(self, bag):
        self.rack = []
        self.bag = bag
        self.initialize()

    def initialize(self):
        # Добавляем 2 гласные плитки в руку игрока
        for _ in range(2):
            self.addToRack("ГЛАСНАЯ")
        # Добавляем 5 согласные плитки в руку игрока
        for _ in range(5):
            self.addToRack("СОГЛАСНАЯ")

    def addToRack(self, tile_type):
        # Добавляет плитку в руку игрока, учитывая тип плитки
        tile = self.bag.takeFromBag(tile_type)
        self.rack.append(tile)

    def getRackStr(self):
        return ", ".join(str(tile.getLetter()) for tile in self.rack)

    def getRackArr(self):
        return self.rack

    def removeFromRack(self, tile):
        self.rack.remove(tile)

    def getRackLength(self):
        return len(self.rack)

    def replenishRack(self):
        # Подсчитываем количество гласных и согласных плиток в текущей руке
        num_vowels = sum(tile.getLetter() in "АЕИОУЫЭЮЯ" for tile in self.rack)
        num_consonants = sum(tile.getLetter() in "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ" for tile in self.rack)

        # Проверяем, какое условие нужно выполнить для дополнения руки до 7 плиток
        if num_vowels == 1 and num_consonants == 6:
            tiles_to_add = [(1, "ГЛАСНАЯ"), (6, "СОГЛАСНАЯ")]
        elif num_vowels == 2 and num_consonants == 5:
            tiles_to_add = [(2, "ГЛАСНАЯ"), (5, "СОГЛАСНАЯ")]
        elif num_vowels == 3 and num_consonants == 4:
            tiles_to_add = [(3, "ГЛАСНАЯ"), (4, "СОГЛАСНАЯ")]
        else:
            # Если текущее состояние руки не соответствует ни одному из условий, добавляем случайные плитки
            tiles_to_add = [(7 - (num_vowels + num_consonants), "СЛУЧАЙНАЯ")]

        # Добавляем плитки в руку, чтобы она содержала 7 плиток, учитывая условия
        for num_tiles, tile_type in tiles_to_add:
            for _ in range(num_tiles):
                self.addToRack(tile_type)
