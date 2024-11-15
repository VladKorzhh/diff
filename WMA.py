def weighted_moving_average(data, weights):
    """
    Вычисление взвешенного скользящего среднего (WMA).
    
    :param data: Список чисел (данные).
    :param weights: Список весов (должен совпадать по длине с окном).
    :return: Список значений WMA.
    """
    if not data or not weights:
        raise ValueError("Данные и веса не должны быть пустыми.")
    if len(weights) > len(data):
        raise ValueError("Размер весов не должен превышать размер данных.")
    
    # Длина окна
    window_size = len(weights)
    # Нормализация весов (на случай, если они не нормализованы)
    weight_sum = sum(weights)
    normalized_weights = [w / weight_sum for w in weights]
    
    # Результирующий список WMA
    wma = []
    
    # Скользящее окно
    for i in range(len(data) - window_size + 1):
        # Текущие данные в окне
        window = data[i:i + window_size]
        # Скалярное произведение данных окна и нормализованных весов
        wma_value = sum(x * w for x, w in zip(window, normalized_weights))
        wma.append(wma_value)
    
    return wma


# Пример использования
data = [10, 20, 30, 40, 50, 60]
weights = [0.1, 0.3, 0.6]  # Более свежие значения имеют больший вес

result = weighted_moving_average(data, weights)
print("WMA:", result)
