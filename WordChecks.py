# Проверяет, можно ли составить слово из столбца.
# param1 введенное слово, чтобы проверить, находятся ли его буквы в столбце.
# param2 столбец, из которого можно проверить буквы слов.
# возвращает логическое значение, указывающее, можно ли создать word из rack.
# исключения ValueError, если введена пустая строка
    
def checkRack(word, rack):
    if word is None:
        raise ValueError("Необходимо ввести слово")
    if rack is None: # rack - набор выданных букв
        raise ValueError("Необходимо предоставить набор букв")

    wordUp = word.upper()
    for char in wordUp:
        if char not in rack:
            return False
    return True


# Проверяет, принадлежит ли слово словарю scrabble.
# param1 введенное слово для проверки, существует ли оно в словаре текстового файла.
# возвращает логическое значение, указывающее, что слово существует в словаре.
# исключения IOError, если текстовый файл не может быть найден.
def checkInDict(word):
    try:
        dicfile = open('dic.txt', 'r')
        file1 = dicfile.read()
    except IOError:
        print ("Error: can\'t find file or read data")
    else:
        file1 = file1.split("\n") # Содержимое файла разделяется на строки с помощью метода split("\n"), чтобы получить список слов из словаря.
        word = word.upper()
        if word in file1:
            checksBool = True
        else:
            checksBool = False
        dicfile.close()
        return checksBool
