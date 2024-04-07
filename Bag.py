from Tile import *
from random import shuffle

#  Этот метод реализует базовую модель сумки для игры в Скрэббл.
# пгршшрлришрили
class Bag:

   # инициализирует модель пакета, вызывая метод initBag(), который добавляет в пакет 100 плиток по умолчанию.
    def __init__(self):
        self.bag = []
        self.initBag()

    # Добавляет определенное количество определенной плитки в пакет. Принимает плитку и целое количество в качестве аргументов.
 # @param1 объект плитки, представляющий буквенную плитку.
 # @param2 количество плиток, добавляемых к обратной стороне.
    def addToBag(self, tile, numOfTiles): # Метод для добавления определенного количества плиток в мешок.
        for i in range(numOfTiles):
            self.bag.append(tile)

    # инициализирует пакет с плитками из 100 букв, необходимыми для прохождения игры
    def initBag(self):
        self.addToBag(Tile("А"), 8)
        self.addToBag(Tile("Б"), 2)
        self.addToBag(Tile("В"), 4)
        self.addToBag(Tile("Г"), 2)
        self.addToBag(Tile("Д"), 4)
        self.addToBag(Tile("Е"), 9)
        self.addToBag(Tile("Ж"), 1)
        self.addToBag(Tile("З"), 2)
        self.addToBag(Tile("И"), 5)
        self.addToBag(Tile("Й"), 1)
        self.addToBag(Tile("К"), 4)
        self.addToBag(Tile("Л"), 4)
        self.addToBag(Tile("М"), 3)
        self.addToBag(Tile("Н"), 5)
        self.addToBag(Tile("О"), 10)
        self.addToBag(Tile("П"), 4)
        self.addToBag(Tile("Р"), 5)
        self.addToBag(Tile("С"), 5)
        self.addToBag(Tile("Т"), 5)
        self.addToBag(Tile("У"), 4)
        self.addToBag(Tile("Ф"), 1)
        self.addToBag(Tile("Х"), 1)
        self.addToBag(Tile("Ц"), 1)
        self.addToBag(Tile("Ч"), 1)
        self.addToBag(Tile("Ш"), 1)
        self.addToBag(Tile("Щ"), 1)
        self.addToBag(Tile("Ы"), 2)
        self.addToBag(Tile("Ъ"), 1)
        self.addToBag(Tile("Ь"), 2)
        self.addToBag(Tile("Э"), 1)
        self.addToBag(Tile("Ю"), 1)
        self.addToBag(Tile("Я"), 2)
        shuffle(self.bag)

   # Извлекает плитку из пакета.
 # Возвращает плитку с торца пакета.
    def takeFromBag(self): # для извлечения одной плитки из мешка.
        return self.bag.pop()

    # Возвращает количество плиток, оставшихся в пакете.
 # возвращает количество плиток, оставшихся в пакете.
    def getRemainingTiles(self): # возвращает количество оставшихся плиток в мешке.
        return len(self.bag)
