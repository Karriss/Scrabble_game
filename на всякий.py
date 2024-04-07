import random

# Создаем 7 квадратов с буквами и добавляем им теги
for i in range(7):
    x_k1 = x_kv + i * square_size
    y_k1 = y_kv
    x_k2 = x_k1 + square_size
    y_k2 = y_k1 + square_size
    canvas.create_rectangle(x_k1, y_k1, x_k2, y_k2, fill="white", tags=("kv_square", f"kv_{i}"))
    
    # Сгенерируем случайные позиции для размещения буквы внутри квадрата
    rand_x = random.randint(x_k1, x_k2)
    rand_y = random.randint(y_k1, y_k2)
    
    # Размещаем букву в случайной позиции внутри квадрата
    canvas.create_text(rand_x, rand_y, text="ABCDEF"[i], font=("Arial", 16), tags=f"kv_{i}_text")