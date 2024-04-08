def place_word_in_matrix(matrix, word, row, col, direction):
    if direction == 'horizontal':
        for i, letter in enumerate(word):
            matrix[row][col + i] = letter
    elif direction == 'vertical':
        for i, letter in enumerate(word):
            matrix[row + i][col] = letter

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

def main():
    # Создаем матрицу 15 на 15, заполненную пробелами
    matrix = [[' ' for _ in range(15)] for _ in range(15)]

    # Слово для размещения
    word = "пример"

    # Начальные координаты и направление
    row = 5
    col = 5
    direction = 'horizontal'

    # Размещаем слово в матрице
    place_word_in_matrix(matrix, word, row, col, direction)

    # Выводим матрицу на экран
    print_matrix(matrix)

if __name__ == "__main__":
    main()
